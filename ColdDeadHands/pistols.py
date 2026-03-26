from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import Manufacturer, _create_manufacturer_pool


JAKOBSPISTOL: Manufacturer = Manufacturer(
    name="jakobs_pistols",
    non_uniques=[
        "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_01_Common.Balance_PS_JAK_01_Common",
        "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_02_UnCommon.Balance_PS_JAK_02_UnCommon",
        "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_03_Rare.Balance_PS_JAK_03_Rare",
        "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_04_VeryRare.Balance_PS_JAK_04_VeryRare",
    ],
    uniques=[
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc.Balance_PS_JAK_TheDuc',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel.Balance_PS_JAK_WagonWheel',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven.Balance_PS_JAK_Unforgiven',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion.Balance_PS_JAK_MelsCompanion',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug.Balance_PS_JAK_Buttplug',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver.Balance_PS_JAK_SpyRevolver',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace.Balance_PS_JAK_AmazingGrace',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent.Balance_PS_JAK_Malevolent',
        '/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother.Balance_PS_JAK_GodMother',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Peashooter/Balance/Balance_PS_JAK_Peashooter.Balance_PS_JAK_Peashooter',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/QuickDraw/Balance/Balance_PS_JAK_QuickDraw.Balance_PS_JAK_QuickDraw',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Rose/Balance/Balance_PS_JAK_Rose.Balance_PS_JAK_Rose',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Trickshot/Balance/Balance_PS_JAK_Trickshot.Balance_PS_JAK_Trickshot',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense.Balance_PS_JAK_TheSeventhSense',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense.Balance_PS_JAK_SeventhSense',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary.Balance_PS_JAK_LoveDrill_Legendary',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill.Balance_PS_JAK_LoveDrill',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti.Balance_PS_JAK_LittleYeeti',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher',
    ]
)

DAHLPISTOL: Manufacturer = Manufacturer(
    name="dahl_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_Common.Balance_DAL_PS_01_Common',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_02_UnCommon.Balance_DAL_PS_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_03_Rare.Balance_DAL_PS_03_Rare',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_04_VeryRare.Balance_DAL_PS_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_Rare.Balance_DAL_PS_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis.Balance_DAL_PS_Nemesis',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet.Balance_DAL_PS_Hornet',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA.Balance_DAL_PS_AAA',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman.Balance_DAL_PS_Rakkman',
        '/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader.Balance_DAL_PS_Omniloader',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/PrivateInvestigator/Balance/Balance_DAL_PS_PrivateInvestigator.Balance_DAL_PS_PrivateInvestigator',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope.Balance_DAL_PS_Kaleidoscope',
    ]
)


TEDIOREPISTOL: Manufacturer = Manufacturer(
    name="tediore_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_01_Common.Balance_PS_Tediore_01_Common',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_02_UnCommon.Balance_PS_Tediore_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_03_Rare.Balance_PS_Tediore_03_Rare',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_04_VeryRare.Balance_PS_Tediore_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_Rare.Balance_PS_Tediore_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang.Balance_PS_TED_Gunerang',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker.Balance_PS_Tediore_BabyMaker',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang.Balance_PS_TED_Bangerang',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute',
        '/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre',
    ]
)


VLADOFPISTOL: Manufacturer = Manufacturer(
    name="vladof_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_01_Common.Balance_PS_VLA_01_Common',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_02_UnCommon.Balance_PS_VLA_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_03_Rare.Balance_PS_VLA_03_Rare',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_04_VeryRare.Balance_PS_VLA_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_Rare.Balance_PS_VLA_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech',
        '/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Balance/Balance_PS_VLA_Lasocannon.Balance_PS_VLA_Lasocannon',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Miscreant/Balance/Balance_PS_VLA_Miscreant.Balance_PS_VLA_Miscreant',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Firefly/Balance/Balance_PS_VLA_Firefly.Balance_PS_VLA_Firefly',
    ]
)

MALIWANPISTOL: Manufacturer = Manufacturer(
    name="maliwan_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_01_Common.Balance_PS_MAL_01_Common',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_02_UnCommon.Balance_PS_MAL_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_03_Rare.Balance_PS_MAL_03_Rare',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare.Balance_PS_MAL_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_Rare.Balance_PS_MAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Deatomizer/Balance/Balance_PS_MAL_Deatomizer.Balance_PS_MAL_Deatomizer',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster.Balance_PS_MAL_BubbleBlaster',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler.Balance_PS_MAL_Decoupler',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil.Balance_PS_MAL_FrozenDevil',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap.Balance_PS_MAL_GreaseTrap',
        '/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator',
    ]
)

COVPISTOL: Manufacturer = Manufacturer(
    name="cov_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_01_Common.Balance_PS_COV_01_Common',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_02_UnCommon.Balance_PS_COV_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_03_Rare.Balance_PS_COV_03_Rare',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_04_VeryRare.Balance_PS_COV_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_Rare.Balance_PS_COV_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion.Balance_PS_COV_Legion',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber.Balance_PS_COV_PsychoStabber',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece.Balance_PS_COV_Mouthpiece',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis.Balance_PS_COV_Skeksis',
        '/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad.Balance_PS_COV_Chad',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Gargoyle/Balance/Balance_PS_COV_Gargoyle.Balance_PS_COV_Gargoyle',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy.Balance_PS_COV_Tizzy',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost.Balance_PS_COV_Hydrafrost',
    ]
)

TORGUEPISTOL: Manufacturer = Manufacturer(
    name="torgue_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_01_Common.Balance_PS_TOR_01_Common',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_02_UnCommon.Balance_PS_TOR_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_03_Rare.Balance_PS_TOR_03_Rare',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_04_VeryRare.Balance_PS_TOR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_Rare.Balance_PS_TOR_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo',
        '/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/TinyTinaGun/Balance/Balance_PS_TOR_TinyTinaGun.Balance_PS_TOR_TinyTinaGun',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy.Balance_PS_TOR_Troy',
        '/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Balance/Balance_PS_TOR_UnkemptHarold.Balance_PS_TOR_UnkemptHarold',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice_Epic.Balance_PS_TOR_Voice_Epic',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice.Balance_PS_TOR_Voice',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville',
        '/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf',
    ]
)

ATLASPISTOL: Manufacturer = Manufacturer(
    name="atlas_pistols",
    non_uniques=[
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common.Balance_PS_ATL_01_Common',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon.Balance_PS_ATL_02_UnCommon',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare.Balance_PS_ATL_03_Rare',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare.Balance_PS_ATL_04_VeryRare',
    ],
    uniques=[
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap.Balance_PS_ATL_DoubleTap',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger.Balance_PS_ATL_Warmonger',
        '/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill.Balance_PS_ATL_Drill',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/SpiritOfMaya/Balance/Balance_PS_ATL_SpiritOfMaya.Balance_PS_ATL_SpiritOfMaya',
        '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay.Balance_PS_ATL_Replay',
    ]
)


pistols_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/Pistols/ItemPool_Pistols_Common.ItemPool_Pistols_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_Pistol.Att_MinGameStage_Pistol')

def _init_pistols():
    manufacturers = [JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,pistols_common,min_game_stage)


    #for manu in [JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")