from typing import Type, Dict
from poke_worlds.emulation.parser import StateParser
from poke_worlds.emulation.tracker import StateTracker
from poke_worlds.emulation.emulator import Emulator
from poke_worlds.emulation.runes_of_virtue.parsers import RunesOfVirtueParser

GAME_TO_GB_NAME = {
    "runes_of_virtue": "RunesOfVirtue.gb",
}
""" Expected save name for each game. Save the file to <storage_dir_from_config_file>/<game_name>_rom_data/<gb_name>"""

STRONGEST_PARSERS: Dict[str, Type[StateParser]] = {
    "runes_of_virtue": RunesOfVirtueParser,
}

AVAILABLE_STATE_TRACKERS: Dict[str, Dict[str, Type[StateTracker]]] = {
    "runes_of_virtue": {"default": StateTracker},
}

AVAILABLE_EMULATORS: Dict[str, Dict[str, Type[Emulator]]] = {
    "runes_of_virtue": {"default": Emulator},
}
