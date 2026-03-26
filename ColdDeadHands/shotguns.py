from unrealsdk import find_object
from unrealsdk.unreal import UObject

from .common import _create_manufacturer_pool, Manufacturer


HYPERIONSHOTGUN: Manufacturer = Manufacturer(
    name="hyperion_shotguns",
    non_uniques=[
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_01_Common.Balance_SG_HYP_01_Common',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_02_UnCommon.Balance_SG_HYP_02_UnCommon',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_03_Rare.Balance_SG_HYP_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_04_VeryRare.Balance_SG_HYP_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Hyperion/Balance/Balance_SG_HYP_ETech_Rare.Balance_SG_HYP_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Hyperion/Balance/Balance_SG_HYP_ETech_VeryRare.Balance_SG_HYP_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick.Balance_SG_HYP_Brick',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall.Balance_SG_HYP_ConferenceCall',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert.Balance_SG_HYP_Phebert',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor.Balance_SG_HYP_Redistributor',
        '/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher.Balance_SG_HYP_TheButcher',
        '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux.Balance_SG_HYP_Reflux',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence_Epic.Balance_SG_HYP_Convergence_Epic',
        '/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger.Balance_SG_HYP_ETech_Fearmonger',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer.Balance_SG_HYP_MeltFacer',
        '/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand',
        '/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger.Balance_SG_HYP_IceBurger',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker.Balance_SG_HYP_Firecracker',
        '/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Guardian/Balance/Balance_SG_HYP_Guardian.Balance_SG_HYP_Guardian',
    ],
)

MALIWANSHOTGUN: Manufacturer = Manufacturer(
    name="maliwan_shotguns",
    non_uniques=[
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_01_Common.Balance_SG_MAL_01_Common',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_02_UnCommon.Balance_SG_MAL_02_UnCommon',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_03_Rare.Balance_SG_MAL_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare.Balance_SG_MAL_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_Rare.Balance_SG_MAL_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_VeryRare.Balance_SG_MAL_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev',
        '/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp',
        '/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit.Balance_SG_MAL_BlindBandit',
        '/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit_Epic.Balance_SG_MAL_BlindBandit_Epic',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler.Balance_SG_MAL_ETech_Antler',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency.Balance_SG_MAL_Frequency',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing',
    ],
)

TORGUESHOTGUN: Manufacturer = Manufacturer(
    name="torgue_shotguns",
    non_uniques=[
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_01_Common.Balance_SG_Torgue_01_Common',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_02_UnCommon.Balance_SG_Torgue_02_UnCommon',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_03_Rare.Balance_SG_Torgue_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_04_VeryRare.Balance_SG_Torgue_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_Rare.Balance_SG_Torgue_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare.Balance_SG_Torgue_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog.Balance_SG_Torgue_Balrog',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha.Balance_SG_TOR_Brewha',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker.Balance_SG_Torgue_Flakker',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine.Balance_SG_Torgue_RedLine',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring.Balance_SG_TOR_Boring',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob',
        '/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper.Balance_SG_Torgue_Thumper',
        '/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Shoveler/Balance/Balance_SG_Torgue_Shoveler.Balance_SG_Torgue_Shoveler',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker.Balance_SG_Torgue_ETech_Shocker',
        '/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/CriticalThug/Balance/Balance_SG_Torgue_CriticalThug.Balance_SG_Torgue_CriticalThug',
    ],
)

JAKOBSSHOTGUN: Manufacturer = Manufacturer(
    name="jakobs_shotguns",
    non_uniques=[
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_01_Common.Balance_SG_JAK_01_Common',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_02_UnCommon.Balance_SG_JAK_02_UnCommon',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_03_Rare.Balance_SG_JAK_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_04_VeryRare.Balance_SG_JAK_04_VeryRare',
    ],
    uniques=[
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter.Balance_SG_JAK_Fingerbiter',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia.Balance_SG_JAK_Garcia',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker.Balance_SG_JAK_Hellwalker',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble.Balance_SG_JAK_Nimble',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch.Balance_SG_JAK_OnePunch',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge.Balance_SG_JAK_LGD_Sledge',
        '/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota.Balance_SG_JAK_Dakota',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs.Balance_SG_JAK_Fakobs',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/SpeakEasy/Balance/Balance_SG_JAK_SpeakEasy.Balance_SG_JAK_SpeakEasy',
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Splinter/Balance/Balance_SG_JAK_Splinter.Balance_SG_JAK_Splinter',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure.Balance_SG_JAK_TheCure',
    ],
)

TEDIORESHOTGUN: Manufacturer = Manufacturer(
    name="tediore_shotguns",
    non_uniques=[
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_01_Common.Balance_SG_TED_01_Common',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_02_UnCommon.Balance_SG_TED_02_UnCommon',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_03_Rare.Balance_SG_TED_03_Rare',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_04_VeryRare.Balance_SG_TED_04_VeryRare',
    ],
    etech='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Tediore/Balance/Balance_SG_TED_ETech_Rare.Balance_SG_TED_ETech_Rare',
    etech_rare='/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Tediore/Balance/Balance_SG_TED_ETech_VeryRare.Balance_SG_TED_ETech_VeryRare',
    uniques=[
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon.Balance_SG_TED_Horizon',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius.Balance_SG_TED_Polybius',
        '/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge',
        '/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/TwitchPrime/Balance/Balance_SG_TED_Twitch.Balance_SG_TED_Twitch',
    ],
    dlc_uniques=[
        '/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Brightside/Balance/Balance_SG_TED_Brightside.Balance_SG_TED_Brightside',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy.Balance_SG_TED_Anarchy',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen',
        '/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb.Balance_SG_TED_SacrificialLamb',
    ],
)

shotguns_common:UObject = find_object('ItemPoolData','/Game/GameData/Loot/ItemPools/Guns/Shotguns/ItemPool_Shotguns_Common.ItemPool_Shotguns_Common')
min_game_stage:UObject = find_object('GbxAttributeData','/Game/GameData/Loot/LootSchedule/Attributes/Weapon/Att_MinGameStage_Shotgun.Att_MinGameStage_Shotgun')

def _init_shotguns():
    manufacturers = [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]
    for manufacturer in manufacturers:
        _create_manufacturer_pool(manufacturer,shotguns_common,min_game_stage)


    #for manu in [HYPERIONSHOTGUN, MALIWANSHOTGUN, TORGUESHOTGUN, JAKOBSSHOTGUN, TEDIORESHOTGUN]:
    #    print(f"#{manu.name}")
    #    baldefs = manu.non_uniques + manu.uniques + manu.dlc_uniques
    #    if manu.etech:
    #        baldefs.append(manu.etech)
    #    if manu.etech_rare:
    #        baldefs.append(manu.etech_rare)
    #    for baldef in baldefs:
    #        print(f"'{baldef}',")