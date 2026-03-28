from typing import Optional
from poke_worlds.emulation.tracker import MetricGroup
from poke_worlds.emulation.runes_of_virtue.parsers import RunesOfVirtueParser
import numpy as np


class RunesOfVirtueCoreMetrics(MetricGroup):
    """
    Core metrics for Ultima: Runes of Virtue.

    Reports:
    - is_in_menu: Whether the player is currently in a menu.

    Final Reports:
    - None
    """

    NAME = "runes_core"
    REQUIRED_PARSER = RunesOfVirtueParser

    def reset(self, first=False):
        self.is_in_menu = False

    def close(self):
        self.reset()

    def step(self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]):
        self.state_parser: RunesOfVirtueParser
        self.is_in_menu = self.state_parser.is_in_menu(current_frame)

    def report(self) -> dict:
        return {
            "is_in_menu": self.is_in_menu,
        }

    def report_final(self) -> dict:
        return {}
