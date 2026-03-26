from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import _create_manufacturer_pool, Manufacturer


ATLASHEAVYWEAPON: Manufacturer = Manufacturer(
    name="atlas_hws",
    non_uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common.Balance_HW_ATL_01_Common',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon.Balance_HW_ATL_02_UnCommon',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare.Balance_HW_ATL_03_Rare',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare.Balance_HW_ATL_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman.Balance_HW_ATL_Freeman',
        '/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath.Balance_HW_ATL_RubysWrath',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Plumage/Balance/Balance_HW_ATL_Plumage.Balance_HW_ATL_Plumage',
    ]
)

COVHEAVYWEAPON: Manufacturer = Manufacturer(
    name="cov_hws",
    non_uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_01_Common.Balance_HW_COV_01_Common',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_02_UnCommon.Balance_HW_COV_02_UnCommon',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_03_Rare.Balance_HW_COV_03_Rare',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_04_VeryRare.Balance_HW_COV_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop.Balance_HW_COV_HotDrop',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper.Balance_HW_COV_PortaPooper',
        '/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror',
        '/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter.Balance_HW_COV_Globetrotter',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher.Balance_HW_COV_BanditLauncher',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher_Epic.Balance_HW_COV_BanditLauncher_Epic',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake.Balance_HW_COV_ETech_YellowCake',
        '/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Mechanic/Balance/Balance_HW_COV_Mechanic.Balance_HW_COV_Mechanic',
    ]
)

TORGUEHEAVYWEAPON: Manufacturer = Manufacturer(
    name="torgue_hws",
    non_uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_01_Common.Balance_HW_TOR_01_Common',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_02_UnCommon.Balance_HW_TOR_02_UnCommon',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_03_Rare.Balance_HW_TOR_03_Rare',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_04_VeryRare.Balance_HW_TOR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/TOR/Balance/Balance_HW_TOR_ETech_Rare.Balance_HW_TOR_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/TOR/Balance/Balance_HW_TOR_ETech_VeryRare.Balance_HW_TOR_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon.Balance_HW_TOR_BurgerCannon',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive.Balance_HW_TOR_Hive',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm.Balance_HW_TOR_Swarm',
        '/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska.Balance_HW_TOR_Tunguska',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague.Balance_HW_TOR_Plague',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Satisfaction/Balance/Balance_HW_TOR_Satisfaction.Balance_HW_TOR_Satisfaction',
    ]
)

VLADOFHEAVYWEAPON: Manufacturer = Manufacturer(
    name="vladof_hws",
    non_uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_01_Common.Balance_HW_VLA_01_Common',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_02_UnCommon.Balance_HW_VLA_02_UnCommon',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_03_Rare.Balance_HW_VLA_03_Rare',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_04_VeryRare.Balance_HW_VLA_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/VLA/Balance/Balance_HW_VLA_ETech_Rare.Balance_HW_VLA_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/VLA/Balance/Balance_HW_VLA_ETech_VeryRare.Balance_HW_VLA_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst.Balance_HW_VLA_CloudBurst',
        '/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Kickcharger/Balance/Balance_HW_VLA_ETech_Kickcharger.Balance_HW_VLA_ETech_Kickcharger',
        '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Redeye/Balance/Balance_HW_VLA_Redeye.Balance_HW_VLA_Redeye',
    ]
)

shotguns_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/Heavy/ItemPool_Heavy_Common.ItemPool_Heavy_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_Heavy.Att_MinGameStage_Heavy')

def _init_heavyweapons():
    manufacturers = [ATLASHEAVYWEAPON, COVHEAVYWEAPON, TORGUEHEAVYWEAPON, VLADOFHEAVYWEAPON]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,shotguns_common,min_game_stage)


    #for manu in [ATLASHEAVYWEAPON, COVHEAVYWEAPON, TORGUEHEAVYWEAPON, VLADOFHEAVYWEAPON]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")