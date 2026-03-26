from mods_base import ObjectFlags
from unrealsdk import make_struct,find_object, construct_object
from unrealsdk.unreal import UObject, WrappedStruct

from dataclasses import dataclass, field

from .options import oidDLCItems

all_uniques = []

Att_RarityWeight_01_Common:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_01_Common.Att_RarityWeight_01_Common')
Att_RarityWeight_02_Uncommon:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_02_Uncommon.Att_RarityWeight_02_Uncommon')
Att_RarityWeight_03_Rare:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_03_Rare.Att_RarityWeight_03_Rare')
Att_RarityWeight_04_VeryRare:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_04_VeryRare.Att_RarityWeight_04_VeryRare')
Att_RarityWeight_05_Legendary:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/RarityWeighting/Att_RarityWeight_05_Legendary.Att_RarityWeight_05_Legendary')

CDHCOMMONWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_01_Common, "common_weight", ObjectFlags.KEEP_ALIVE)
CDHUNCOMMONWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_02_Uncommon, "uncommon_weight", ObjectFlags.KEEP_ALIVE)
CDHRAREWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_03_Rare, "rare_weight", ObjectFlags.KEEP_ALIVE)
CDHETECHRAREWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_03_Rare, "etech_rare_weight", ObjectFlags.KEEP_ALIVE)
CDHVERYRAREWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_04_VeryRare, "veryrare_weight", ObjectFlags.KEEP_ALIVE)
CDHETECHVERYRAREWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_04_VeryRare, "etech_veryrare_weight", ObjectFlags.KEEP_ALIVE)
CDHLEGENDARYWEIGHT:UObject = construct_object('GbxAttributeData', Att_RarityWeight_05_Legendary, "legendary_weight", ObjectFlags.KEEP_ALIVE)

CDHCOMMONRESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_01_Common, "common_resolver", ObjectFlags.KEEP_ALIVE)
CDHUNCOMMONRESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_02_Uncommon, "uncommon_resolver", ObjectFlags.KEEP_ALIVE)
CDHRARERESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_03_Rare, "rare_resolver", ObjectFlags.KEEP_ALIVE)
CDHETECHRARERESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_03_Rare, "etech_rare_resolver", ObjectFlags.KEEP_ALIVE)
CDHVERYRARERESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_04_VeryRare, "veryrare_resolver", ObjectFlags.KEEP_ALIVE)
CDHETECHVERYRARERESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_04_VeryRare, "etech_veryrare_resolver", ObjectFlags.KEEP_ALIVE)
CDHLEGENDARYRESOLVER:UObject = construct_object('SimpleMathValueResolver', Att_RarityWeight_05_Legendary, "legendary_resolver", ObjectFlags.KEEP_ALIVE)

CDHCOMMONWEIGHT.ValueResolver = CDHCOMMONRESOLVER
CDHUNCOMMONWEIGHT.ValueResolver = CDHUNCOMMONRESOLVER
CDHRAREWEIGHT.ValueResolver = CDHRARERESOLVER
CDHETECHRAREWEIGHT.ValueResolver = CDHETECHRARERESOLVER
CDHVERYRAREWEIGHT.ValueResolver = CDHVERYRARERESOLVER
CDHETECHVERYRAREWEIGHT.ValueResolver = CDHETECHVERYRARERESOLVER
CDHLEGENDARYWEIGHT.ValueResolver = CDHLEGENDARYRESOLVER

RARITYRESOLVERS:list[UObject] = [
    CDHCOMMONRESOLVER,
    CDHUNCOMMONRESOLVER,
    CDHRARERESOLVER,
    CDHVERYRARERESOLVER,
    CDHLEGENDARYRESOLVER,
]

RARITYWEIGHTS:dict[int,list[float]] = {
    9:  [1.00, 0.85, 0.00, 0.00, 0.00], #0-9
    19: [1.00, 1.00, 0.10, 0.00, 0.00], #10-19
    29: [1.00, 1.00, 0.40, 0.05, 0.00], #20-29
    39: [1.00, 1.00, 1.00, 0.30, 0.01], #30-39
    49: [1.00, 1.00, 1.00, 0.65, 0.015], #40-49
    59: [0.85, 1.00, 1.00, 1.00, 0.05], #50-59
    69: [0.50, 0.90, 1.00, 1.00, 0.05], #60-69
    70: [0.15, 0.85, 1.00, 1.00, 0.055], #70+
}

CDHETECHRARERESOLVER.ValueA.BaseValueConstant = 0
CDHETECHRARERESOLVER.ValueA.BaseValueScale = 0
CDHETECHVERYRARERESOLVER.ValueA.BaseValueConstant = 0 
CDHETECHVERYRARERESOLVER.ValueA.BaseValueScale = 0 

