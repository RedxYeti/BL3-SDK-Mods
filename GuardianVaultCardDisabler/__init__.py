from typing import Any 
from mods_base import hook, build_mod, BoolOption
from unrealsdk.hooks import Block 
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct 

@hook("/Script/OakGame.PlayerGuardianRankComponent:NotifyUncappedExperienceAdded")
@hook("/Script/OakGame.GFxExperienceBar:HandleGuardianExperienceAdded")
@hook("/Script/OakGame.OakPlayerController:NotifyUncappedExperienceAdded")
def NotifyExperienceAdded(*_) -> Any:
    return Block


@hook("/Script/OakGame.GFxExperienceBar:extFinishedDim")
def RankDisabler(obj:UObject,*_) -> Any:
    if oidAutoDisableGuardianRank.value:
        obj.GetOwningPlayerController().PlayerGuardianRankComponent.bGuardianRankSystemEnabled = False


oidAutoDisableGuardianRank = BoolOption(
    "Auto Disable Guardian Rank",
    False,
    "On",
    "Off",
    description="Automatically disables Guardian Rank, mostly for new characters."
)

build_mod()