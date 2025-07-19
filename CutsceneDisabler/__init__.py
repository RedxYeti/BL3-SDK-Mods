from typing import Any
from mods_base import hook, build_mod 
from unrealsdk.hooks import Type, Block 
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct 


@hook("/Script/GbxLevelSequence.GbxLevelSequenceActor:OnLevelSequencePlay", Type.POST)
def ForceEndCutscene(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    obj.GoToEndAndStop()
    obj.OnLevelSequenceFinished()
    obj.OnRep_ReplicatedCutsceneSkip()
    obj.bWasCutsceneSkipped = True
    return
 

@hook("/Script/GbxGameSystemCore.ScreenParticleManagerComponent:ClientShowScreenParticleEx", Type.PRE)
def BlockFade(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> Any:
    if args.Template and args.Template.Name == "PS_CIN_Screen_SolidFade_OneSec":
        return Block


build_mod()