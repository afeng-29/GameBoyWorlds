from poke_worlds.utils import verify_parameters, log_error
from poke_worlds.emulation.parser import StateParser, NamedScreenRegion
import os
import numpy as np


class RunesOfVirtueParser(StateParser):
    """
    State parser for Ultima: Runes of Virtue.

    Defines a named screen region 'menu_indicator' that captures a strip
    at the bottom of the screen which changes visually when any menu is open.

    After running dev_play, use:
        c menu_indicator
    while a menu is open to save the reference image.
    """

    VARIANT = "runes_of_virtue"

    # Bottom strip of the screen (y=136, height=8, full width=160).
    # This region changes appearance when a menu is active.
    # Adjust these coordinates after inspecting the screen with 'd None' in dev_play.
    REGIONS = [
        ("menu_indicator", 0, 136, 160, 8),
    ]

    def __init__(self, pyboy, parameters):
        verify_parameters(parameters)
        if f"{self.VARIANT}_rom_data_path" not in parameters:
            log_error(
                f"ROM data path not found for variant: {self.VARIANT}. Add {self.VARIANT}_rom_data_path to config files.",
                parameters,
            )
        self.rom_data_path = parameters[f"{self.VARIANT}_rom_data_path"]
        captures_dir = os.path.join(self.rom_data_path, "captures")
        regions = []
        for name, x, y, w, h in self.REGIONS:
            target_path = os.path.join(captures_dir, f"{name}.npy")
            regions.append(NamedScreenRegion(
                name=name,
                start_x=x,
                start_y=y,
                width=w,
                height=h,
                parameters=parameters,
                target_path=target_path,
            ))
        super().__init__(pyboy, parameters, named_screen_regions=regions)

    def is_in_menu(self, current_screen: np.ndarray) -> bool:
        """Returns True if the menu_indicator region matches its captured reference."""
        return self.named_region_matches_target(current_screen, "menu_indicator")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(variant={self.VARIANT})"
