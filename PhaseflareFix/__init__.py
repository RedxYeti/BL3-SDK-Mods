from typing import Any
from mods_base import hook, build_mod, BoolOption 
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct 


orb_states = [3,4]

@hook(
    "/Game/PlayerCharacters/SirenBrawler/_DLC/Ixora/Phasetrance/Projectiles/Proj_Siren_DLCSkill_WalkingPotato_Base.Proj_Siren_DLCSkill_WalkingPotato_Base_C:SetOrbState",
    Type.PRE
    )
def PhasePhlarePhix(obj: UObject, args: WrappedStruct, *_) -> None:
    if args.NewState in orb_states:
        obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels.WorldStatic = 0
        obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels.WorldDynamic = 0
    else:
        obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels.WorldStatic = 1
        obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels.WorldDynamic = 1
    return

 
def orb_option(option, new_value):
    global orb_states
    orb_states = [2,3,4] if new_value else [3,4]

oidCollisionAmount = BoolOption(
    "Collision Amount",
    False,
    "No Collision",
    "Less Collision",
    description=("Controls how much collision is removed from the orb."
                "\n\nLess collision will be good in most cases but will still get stuck from time to time."
                "\n\nNo collision means it will almost never get stuck, but if you melee it in a direction with no enemies, it may keep going that direction forever until you call it back."),
    on_change=orb_option
)

build_mod()