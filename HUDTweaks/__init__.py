from mods_base import build_mod#type:ignore
from ui_utils import show_hud_message#type:ignore
from typing import Any #type:ignore
import unrealsdk#type:ignore
from unrealsdk import make_struct, find_all #type:ignore
from mods_base import get_pc, hook, keybind, build_mod, ENGINE, SliderOption, BoolOption, SpinnerOption #type:ignore
from unrealsdk.hooks import Type, add_hook, Block, remove_hook #type:ignore
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WeakPointer #type:ignore
from ui_utils import show_hud_message #type:ignore

oidScale = SliderOption("HUD Scale", 
                         100, 
                         0, 
                         200, 
                         1, 
                         True, 
                         description="Set the scale you want your HUD to be.")



oidHideGuardianRankBar: BoolOption = BoolOption("Hide Guardian Rank Bar",
                                              False,
                                              "Hide",
                                              "Show",
                                              description="Hides the Guardian Rank bar above the XP bar.")


oidHideVaultCardBar: BoolOption = BoolOption("Hide Vault Card Bar",
                                           False,
                                           "Hide",
                                           "Show",
                                           description="Hides the Vault Card bar below the XP bar.")


oidSkillPointNotif: SpinnerOption = SpinnerOption("Skill Point Notification",
                                                "Skill and Guardian",
                                                ["Skill and Guardian", "Skill Only", "Nothing"], 
                                                wrap_enabled = True,
                                                description="Choose what notification messages show above the XP bar.")


oidHidePlayerClass: SpinnerOption = SpinnerOption("Healthbar Player Class",
                                                   value="Character Class",
                                                   choices=["Character Class", "Class Mod", "Nothing"],
                                                   wrap_enabled = True,
                                                   description="Choose what shows next to your healthbar.")


RarityColors = {
    "Common": "#FFFFFF",
    "Uncommon": "#32C339",
    "Rare": "#0E69E0",
    "Epic": "#C237CC",
    "Legendary": "#FF8E04",
}


def HideStuff(XPBar):
    if not XPBar:
        return

    if oidSkillPointNotif.value == "Nothing":
        XPBar.SkillPointsAvailableWrapper.SetVisible(False)

    elif oidSkillPointNotif.value == "Skill Only":
        if XPBar.CachedRemainingSkillPoints >= 1:
            XPBar.SkillPointsAvailableWrapper.SetVisible(True)
        else:
            XPBar.SkillPointsAvailableWrapper.SetVisible(False)

    if oidHideGuardianRankBar.value:
        XPBar.GuardianXPProgressBar.SetVisible(False)
        
    if oidHideVaultCardBar.value:
        XPBar.VaultCardXPProgressBar.SetVisible(False)

    if oidHidePlayerClass.value == "Nothing" and XPBar.GetOwningPlayerController().GetCurrentPlayerClass():
        XPBar.GetOwningPlayerController().GetCurrentPlayerClass().DisplayName = ""
    return


def SetScale(PC):
    if not PC.OakHUD or not PC.OakHUD.GFxHUDContainer:
        return

    for item in unrealsdk.find_all("GbxGFxMovie", False):
        if item in PC.OakHUD.GFxHUDContainer.Widgets:
            data = item.AnchorData

            Scale = oidScale.value / 100
            data.Scale.X = Scale
            data.Scale.Y = Scale

            item.SetAnchor(data)
    return


@hook("/Script/GbxUI.GbxGFxHUDWidget:extInitAnimationFinished", Type.POST)
@hook("/Script/GbxUI.GbxGFxHUDWidget:extHideAnimationFinished", Type.POST)
@hook("/Script/OakGame.GFxExperienceBar:extFinishedDim", Type.POST)
@hook("/Script/OakGame.OakHUD:StateChanged", Type.POST)
def extInitAnimationFinished(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if oidScale.value != 100:
        if func.func.Name == "StateChanged":
            SetScale(obj.OakPlayerOwner)
        else:
            SetScale(obj.GetOwningPlayerController())

    if func.func.Name == "extFinishedDim":
        HideStuff(obj)
    return


@hook("/Script/OakGame.OakInventoryEquippableItem:OnEquipped", Type.PRE)
def OnEquipped(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    if oidHidePlayerClass.value != "Class Mod":
        return

    if obj.Class.Name == "BPClass_ClassMod_C":
        InventoryState = obj.InventoryBalanceState
        Name = InventoryState.NamePartList[-1].PartName
        Color = str(InventoryState.InventoryBalanceData.RarityData.RarityFrameName)
        CurrentClassMod = f"<font color='{RarityColors[Color]}'>{Name}</font>"
        get_pc().GetCurrentPlayerClass().DisplayName = CurrentClassMod

    return



build_mod(options = [oidScale, oidSkillPointNotif, oidHideGuardianRankBar, oidHideVaultCardBar, oidHidePlayerClass])