for resolver in RARITYRESOLVERS:
    resolver.Operator = 0
    resolver.ValueB.BaseValueConstant = 0
    resolver.ValueB.BaseValueScale = 0

CDHETECHRARERESOLVER.ValueB.BaseValueConstant = 0
CDHETECHRARERESOLVER.ValueB.BaseValueScale = 0
CDHETECHVERYRARERESOLVER.ValueB.BaseValueConstant = 0 
CDHETECHVERYRARERESOLVER.ValueB.BaseValueScale = 0 


MAIN_RARITIES:list[UObject] = [
    CDHCOMMONWEIGHT,
    CDHUNCOMMONWEIGHT,
    CDHRAREWEIGHT,
    CDHVERYRAREWEIGHT,
]

@dataclass
class Manufacturer:
    name: str = ""
    pool: UObject | None = None
    non_uniques: list[str] = field(default_factory=list)
    etech: str = ""
    etech_rare: str = ""
    uniques: list[str] = field(default_factory=list)
    dlc_uniques: list[str] = field(default_factory=list)


etech_requirement:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_ETech.Att_MinGameStage_ETech')

def make_new_pool_entry(type:str, type_to_add:str = "", weighting:UObject | None = None, pool_to_add = None) -> WrappedStruct | None:
    balance_data = None
    if type == "bal_def":
        try:
            balance_data = find_object('InventoryBalanceData', type_to_add)
        except:
            return None
    

    new_pool_entry = make_struct("BalancedInventoryInfo")
    new_pool_entry.ItemPoolData = pool_to_add if pool_to_add else None
    new_pool_entry.InventoryBalanceData = balance_data
    new_pool_entry.ResolvedInventoryBalanceData = balance_data
    new_pool_entry.Weight.BaseValueConstant = 1
    new_pool_entry.Weight.BaseValueAttribute = weighting if weighting else None
    new_pool_entry.Weight.BaseValueScale = 1

    return new_pool_entry

def _create_manufacturer_pool(in_manufacturer:Manufacturer, construct_base_object:UObject, min_game_stage:UObject) -> None:
    main_pool = construct_object("ItemPoolData", construct_base_object, in_manufacturer.name, flags=ObjectFlags.KEEP_ALIVE)
    for index, balance in enumerate(in_manufacturer.non_uniques):
        main_pool.BalancedItems.append(make_new_pool_entry("bal_def", balance, MAIN_RARITIES[index]))

    if in_manufacturer.etech:
        etech_pool = construct_object("ItemPoolData", construct_base_object, f"{in_manufacturer.name}.etech", flags=ObjectFlags.KEEP_ALIVE)
        etech_pool.MinGameStageRequirement = etech_requirement
        all_etech = [in_manufacturer.etech, in_manufacturer.etech_rare]
        for balance in all_etech:
            weight = CDHETECHRAREWEIGHT if balance in in_manufacturer.etech else CDHETECHVERYRAREWEIGHT
            etech_pool.BalancedItems.append(make_new_pool_entry("bal_def", balance, weighting=weight))
        main_pool.BalancedItems.append(make_new_pool_entry("pool", weighting=None, pool_to_add=etech_pool))

    if in_manufacturer.uniques:
        unique_pool = construct_object("ItemPoolData", construct_base_object, f"{in_manufacturer.name}.unique", flags=ObjectFlags.KEEP_ALIVE)
        for balance in in_manufacturer.uniques:
            all_uniques.append(balance)
            unique_pool.BalancedItems.append(make_new_pool_entry("bal_def", balance, weighting=None))
        main_pool.BalancedItems.append(make_new_pool_entry("pool", weighting=CDHLEGENDARYWEIGHT, pool_to_add=unique_pool))

    if oidDLCItems.value and in_manufacturer.dlc_uniques:
        dlc_unique_pool = construct_object("ItemPoolData", construct_base_object, f"{in_manufacturer.name}.dlc_unique", flags=ObjectFlags.KEEP_ALIVE)
        for balance in in_manufacturer.dlc_uniques:
            all_uniques.append(balance)
            dlc_unique_pool.BalancedItems.append(make_new_pool_entry("bal_def", balance, weighting=None))
        main_pool.BalancedItems.append(make_new_pool_entry("pool", weighting=CDHLEGENDARYWEIGHT, pool_to_add=dlc_unique_pool))

    main_pool.MinGameStageRequirement = min_game_stage
    in_manufacturer.pool = main_pool