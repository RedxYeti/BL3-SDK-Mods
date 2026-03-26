from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import _create_manufacturer_pool, Manufacturer


VLADOFAR: Manufacturer = Manufacturer(
    name="vladof_ars",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_01_Common.Balance_AR_VLA_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_02_UnCommon.Balance_AR_VLA_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_03_Rare.Balance_AR_VLA_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_04_VeryRare.Balance_AR_VLA_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/VLA/Balance/Balance_AR_VLA_ETech_Rare.Balance_AR_VLA_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/VLA/Balance/Balance_AR_VLA_ETech_VeryRare.Balance_AR_VLA_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc.Balance_AR_VLA_BigSucc',  
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator.Balance_AR_VLA_Dictator',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor.Balance_AR_VLA_Faisor',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall.Balance_AR_VLA_LuciansCall',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre.Balance_AR_VLA_Ogre',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier.Balance_AR_VLA_Sherdifier',
        '/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger.Balance_AR_VLA_WebSlinger', 
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/DowsingRod/Balance/Balance_AR_VLA_Dowsing.Balance_AR_VLA_Dowsing',
    ]
)

ATLASAR: Manufacturer = Manufacturer(
    name="atlas_ars",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common.Balance_ATL_AR_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon.Balance_ATL_AR_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare.Balance_ATL_AR_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare.Balance_ATL_AR_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier',
        '/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell.Balance_ATL_AR_RebelYell',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ.Balance_ATL_AR_OPQ',
    ]
)

COVAR: Manufacturer = Manufacturer(
    name="cov_ars",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_01_Common.Balance_AR_COV_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_02_UnCommon.Balance_AR_COV_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_03_Rare.Balance_AR_COV_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_04_VeryRare.Balance_AR_COV_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/COV/Balance/Balance_AR_COV_ETech_Rare.Balance_AR_COV_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/COV/Balance/Balance_AR_COV_ETech_VeryRare.Balance_AR_COV_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR',
        '/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar.Balance_AR_COV_Sawbar',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse.Balance_AR_COV_Sawhorse',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse_Epic.Balance_AR_COV_Sawhorse_Epic',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew.Balance_AR_COV_PewPew',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Shock.Balance_AR_COV_BioBetsy_Shock',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom',
    ]
)

DAHLAR: Manufacturer = Manufacturer(
    name="dahl_ars",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_01_Common.Balance_DAL_AR_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_02_UnCommon.Balance_DAL_AR_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_03_Rare.Balance_DAL_AR_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_04_VeryRare.Balance_DAL_AR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/Dahl/Balance/Balance_DAL_AR_ETech_Rare.Balance_DAL_AR_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/Dahl/Balance/Balance_DAL_AR_ETech_VeryRare.Balance_DAL_AR_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD.Balance_DAL_AR_BOTD',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage.Balance_DAL_AR_Barrage',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos.Balance_DAL_AR_Kaos',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix.Balance_DAL_AR_StarHelix',
        '/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord.Balance_DAL_AR_Warlord',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender.Balance_DAL_AR_Soulrender',
        '/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/Corruption/Balance/Balance_DAL_AR_Corruption.Balance_DAL_AR_Corruption',
    ]
)

JAKOBSAR: Manufacturer = Manufacturer(
    name="jakobs_ar",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_01_Common.Balance_AR_JAK_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_02_UnCommon.Balance_AR_JAK_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_03_Rare.Balance_AR_JAK_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_04_VeryRare.Balance_AR_JAK_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah.Balance_AR_JAK_Bekah',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun.Balance_AR_JAK_04_GatlingGun',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory.Balance_AR_JAK_HandOfGlory',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler.Balance_AR_JAK_LeadSprinkler',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle.Balance_AR_JAK_PasRifle',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall.Balance_AR_JAK_RowansCall',
        '/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath.Balance_AR_JAK_TraitorsDeath',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/CoolBeans/Balance/Balance_AR_JAK_CoolBeans.Balance_AR_JAK_CoolBeans',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/McSmugger/Balance/Balance_AR_JAK_McSmugger.Balance_AR_JAK_McSmugger',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/StoneThrow/Balance/Balance_AR_JAK_Stonethrow.Balance_AR_JAK_Stonethrow',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant',
        '/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/BladeFury/Balance/Balance_AR_JAK_BladeFury.Balance_AR_JAK_BladeFury',
    ]
)

TORGUEAR: Manufacturer = Manufacturer(
    name="torgue_ars",
    non_uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_01_Common.Balance_AR_TOR_01_Common',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_02_UnCommon.Balance_AR_TOR_02_UnCommon',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_03_Rare.Balance_AR_TOR_03_Rare',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_04_VeryRare.Balance_AR_TOR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/TOR/Balance/Balance_AR_TOR_ETech_Rare.Balance_AR_TOR_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/TOR/Balance/Balance_AR_TOR_ETech_VeryRare.Balance_AR_TOR_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist.Balance_AR_TOR_Alchemist',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement.Balance_AR_TOR_AmberManagement',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat.Balance_AR_TOR_Bearcat',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder.Balance_AR_TOR_LaserSploder',
        '/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt.Balance_AR_TOR_TryBolt',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue.Balance_AR_TOR_LovableRogue',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue_Epic.Balance_AR_TOR_LovableRogue_Epic',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ContainedExplosion/Balance/Balance_AR_TOR_Contained.Balance_AR_TOR_Contained',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/HotfootTeddy/Balance/Balance_AR_TOR_Hotfoot.Balance_AR_TOR_Hotfoot',
    ]
)

ars_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/AssaultRifles/ItemPool_AssaultRifles_Common.ItemPool_AssaultRifles_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_AssaultRifle.Att_MinGameStage_AssaultRifle')


def _init_ars():
    manufacturers = [VLADOFAR, ATLASAR, COVAR, DAHLAR, JAKOBSAR, TORGUEAR]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,ars_common,min_game_stage)

    #for manu in [VLADOFAR, ATLASAR, COVAR, DAHLAR, JAKOBSAR, TORGUEAR]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")