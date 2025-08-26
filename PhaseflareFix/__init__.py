from typing import Any
from mods_base import hook, build_mod, BoolOption
from unrealsdk import make_struct
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct 


orb_states = [3,4]

collision_channels = ['WorldStatic',
                      'WorldDynamic',
                      'Visibility',
                      'Camera',
                      'PhysicsBody',
                      'Vehicle',
                      'Destructible',
                      'EngineTraceChannel1',
                      'EngineTraceChannel2',
                      'EngineTraceChannel3',
                      'EngineTraceChannel4',
                      'EngineTraceChannel5',
                      'EngineTraceChannel6',
                      'GameTraceChannel1',
                      'GameTraceChannel2',
                      'GameTraceChannel3',
                      'GameTraceChannel4',
                      'GameTraceChannel5',
                      'GameTraceChannel6',
                      'GameTraceChannel7',
                      'GameTraceChannel8',
                      'GameTraceChannel9',
                      'GameTraceChannel10',
                      'GameTraceChannel11',
                      'GameTraceChannel12',
                      'GameTraceChannel13',
                      'GameTraceChannel14',
                      'GameTraceChannel15',
                      'GameTraceChannel16',
                      'GameTraceChannel17',
                      'GameTraceChannel18',
                      ]

@hook(
    "/Game/PlayerCharacters/SirenBrawler/_DLC/Ixora/Phasetrance/Projectiles/Proj_Siren_DLCSkill_WalkingPotato_Base.Proj_Siren_DLCSkill_WalkingPotato_Base_C:SetOrbState",
    Type.PRE
    )
def PhasePhlarePhix(obj: UObject, args: WrappedStruct, *_) -> None:
    if args.NewState == 2:
        if oidForceFinalHeight.value and (not obj.MyHomingTarget or obj.MyHomingTarget == obj.Instigator):
            finalZ = obj.Instigator.K2_GetActorLocation().Z 
            finalZ += 50

            self_loc = obj.K2_GetActorLocation()
            selfX = self_loc.X
            selfY = self_loc.Y
            final_loc = make_struct("Vector", X=selfX, Y=selfY, Z=finalZ)

            obj.K2_SetActorLocation(final_loc, True, make_struct("HitResult"), False)

        elif oidForceFinalLoc.value and obj.MyHomingTarget and obj.MyHomingTarget != obj.Instigator:
            obj.K2_SetActorLocation(obj.MyHomingTarget.K2_GetActorLocation(), True, make_struct("HitResult"), True)
        return
        

    response = obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels
    if args.NewState in orb_states:
        for channel in collision_channels:
            setattr(response, channel, 0)
    else:
        for channel in collision_channels:
            setattr(response, channel, 1)
    return


@hook("/Script/OakGame.OakActionAbility:OnStopActionAbility",Type.PRE)
@hook("/Script/OakGame.OakActionAbility:OnPlayerDeadOrDying",Type.PRE)
def PhasePhlareDowned(obj: UObject, args: WrappedStruct, *_):
    if not oidFFYL.value:
        return

    if obj.Class.Name != "ActionSkill_Siren_Phasetrance_C" or not obj.DLCSkillOrb:
        return

    if obj.GetDurationPercent() > 0 and obj.GetOakPlayerController().Pawn.FFYLComponent.CurrentDownState == 1:
        return Block
    
@hook("/Script/OakGame.PlayerMeleeStateComponent:PerformPlayerMelee",Type.POST)
def PhasePhlareMelee(obj: UObject, args: WrappedStruct, *_):
    if not oidMeleeAutoAim.value or not obj.CurrentMeleeTarget:
        return
    

    if obj.CurrentMeleeTarget.Class.Name == "Proj_Siren_DLCSkill_WalkingPotato_Attack_1_C":
        obj.ActivePlayerMeleeData.bUseTargetHoming = False


oidFFYL = BoolOption(
    "Enabled During FFYL",
    False,
    "On",
    "Off",
    description=("Stops the orb from breaking while you're in fight for your life."),
)

oidMeleeAutoAim = BoolOption(
    "Disable Melee Auto Aim",
    True,
    "On",
    "Off",
    description=("Disables your camera automatically aiming to the orb. Does not affect meleeing enemies."),
)

oidForceFinalLoc = BoolOption(
    "Force Final Location To Target",
    True,
    "On",
    "Off",
    description=("Forces the orb to teleport to it's target after it's finishing homing."),
)

oidForceFinalHeight = BoolOption(
    "Force Final Height to Player Height",
    True,
    "On",
    "Off",
    description=("If the orb doesn't have target, when the orb stops moving it will move to the same height as the player."),
)

build_mod()