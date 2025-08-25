from typing import Any
from mods_base import hook, build_mod, BoolOption 
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

 

oidFFYL = BoolOption(
    "Enabled During FFYL",
    False,
    "On",
    "Off",
    description=("Stops the orb from breaking while you're in fight for your life."),
)

build_mod()