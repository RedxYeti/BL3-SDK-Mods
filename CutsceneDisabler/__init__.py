from typing import Any
from mods_base import hook, build_mod 
from unrealsdk.hooks import Type, Block 
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct 


blacklist_scenes = [
    "/Game/Maps/Zone_1/Towers/Towers_Mission.Towers_Mission:PersistentLevel.SEQ_CraneSpawn",
    "/Game/Maps/Sanctuary3/Sanctuary3_Mission.Sanctuary3_Mission:PersistentLevel.SEQ_Skybox_Planet_Loop_1",
    ]

@hook("/Script/GbxLevelSequence.GbxLevelSequenceActor:OnLevelSequencePlay", Type.POST)
def ForceEndCutscene(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    obj.GoToEndAndStop()
    obj.OnLevelSequenceFinished()
    obj.OnRep_ReplicatedCutsceneSkip()
    obj.bWasCutsceneSkipped = True
    ForceEndCutscene.disable()
    return
 

@hook("/Script/GbxGameSystemCore.ScreenParticleManagerComponent:ClientShowScreenParticleEx", Type.PRE)
def BlockFade(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> Any:
    if args.Template and args.Template.Name == "PS_CIN_Screen_SolidFade_OneSec":
        ForceEndCutscene.enable()
        return Block


build_mod(hooks=[BlockFade])