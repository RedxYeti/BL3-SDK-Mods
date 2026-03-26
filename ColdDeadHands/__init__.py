from typing import Any
from mods_base import hook, build_mod, BoolOption,ENGINE,get_pc
from unrealsdk import make_struct,find_class,find_object
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction, notify_changes

from .options import oidDLCItems

from .itempools import EnemyPool
from .common import all_uniques
from .common import RARITYWEIGHTS, RARITYRESOLVERS, CDHETECHRARERESOLVER, CDHETECHVERYRARERESOLVER, CDHCOMMONRESOLVER, CDHUNCOMMONRESOLVER, CDHRARERESOLVER, CDHETECHRARERESOLVER, CDHVERYRARERESOLVER, CDHETECHVERYRARERESOLVER, CDHLEGENDARYRESOLVER
from .pistols import _init_pistols
from .submachineguns import _init_smgs
from .assaultrifles import _init_ars
from .shotguns import _init_shotguns
from .snipers import _init_snipers
from .heavyweapons import _init_heavyweapons
from .legitbaldefs import pistol_bal_defs, smg_bal_defs, ar_bal_defs, shotgun_bal_defs, sniper_bal_defs, heavyweapon_bal_defs

all_bal = pistol_bal_defs + smg_bal_defs + ar_bal_defs + shotgun_bal_defs + sniper_bal_defs + heavyweapon_bal_defs
all_bal = {bal.lower() for bal in all_bal}
all_pools = []


def set_ondeath_pools() -> None:
    try:
        ItemPoolList_StandardEnemyGunsandGear = find_object('ItemPoolListData','/Game/GameData/Loot/ItemPools/ItemPoolList_StandardEnemyGunsandGear.ItemPoolList_StandardEnemyGunsandGear')
        if len(ItemPoolList_StandardEnemyGunsandGear.ItemPools) == 11:
            del ItemPoolList_StandardEnemyGunsandGear.ItemPools[4]
    except:
        pass

def make_new_pool_info(path_name:str) -> WrappedStruct:
    new_pool_info = make_struct("ItemPoolInfo")
    new_pool_info.ItemPool = EnemyPool.get_pool(path_name)
    new_pool_info.PoolProbability.BaseValueConstant = 1
    new_pool_info.PoolProbability.BaseValueScale = 1
    new_pool_info.NumberOfTimesToSelectFromThisPool.BaseValueConstant = 1
    new_pool_info.NumberOfTimesToSelectFromThisPool.BaseValueScale = 1
    return new_pool_info

dropondeath = []
@hook("/Game/Enemies/_Shared/_Design/BPChar_Enemy.BPChar_Enemy_C:UserConstructionScript", Type.PRE)
def OnPossess_CDH(obj: UObject,args: WrappedStruct, ret: Any, func: BoundFunction) -> Any:
    if hasattr(obj, "AIBalanceState") and obj.AIBalanceState:
        #global dropondeath
        #bDeathPool = False
        #for pt in obj.AIBalanceState.Playthroughs:
        #    for pool in pt.DropOnDeathItemPools.ItemPoolLists:
        #        if pool not in dropondeath:
        #            print(pool)
        #            dropondeath.append(pool)
        #            bDeathPool = True   
        #if bDeathPool:
        #    show_hud_message("chd", "death pool", 2)

        with notify_changes():
            for pt in obj.AIBalanceState.Playthroughs:
                single_collection = pt.EquippedItemPoolCollection
                if single_collection:
                    for pool in single_collection.ItemPools:
                        item = pool.ItemPool
                        if item:
                            path = pool.ItemPool._path_name()
                            if path in all_pools:
                                pool.ItemPool = EnemyPool.get_pool(path)


                if pt.EquippedItemPoolCollections:
                    for collection in pt.EquippedItemPoolCollections:
                        for pool in collection.ItemPools:
                            if pool.ItemPool:
                                path = pool.ItemPool._path_name()
                                if path in all_pools:
                                    pool.ItemPool = EnemyPool.get_pool(path)

                        bFoundPool = False
                        for poollist in collection.ItemPoolLists:
                            if poollist and poollist._path_name() in all_pools:
                                bFoundPool = True
                                collection.ItemPools.append(make_new_pool_info(poollist._path_name()))

                        if bFoundPool:
                            collection.ItemPoolLists = []
 


