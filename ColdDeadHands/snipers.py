from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import _create_manufacturer_pool, Manufacturer


MALIWANSNIPER: Manufacturer = Manufacturer(
    name="maliwan_snipers",
    non_uniques=[
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_01_Common.Balance_MAL_SR_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_02_UnCommon.Balance_MAL_SR_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_03_Rare.Balance_MAL_SR_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare.Balance_MAL_SR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_Rare.Balance_SR_MAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_VeryRare.Balance_SR_MAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki',
        '/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber.Balance_MAL_SR_ImaginaryNumber',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Balance/Balance_MAL_SR_BinaryOperator.Balance_MAL_SR_BinaryOperator',
    ],
)

DAHLSNIPER: Manufacturer = Manufacturer(
    name="dahl_snipers",
    non_uniques=[
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_01_Common.Balance_SR_DAL_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_02_UnCommon.Balance_SR_DAL_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_03_Rare.Balance_SR_DAL_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_04_VeryRare.Balance_SR_DAL_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Dahl/Balance/Balance_SR_DAL_ETech_Rare.Balance_SR_DAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Dahl/Balance/Balance_SR_DAL_ETech_VeryRare.Balance_SR_DAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication.Balance_SR_DAL_BrashisDedication',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane.Balance_SR_DAL_ETech_MalaksBane',
        '/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer.Balance_SR_DAL_WorldDestroyer',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk.Balance_SR_DAL_SandHawk',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime',
    ],
)

HYPERIONSNIPER: Manufacturer = Manufacturer(
    name="hyperion_snipers",
    non_uniques=[
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_01_Common.Balance_SR_HYP_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_02_UnCommon.Balance_SR_HYP_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_03_Rare.Balance_SR_HYP_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_04_VeryRare.Balance_SR_HYP_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Hyperion/Balance/Balance_SR_HYP_ETech_Rare.Balance_SR_HYP_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Hyperion/Balance/Balance_SR_HYP_ETech_VeryRare.Balance_SR_HYP_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork.Balance_SR_HYP_Masterwork',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime.Balance_SR_HYP_TwoTime',
        '/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks.Balance_SR_HYP_Woodblocks',
        '/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer.Balance_SR_HYP_ZeroForPlayer',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Narp/Balance/Balance_SR_HYP_Narp.Balance_SR_HYP_Narp',
    ],
)

JAKOBSSNIPER: Manufacturer = Manufacturer(
    name="jakobs_snipers",
    non_uniques=[
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_01_Common.Balance_SR_JAK_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_02_UnCommon.Balance_SR_JAK_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_03_Rare.Balance_SR_JAK_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_04_VeryRare.Balance_SR_JAK_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion.Balance_SR_JAK_Headsplosion',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen.Balance_SR_JAK_IceQueen',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle.Balance_SR_JAK_Monocle',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter.Balance_SR_JAK_Hunter',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted.Balance_SR_JAK_Hunted',
        '/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress.Balance_SR_JAK_Huntress',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard.Balance_SR_JAK_CockyBastard',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat',
        '/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/BirdofPrey/Balance/Balance_SR_JAK_BirdofPrey.Balance_SR_JAK_BirdofPrey',
        '/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Disruptor/Balance/Balance_SR_JAK_Disruptor.Balance_SR_JAK_Disruptor',
    ],
)
VLADOFSNIPER: Manufacturer = Manufacturer(
    name="vladof_snipers",
    non_uniques=[
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_01_Common.Balance_VLA_SR_01_Common',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_02_UnCommon.Balance_VLA_SR_02_UnCommon',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_03_Rare.Balance_VLA_SR_03_Rare',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_04_VeryRare.Balance_VLA_SR_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Vladof/Balance/Balance_SR_VLA_ETech_Rare.Balance_SR_VLA_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Vladof/Balance/Balance_SR_VLA_ETech_VeryRare.Balance_SR_VLA_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda.Balance_VLA_SR_Lyuda',
        '/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison.Balance_VLA_SR_Prison',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator.Balance_VLA_SR_Septimator',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator_Epic.Balance_VLA_SR_Septimator_Epic',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Boogeyman/Balance/Balance_VLA_SR_Boogeyman.Balance_VLA_SR_Boogeyman',
    ],
)

snipers_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/SniperRifles/ItemPool_SniperRifles_Common.ItemPool_SniperRifles_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_SniperRifle.Att_MinGameStage_SniperRifle')

def _init_snipers():
    manufacturers = [MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,snipers_common,min_game_stage)

    #for manu in [MALIWANSNIPER, DAHLSNIPER, HYPERIONSNIPER, JAKOBSSNIPER, VLADOFSNIPER]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")
