from unrealsdk import find_all
from mods_base import build_mod, capture_next_console_line, SETTINGS_DIR, SliderOption
import os

console_history:str = ""

def prep_history() -> None:
    global console_history
    console_history_dir = os.path.join(SETTINGS_DIR, "console_history")

    if not os.path.exists(console_history_dir):
        os.makedirs(console_history_dir)

    console_history = os.path.join(console_history_dir, "console_history.txt")

    if not os.path.exists(console_history):
        with open(console_history, "w") as file:
            file.write("")
    else:
        with open(console_history, "r") as file:
            history = [line.strip() for line in file if line.strip()]
    
        find_all("Console")[-1].HistoryBuffer = history

    capture_next_console_line(save_command)
    return


def save_command(new_command:str):
    if not new_command:
        return
    
    with open(console_history, "r") as file:
        history = [line.strip() for line in file if line.strip()]

    if new_command in history:
        return

    history.append(new_command.strip())

    history = history[-oidMaxHistory.value:]

    with open(console_history, "w") as file:
        for command in history:
            file.write(command + "\n")
            
    capture_next_console_line(save_command)
    return


oidMaxHistory = SliderOption(
    "Max History Count",
    20,
    1,
    50,
    description="Choose how many commands are saved."
)

build_mod(on_enable=prep_history)