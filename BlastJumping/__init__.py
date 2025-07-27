from typing import Any 
from mods_base import hook, build_mod, SliderOption, GroupedOption, BoolOption
from unrealsdk import make_struct, find_class, find_object, find_all
from unrealsdk.hooks import Type 
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WeakPointer 


audio_lib = find_class("BPF_AudioFunctionLibrary_C").ClassDefaultObject

fly_speed = make_struct("GbxAttributeFloat",Value=100000,BaseValue=100000)

source_heavy = '/Game/GameData/DamageSources/DamageSource_Bullet_Heavy.DamageSource_Bullet_Heavy_C'
source_torgue_shotgun = "/Game/GameData/DamageSources/DamageSource_Bullet_Shotgun.DamageSource_Bullet_Shotgun_C"
source_torgue_ar = "/Game/GameData/DamageSources/DamageSource_Bullet_AssaultRifle.DamageSource_Bullet_AssaultRifle_C"
source_torgue_pistol = "/Game/GameData/DamageSources/DamageSource_Bullet_Pistol.DamageSource_Bullet_Pistol_C"
sources = [source_heavy, source_torgue_shotgun, source_torgue_ar, source_torgue_pistol]

character_classes = ["BPChar_Operative_C","BPChar_Siren_C","BPChar_Gunner_C","BPChar_Beastmaster_C"]

def get_launch_vector(origin_location, player_location, mag, current_velocity, force_strength):
    dx = player_location.X - origin_location.X 
    dy = player_location.Y - origin_location.Y
    dz = player_location.Z - origin_location.Z

    nx = dx / mag
    ny = dy / mag
    nz = dz / mag

    force_x = nx * force_strength
    force_y = ny * force_strength
    force_z = nz * force_strength

    final_velocity_x = current_velocity.X + force_x
    final_velocity_y = current_velocity.Y + force_y
    final_velocity_z = current_velocity.Z + force_z

    return make_struct("Vector",
        x=final_velocity_x,
        y=final_velocity_y,
        z=final_velocity_z,
    )


def setup(character_movement, damage_component):
    damage_component.MaxSelfInflictedLaunchVelocity = 0
    damage_component.LaunchVerticalDampening = -10
    character_movement.AirControl  = oidAirControl.value
    character_movement.BrakingFrictionBoostWhenExceedingMaxSpeed = oidFrictionMaxSpeed.value
    character_movement.BrakingDecelerationFlying = oidGroundFriction.value
    character_movement.MaxFlySpeed = fly_speed
    character_movement.BrakingDecelerationFallingBoostWhenExceedingMaxSpeed = 0

    """
    vanilla values
    MaxSelfInflictedLaunchVelocity >>> 250.0
    LaunchVerticalDampening >>> 0.5
    AirControl >>> 0.6
    MaxFlySpeed >>> {Value: 600.0, BaseValue: 600.0}
    BrakingDecelerationFallingBoostWhenExceedingMaxSpeed >>> 2000.0
    BrakingFrictionBoostWhenExceedingMaxSpeed >>> 0.1
    BrakingDecelerationFlying >>> 2048.0
    """
    #print(character_movement.CrouchedHalfHeight)

    


def do_blast_jump(player_pawn:UObject, blast_location:WrappedStruct, blast_modifier:float) -> None:
    if blast_modifier <= 0:
        return
    blast = make_struct("Vector",X=blast_location.X, Y=blast_location.Y,Z=blast_location.Z)
    player_loc = player_pawn.K2_GetActorLocation()
    _, mag = audio_lib.GetDistanceBetweenVectors(blast, player_loc, None, 0)
    if mag > 350:
        return
    character_movement = player_pawn.OakCharacterMovement
    setup(character_movement, player_pawn.OakDamageComponent) #runs everytime for coop joiners
    current_vel = character_movement.Velocity
    force = 1650 * blast_modifier #1650 was just kinda fun so i made it the baseline for launchers
    new_vel = get_launch_vector(blast_location, player_loc, mag, current_vel, force)
    player_pawn.LaunchPawn(new_vel, True, True)


player_nades = []
@hook("/Script/Engine.Actor:ReceiveDestroyed", Type.POST)
def ReceiveDestroyed(obj: UObject,args: WrappedStruct,ret: Any,func: BoundFunction) -> Any:
    if "grenade" not in str(obj).lower():
        return

    if not obj.Instigator or obj.Instigator.Class.Name not in character_classes:
        return
    
    for nade in player_nades[:]:
        if not nade():
            player_nades.remove(nade)
            continue
        
        if obj == nade():
            do_blast_jump(obj.Instigator, obj.K2_GetActorLocation(), oidGrenadeForce.value)
            player_nades.remove(nade)
    
    if not len(player_nades):
        ReceiveDestroyed.disable()


@hook("/Script/GbxWeapon.Projectile:OnExplode", Type.PRE)
def Projectile(obj: UObject,args: WrappedStruct,ret: Any,func: BoundFunction,) -> Any:
    if obj.Instigator and obj.Instigator.Class.Name in character_classes:
        player_nades.append(WeakPointer(obj))
        ReceiveDestroyed.enable()