@hook("/Script/OakGame.OakPlayerController:OnLevelChanged", Type.POST)
def ServerAcknowledgePossession_CDH(obj: UObject,args: WrappedStruct, ret: Any, func: BoundFunction) -> Any:
    set_ondeath_pools()
    player_level = obj.PrimaryCharacter.PlayerBalanceComponent.ExperienceLevel
    if player_level >= 70:
        for i in range(5):
            RARITYRESOLVERS[i].ValueA.BaseValueConstant = RARITYWEIGHTS[70][i]
        CDHETECHRARERESOLVER.ValueA.BaseValueConstant = RARITYRESOLVERS[2].ValueA.BaseValueConstant / 3
        CDHETECHVERYRARERESOLVER.ValueA.BaseValueConstant = RARITYRESOLVERS[3].ValueA.BaseValueConstant / 3
        return
    
    for level in RARITYWEIGHTS.keys():
        if player_level <= level:
            for i in range(5):
                RARITYRESOLVERS[i].ValueA.BaseValueConstant = RARITYWEIGHTS[level][i]
            if RARITYRESOLVERS[2].ValueA.BaseValueConstant > 0: 
                CDHETECHRARERESOLVER.ValueA.BaseValueConstant = RARITYRESOLVERS[2].ValueA.BaseValueConstant / 3
                if RARITYRESOLVERS[3].ValueA.BaseValueConstant > 0:
                    CDHETECHVERYRARERESOLVER.ValueA.BaseValueConstant = RARITYRESOLVERS[3].ValueA.BaseValueConstant / 3
            break


def has_legit_bal_def(weapon:UObject) -> bool:
    return weapon.BalanceStateComponent.InventoryBalanceData._path_name().lower() in all_bal

def make_new_bal_state(balance_state:UObject) -> WrappedStruct: 
    return make_struct("InventoryBalanceStateInitializationData",
        GameStage=balance_state.GetGameStage(),
        InventoryData=balance_state.GetInventoryData(),
        InventoryBalanceData=balance_state.GetInventoryBalanceData(),
        ManufacturerData=balance_state.GetManufacturer(),
        PartList=list(balance_state.GetPartList()),
        GenericPartList=list(balance_state.GetGenericPartList()),
        AdditionalData=list(balance_state.AdditionalData),
    )

from ui_utils import show_hud_message #type: ignore
blacklist = [
                "PetLoader",
                "BPChar_GuardianSera_C",
                "BPChar_GuardianWraith_C",
                "Oversphere",
                "Dropship"
             ]

impulse_force = make_struct("Vector",Z=500)
angular_force = make_struct("Vector",Y=500,Z=500)
InventoryBlueprintLibrary = find_class("InventoryBlueprintLibrary").ClassDefaultObject
enemycount = 0
uniquecount = 0
@hook("/Script/OakGame.OakStatusEffectManagerComponent:OnOwnerDied", Type.PRE)
def OnOwnerDied_CDH(obj: UObject,args: WrappedStruct, ret: Any, func: BoundFunction) -> Any:
    pawn = obj.GetOwner()
    if "vehicle" in str(pawn).lower():
        return

    if pawn.IsPlayerControlled() or pawn.PlayerMaster:
        return

    if not hasattr(pawn, "ActiveWeapons") or not hasattr(pawn, "AIBalanceState") or hasattr(pawn, "TEDProjectile_Base"):
        return
    
    global enemycount,uniquecount
    enemycount += 1
    if len(pawn.ActiveWeapons.WeaponSlots) and pawn.ActiveWeapons.WeaponSlots[0].AttachedWeapon:
        if not has_legit_bal_def(pawn.ActiveWeapons.WeaponSlots[0].AttachedWeapon):
            #if [item for item in blacklist if item not in str(pawn)]:
            #    show_hud_message("cdh", "not legit", 3)
            #    print(f"not legit from {pawn.AIBalanceState.Playthroughs[0].EquippedItemPoolCollections} >>> {pawn.ActiveWeapons.WeaponSlots[0].AttachedWeapon.BalanceStateComponent.InventoryBalanceData._path_name()}")
            return
        
        #if pawn.ActiveWeapons.WeaponSlots[0].AttachedWeapon.BalanceStateComponent.InventoryBalanceData._path_name().lower() in all_uniques:
        #    show_hud_message("cdh", "unique", 1)
        #    uniquecount += 1
        #    print(f"unique drop >>> {enemycount}/{uniquecount}")
            

        pawn_loc = pawn.K2_GetActorLocation()
        pawn_loc.Z += 100

        new_bal = make_new_bal_state(pawn.ActiveWeapons.WeaponSlots[0].AttachedWeapon.BalanceStateComponent)

        pickup = InventoryBlueprintLibrary.BuildInventory(ENGINE.GameViewport.World, True, pawn_loc, new_bal)
        if pickup:
            pickup.RootComponent.AddImpulse(impulse_force, "", True)
            pickup.RootComponent.AddAngularImpulseInDegrees(angular_force, "", True)


def enabled() -> None:
    _init_pistols()
    _init_smgs()
    _init_ars()
    _init_shotguns()
    _init_snipers()
    _init_heavyweapons()
    EnemyPool.registry.clear()
    for subclass in EnemyPool.__subclasses__():
        subclass.register()
    global all_pools
    all_pools = {item for item in EnemyPool.registry.keys()}
    global all_uniques
    all_uniques = {item.lower() for item in all_uniques}


build_mod(on_enable=enabled)