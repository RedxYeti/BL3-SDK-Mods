from typing import Any
from mods_base import hook, build_mod, BoolOption 
from unrealsdk.hooks import Type
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
    response = obj.Sphere.BodyInstance.CollisionResponses.ResponseToChannels
    if args.NewState in orb_states:
        for channel in collision_channels:
            setattr(response, channel, 0)
    else:
        for channel in collision_channels:
            setattr(response, channel, 1)
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