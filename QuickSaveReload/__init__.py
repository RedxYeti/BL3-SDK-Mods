from mods_base import build_mod#type:ignore
from ui_utils import show_hud_message#type:ignore
from typing import Any #type:ignore
import unrealsdk#type:ignore
from unrealsdk import make_struct, find_all #type:ignore
from mods_base import get_pc, hook, keybind, build_mod, ENGINE, SliderOption, BoolOption #type:ignore
from unrealsdk.hooks import Type, add_hook, Block, remove_hook, inject_next_call #type:ignore
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct #type:ignore
from ui_utils import show_hud_message #type:ignore


def ServerUpdateLevelVisibility(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    for item in unrealsdk.find_all("GbxGFxListCell"):
        if item and item.ListIndex != -1 and "OnPlayClicked" in str(item.OnClicked):
            item.OwningMovie.OnContinueClicked(item, unrealsdk.make_struct("GbxMenuInputEvent"))

    remove_hook("/Game/Maps/MenuMap/MenuMap_P.MenuMap_P_C:FadeDownBlackScreen__FinishedFunc", Type.POST, "ServerUpdateLevelVisibility")
    return 


@keybind("Save Quit, Reload")
def SaveQuit():
    if "MenuMap_P" not in str(ENGINE.GameViewport.World.CurrentLevel):
        unrealsdk.construct_object("GFxPauseMenu", get_pc()).OnQuitChoiceMade(None, "GbxMenu_Secondary1", unrealsdk.make_struct("GbxMenuInputEvent"))
        add_hook("/Game/Maps/MenuMap/MenuMap_P.MenuMap_P_C:FadeDownBlackScreen__FinishedFunc", Type.POST, "ServerUpdateLevelVisibility", ServerUpdateLevelVisibility)
    return


build_mod()

