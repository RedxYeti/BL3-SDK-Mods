from unrealsdk import find_object,construct_object
from unrealsdk.unreal import UObject
from mods_base import ObjectFlags

from .common import make_new_pool_entry

from .pistols import JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL
from .submachineguns import DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG
from .assaultrifles import VLADOFAR, ATLASAR, COVAR, DAHLAR, JAKOBSAR, TORGUEAR
from .shotguns import HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN
from .snipers import MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER
from .heavyweapons import ATLASHEAVYWEAPON, COVHEAVYWEAPON, TORGUEHEAVYWEAPON, VLADOFHEAVYWEAPON

Pool_Weapons_All:UObject = find_object('ItemPoolData','/Game/GameData/Loot/Weapons/Pool_Weapons_All.Pool_Weapons_All')
min_gamestage_pistol:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_Pistol.Att_MinGameStage_Pistol')

class EnemyPool:
    registry: dict[str, "EnemyPool"] = {}

    @classmethod
    def register(cls):
        cls.class_pool = construct_object("ItemPoolData", Pool_Weapons_All, cls.__name__, flags=ObjectFlags.KEEP_ALIVE)
        
        if getattr(cls, "is_unique", False):
            cls.class_pool.append(make_new_pool_entry("bal_def", getattr(cls, "unique_pool"), weighting=None))
            
        else:
            cls.class_pool.MinGameStageRequirement = getattr(cls, "min_gamestage", None)
            for manufacturer in getattr(cls, "pool_weapons"):
                cls.class_pool.BalancedItems.append(make_new_pool_entry("pool", weighting=None, pool_to_add=manufacturer.pool))

        EnemyPool.registry[getattr(cls, "base_pool")] = cls()

    @classmethod
    def get_pool(cls, base_pool_path: str):
        return cls.registry[base_pool_path].class_pool