@hook("/Game/Gear/Weapons/_Shared/_Design/Projectiles/Proj_Weapon_BaseProjectile.Proj_Weapon_BaseProjectile_C:OnExplode", Type.POST)
def Proj_Weapon_BaseProjectile_C(obj: UObject,args: WrappedStruct,ret: Any,func: BoundFunction,) -> None:
    last_projectile = obj
    projectile_source = obj.GbxCharacter
    #print(projectile_source.Class.Name)
    #print(f"type >>> {last_projectile.DamageType._path_name()} source >>> {last_projectile.DamageSource._path_name()} >>> func {func.func}")
    if projectile_source.Class.Name not in character_classes:
        return

    if last_projectile.DamageSource._path_name() == source_heavy:
        blast_mod = oidLauncherForce.value
    else:
        blast_mod = oidTorgueForce.value

    if last_projectile.DamageSource._path_name() in sources:
        do_blast_jump(projectile_source, last_projectile.K2_GetActorLocation(), blast_mod)




@hook("/Script/GbxWeapon.LightProjectileData:OnExplode", Type.POST)
@hook("/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/COV/HW/Projectiles/LightProjectile_HW_COV_TrashBall.LightProjectile_HW_COV_TrashBall_C:OnExplode", Type.POST)
def LightProjectileData(obj: UObject,args: WrappedStruct,ret: Any,func: BoundFunction,) -> None:
    last_projectile = args.Projectile
    projectile_source = last_projectile.GetSource()
    #print(projectile_source.OakCharacter.Class.Name)
    #print(f"type >>> {last_projectile.DamageType._path_name()} source >>> {last_projectile.DamageSource._path_name()} >>> func {func.func}")
    if (not hasattr(projectile_source, "OakCharacter")
        or not projectile_source.OakCharacter
        or projectile_source.OakCharacter.Class.Name not in character_classes):
        return
    

    if last_projectile.DamageSource._path_name() == source_heavy:
        blast_mod = oidLauncherForce.value
    else:
        blast_mod = oidTorgueForce.value

    if last_projectile.DamageSource._path_name() in sources:
        do_blast_jump(projectile_source.OakCharacter, last_projectile.ImpactInfo.Location, blast_mod)


oidLauncherForce = SliderOption(
    "Rocket Launcher Force",
    1,
    0,
    5,
    0.1,
    is_integer=False,
    description="Controls how strong the rocket launcher blasts are."
)
oidGrenadeForce = SliderOption(
    "Grenade Force",
    0.7,
    0,
    5,
    0.1,
    is_integer=False,
    description="Controls how strong the grenade blasts are."
)
oidTorgueForce = SliderOption(
    "Torgue Force",
    0.3,
    0,
    5,
    0.1,
    is_integer=False,
    description="Controls how strong the torgue weapon blasts are, excluding the launchers."
)
force_options = GroupedOption(
    "Force Options",
    [oidLauncherForce, oidGrenadeForce, oidTorgueForce],
)

oidAirControl = SliderOption(
    "Air Control",
    5,
    0,
    20,
    0.1,
    is_integer=False,
    description="Detemines how much control over your character you have in the air.\nMod default: 5\nVanilla Default: 0.6"
)
oidFrictionMaxSpeed = SliderOption(
    "Max Speed Slow Down",
    0.04,
    0,
    0.2,
    0.01,
    is_integer=False,
    description="Detemines how much the game will slow you down while in the air after you hit max speed. Lower = faster.\nMod default: 0.04\nVanilla Default: 0.1"
) 
oidGroundFriction = SliderOption(
    "Ground Friction",
    1200,
    0,
    4000,
    1,
    description="Detemines how much you'll slow down when hitting the ground, affecting your bunny hops.\nMod default: 1200\nVanilla Default: 2048"
)
control_options = GroupedOption(
    "Control Options",
    [oidAirControl, oidFrictionMaxSpeed, oidGroundFriction]
)


tinnitus_small = None
tinnitus_med = None
tinnitus_large = None
blur_value =  None
def bool_change(option, new_value):
    global tinnitus_small, tinnitus_med, tinnitus_large, blur_value 
    gameplay_globals = find_all("GbxGameplayGlobals", False)[-1]#type:ignore
    if not tinnitus_small:
        tinnitus_small = gameplay_globals.ShortDurationTinnitusEvent
        tinnitus_med = gameplay_globals.MediumDurationTinnitusEvent
        tinnitus_large = gameplay_globals.LongDurationTinnitusEvent
        blur_value = gameplay_globals.MinExplosionRadiusToTriggerRadialBlur
    
    if option == oidTinnitus:
        if new_value:
            gameplay_globals.ShortDurationTinnitusEvent = None
            gameplay_globals.MediumDurationTinnitusEvent = None
            gameplay_globals.LongDurationTinnitusEvent = None
        else:
            gameplay_globals.ShortDurationTinnitusEvent = tinnitus_small
            gameplay_globals.MediumDurationTinnitusEvent = tinnitus_med
            gameplay_globals.LongDurationTinnitusEvent = tinnitus_large
    
    elif option == oidBlur:
        gameplay_globals.MinExplosionRadiusToTriggerRadialBlur = -1 if new_value else blur_value

oidTinnitus = BoolOption(
    "Disable Tinnitus Effect",
    True,
    "On",
    "Off",
    description="Disables the tinnitus effect (ear ringing) from explosions.",
    on_change=bool_change
)
oidBlur = BoolOption(
    "Disable Blur Effect",
    True,
    "On",
    "Off",
    description="Disables the screen blurring effect from explosions.",
    on_change=bool_change
)
oidQOL = GroupedOption(
    "QoL Options",
    [oidTinnitus, oidBlur]
)



build_mod(options=[force_options,control_options,oidQOL],
          hooks=[Projectile,LightProjectileData,Proj_Weapon_BaseProjectile_C]
          )