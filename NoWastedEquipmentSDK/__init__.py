from typing import Any
from mods_base import hook, build_mod, ENGINE, ObjectFlags
from unrealsdk import find_object
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct 


Att_CharacterWeight_Gunner = find_object('GbxAttributeData','/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Gunner.Att_CharacterWeight_Gunner')
Att_CharacterWeight_Beastmaster = find_object('GbxAttributeData','/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Beastmaster.Att_CharacterWeight_Beastmaster')
Att_CharacterWeight_Operative = find_object('GbxAttributeData','/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Operative.Att_CharacterWeight_Operative')
Att_CharacterWeight_Siren = find_object('GbxAttributeData','/Game/GameData/Loot/CharacterWeighting/Att_CharacterWeight_Siren.Att_CharacterWeight_Siren')

weights = [Att_CharacterWeight_Gunner,
Att_CharacterWeight_Beastmaster,
Att_CharacterWeight_Operative,
Att_CharacterWeight_Siren]


def update_weights():
    characters = []
    for player in ENGINE.GameViewport.World.GameState.PlayerArray:
        if not player.Owner.GetCurrentPlayerClass():
            return
        character_split = str(player.Owner.GetCurrentPlayerClass().Name).split("_")[-1].lower()
        characters.append(character_split)

    for weight in weights:
        val = 1 if any(character in str(weight).lower() for character in characters) else 0
        for resolver in (weight.ValueResolver.ValueA, weight.ValueResolver.ValueB):
            resolver.BaseValueConstant = val
            resolver.BaseValueAttribute = None
            resolver.BaseValueScale = val


@hook("/Script/Engine.PlayerController:ServerNotifyLoadedWorld", Type.POST)
def NoWastedEquipment_ServerNotify(*_) -> None:
    NoWastedEquipment_FinishedDims.enable()


@hook("/Script/OakGame.GFxExperienceBar:extFinishedDim", Type.POST)
def NoWastedEquipment_FinishedDims(*_) -> None:
    update_weights()
    NoWastedEquipment_FinishedDims.disable()


@hook("/Script/OakGame.OakPlayerController:ClientDoLateJoinFadeIn", Type.POST)
def NoWastedEquipment_LateJoin(*_) -> None:
    update_weights()


build_mod()