class ItemPool_Trooper_PS(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_PS.ItemPool_Trooper_PS'
    pool_weapons = [JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]
    min_gamestage = min_gamestage_pistol
    

class ItemPool_TrooperBadass(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBadass.ItemPool_TrooperBadass'
    pool_weapons = [JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]
    min_gamestage = min_gamestage_pistol


class ItemPool_CoVEnemyUse_Pistols(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Pistols.ItemPool_CoVEnemyUse_Pistols'
    pool_weapons = [JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL]
    min_gamestage = min_gamestage_pistol


class ItemPool_TrooperBasic_SM(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_TrooperBasic_SM.ItemPool_TrooperBasic_SM'
    pool_weapons = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG, JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL]


class ItemPool_Trooper_SM(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SM.ItemPool_Trooper_SM'
    pool_weapons = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG, DAHLPISTOL]


class ItemPool_CoVEnemyUse_SMGs(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_SMGs.ItemPool_CoVEnemyUse_SMGs'
    pool_weapons = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG, DAHLPISTOL]


class ItemPool_MAL_SM_NoBeams(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_MAL_SM_NoBeams.ItemPool_MAL_SM_NoBeams'
    pool_weapons = [MALIWANSMG]


class ItemPool_CoVEnemyUse_AssaultRifles(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_AssaultRifles.ItemPool_CoVEnemyUse_AssaultRifles'
    pool_weapons = [VLADOFAR, ATLASAR, COVAR, DAHLAR, JAKOBSAR, TORGUEAR, DAHLSMG, DAHLPISTOL]


class ItemPool_TinkAnointed_AssaultRifles(EnemyPool):
    base_pool = '/Game/Enemies/Tink/Anointed/_Design/ItemPool/ItemPool_TinkAnointed_AssaultRifles.ItemPool_TinkAnointed_AssaultRifles'
    pool_weapons = [DAHLAR]


class ItemPool_TinkUse_Shotguns(EnemyPool):
    base_pool = '/Game/Enemies/Tink/Shotgun/_Design/ItemPools/ItemPool_TinkUse_Shotguns.ItemPool_TinkUse_Shotguns'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPool_CoVEnforcers_Shotguns(EnemyPool):
    base_pool = '/Game/Enemies/Enforcer/_Shared/_Design/Weapon/ItemPool_CoVEnforcers_Shotguns.ItemPool_CoVEnforcers_Shotguns'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPool_CoVEnemyUse_Shotguns(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_Shotguns.ItemPool_CoVEnemyUse_Shotguns'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPool_EnforcerGun_Shotguns(EnemyPool):
    base_pool = '/Game/Enemies/Enforcer/Gun/_Design/Character/ItemPool_EnforcerGun_Shotguns.ItemPool_EnforcerGun_Shotguns'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPool_Trooper_SG(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SG.ItemPool_Trooper_SG'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN, JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]


class ItemPool_Trooper_SR(EnemyPool):
    base_pool = '/Game/Enemies/Trooper/_Shared/_Design/ItemPools/ItemPool_Trooper_SR.ItemPool_Trooper_SR'
    pool_weapons = [MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER, JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL, ATLASPISTOL]


class ItemPool_CoVEnemyUse_SniperRifles(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_CoVEnemyUse_SniperRifles.ItemPool_CoVEnemyUse_SniperRifles'
    pool_weapons = [MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER]


class ItemPool_BadassPunk_HeavyWeapons(EnemyPool):
    base_pool = '/Game/Enemies/Punk_Female/Badass/_Design/Weapon/ItemPools/ItemPool_BadassPunk_HeavyWeapons.ItemPool_BadassPunk_HeavyWeapons'
    pool_weapons = [TORGUEHEAVYWEAPON, VLADOFHEAVYWEAPON, DAHLPISTOL]


class ItemPool_Guns_PunkFemaleBasic(EnemyPool):
    base_pool = '/Game/GameData/Loot/Weapons/Pool_Weapons_All.Pool_Weapons_All:ItemPoolList_Guns_PunkFemaleBasic'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPool_COVEnemyUse_HeavyWeapons(EnemyPool):
    base_pool = '/Game/Enemies/_Shared/_Design/ItemPools/ItemPool_COVEnemyUse_HeavyWeapons.ItemPool_COVEnemyUse_HeavyWeapons'
    pool_weapons = [COVHEAVYWEAPON]


class ItemPoolList_Guns_Punk_Shotguns(EnemyPool):
    base_pool = '/Game/Enemies/Punk_Female/_Shared/_Design/ItemPoolLists/ItemPoolList_Guns_Punk_Shotguns.ItemPoolList_Guns_Punk_Shotguns'
    pool_weapons = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]


class ItemPoolList_Guns_PunkFemaleBasic(EnemyPool):
    base_pool = '/Game/Enemies/Punk_Female/_Shared/_Design/ItemPoolLists/ItemPoolList_Guns_PunkFemaleBasic.ItemPoolList_Guns_PunkFemaleBasic'
    pool_weapons = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG, DAHLPISTOL, JAKOBSPISTOL, DAHLPISTOL, TEDIOREPISTOL, VLADOFPISTOL, MALIWANPISTOL, COVPISTOL, TORGUEPISTOL]


class ItemPoolList_Guns_Punk_AssaultRifles(EnemyPool):
    base_pool = '/Game/Enemies/Punk_Female/_Shared/_Design/ItemPoolLists/ItemPoolList_Guns_Punk_AssaultRifles.ItemPoolList_Guns_Punk_AssaultRifles'
    pool_weapons = [VLADOFAR, ATLASAR, COVAR, DAHLAR, JAKOBSAR, TORGUEAR, DAHLSMG, DAHLPISTOL]


class ItemPool_CrimsonAlliance_SMGs(EnemyPool):
    base_pool = '/Game/NonPlayerCharacters/CrimsonAlliance/_Design/ItemPoolLists/ItemPool_CrimsonAlliance_SMGs.ItemPool_CrimsonAlliance_SMGs'
    pool_weapons = [DAHLSMG, HYPERIONSMG, TEDIORESMG, MALIWANSMG, DAHLPISTOL]


class ItemPoolList_Guns_Punk_Snipers(EnemyPool):
    base_pool = '/Game/Enemies/Punk_Female/_Shared/_Design/ItemPoolLists/ItemPoolList_Guns_Punk_Snipers.ItemPoolList_Guns_Punk_Snipers'
    pool_weapons = [MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER]

class ItemPool_FrontStriker_SMG(EnemyPool):
    base_pool = '/Game/Enemies/Frontrunner/Striker/_Design/ItemPools/ItemPool_FrontStriker_SMG.ItemPool_FrontStriker_SMG'
    pool_weapons = [MALIWANSMG]

