from mods_base import get_pc, keybind, build_mod
from unrealsdk import find_class 
from unrealsdk.unreal import IGNORE_STRUCT

gameplay_statics = find_class("GameplayStatics").ClassDefaultObject

@keybind("Spawn Vehicle")
def spawn_vehicle() -> None:
    if not get_pc().Pawn or not get_pc().Pawn.PlayerBalanceState:
        return

    ride = gameplay_statics.SpawnObject(find_class("CatchARide"), get_pc())
    platform = gameplay_statics.SpawnObject(find_class("CatchARidePlatform"), get_pc())
    ride.CatchARide_Platform1 = platform

    player_loc = get_pc().Pawn.K2_GetActorLocation()
    player_rot = get_pc().Pawn.K2_GetActorRotation()

    veh_index = get_pc().CurrentSavegame.VehicleLastLoadoutIndex
    car = get_pc().VehicleSpawnerComponent.VehicleLoadouts[veh_index]

    if "revolver" in str(car.body).lower():
        platform.PlatformSafeZone.K2_SetRelativeLocationAndRotation(player_loc, player_rot, False, IGNORE_STRUCT, True)
        platform.PlatformSmallVehicleSafeZone1.K2_SetRelativeLocationAndRotation(player_loc, player_rot, False, IGNORE_STRUCT, True)
        platform.SmallVehicleSpawnSocket1.K2_SetRelativeLocationAndRotation(player_loc, player_rot, False, IGNORE_STRUCT, True)
    else:
        platform.K2_SetActorLocationAndRotation(player_loc, player_rot, False, IGNORE_STRUCT, True)

    get_pc().SpawnVehicleFromConfig(get_pc().Pawn.PlayerBalanceState.GetExperienceLevel(),car,ride)
    
build_mod()