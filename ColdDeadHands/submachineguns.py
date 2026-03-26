from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import _create_manufacturer_pool, Manufacturer


DAHLSMG: Manufacturer = Manufacturer(
    name="dahl_smgs",
    non_uniques=[
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_01_Common.Balance_SM_DAHL_01_Common',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_02_UnCommon.Balance_SM_DAHL_02_UnCommon',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_03_Rare.Balance_SM_DAHL_03_Rare',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_04_VeryRare.Balance_SM_DAHL_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Dahl/Balance/Balance_SM_DAL_ETech_Rare.Balance_SM_DAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Dahl/Balance/Balance_SM_DAL_ETech_VeryRare.Balance_SM_DAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag.Balance_SM_DAL_Demoskag',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire.Balance_SM_DAHL_HellFire',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper.Balance_SM_DAL_Ripper',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant.Balance_SM_DAL_SleepingGiant',
        '/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher.Balance_SM_DAHL_Vanquisher',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Torrent/Balance/Balance_SM_DAL_Torrent.Balance_SM_DAL_Torrent',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast.Balance_SM_DAL_ETech_AshenBeast',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast_Epic.Balance_SM_DAL_ETech_AshenBeast_Epic',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer',
    ],
)

HYPERIONSMG: Manufacturer = Manufacturer(
    name="hyperion_smgs",
    non_uniques=[
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_01_Common.Balance_SM_HYP_01_Common',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_02_UnCommon.Balance_SM_HYP_02_UnCommon',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_03_Rare.Balance_SM_HYP_03_Rare',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_04_VeryRare.Balance_SM_HYP_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Hyperion/Balance/Balance_SM_HYP_ETech_Rare.Balance_SM_HYP_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Hyperion/Balance/Balance_SM_HYP_ETech_VeryRare.Balance_SM_HYP_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch.Balance_SM_HYP_Bitch',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad.Balance_SM_HYP_Crossroad',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome.Balance_SM_HYP_Handsome',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3.Balance_SM_HYP_L0V3M4CH1N3',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending.Balance_SM_HYP_PredatoryLending',
        '/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ.Balance_SM_HYP_XZ',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker.Balance_SM_HYP_Pricker',
        '/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog.Balance_SM_HYP_Smog',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Copybeast/Balance/Balance_SM_HYP_Copybeast.Balance_SM_HYP_Copybeast',
        '/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/Troubleshooter/Balance/Balance_SM_HYP_ETech_Troubleshooter.Balance_SM_HYP_ETech_Troubleshooter',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian',
        '/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/GoldRush/Balance/Balance_SM_HYP_GoldRush.Balance_SM_HYP_GoldRush',
    ],
)

TEDIORESMG: Manufacturer = Manufacturer(
    name="tediore_smgs",
    non_uniques=[
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_01_Common.Balance_SM_TED_01_Common',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_02_UnCommon.Balance_SM_TED_02_UnCommon',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_03_Rare.Balance_SM_TED_03_Rare',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_04_VeryRare.Balance_SM_TED_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Tediore/Balance/Balance_SM_TED_ETech_Rare.Balance_SM_TED_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Tediore/Balance/Balance_SM_TED_ETech_VeryRare.Balance_SM_TED_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans.Balance_SM_TED_Beans',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower.Balance_SM_TED_NotAFlamethrower',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind.Balance_SM_TED_SpiderMind',
        '/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon.Balance_SM_TED_TenGallon',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3.Balance_SM_TED_PatMk3',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3_Epic.Balance_SM_TED_PatMk3_Epic',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun.Balance_SM_TED_NeedleGun',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Earthbound/Balance/Balance_SM_TED_Earthbound.Balance_SM_TED_Earthbound',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/DarkArmy/Balance/Balance_SM_TED_DarkArmy.Balance_SM_TED_DarkArmy',
    ],
)

MALIWANSMG: Manufacturer = Manufacturer(
    name="maliwan_smgs",
    non_uniques=[
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_01_Common.Balance_SM_MAL_01_Common',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_02_UnCommon.Balance_SM_MAL_02_UnCommon',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_03_Rare.Balance_SM_MAL_03_Rare',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare.Balance_SM_MAL_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_Rare.Balance_SM_MAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_VeryRare.Balance_SM_MAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse',
        '/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA.Balance_SM_MAL_DNA',
        '/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce.Balance_SM_MAL_SFForce',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Balance/Balance_SM_MAL_PlasmaCoil.Balance_SM_MAL_PlasmaCoil',
    ],
)

smgs_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/SMG/ItemPool_SMGs_Common.ItemPool_SMGs_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_SMG.Att_MinGameStage_SMG')


def _init_smgs():
    manufacturers = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,smgs_common,min_game_stage)

    #for manu in [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")