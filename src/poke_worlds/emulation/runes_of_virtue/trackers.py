from poke_worlds.emulation.tracker import StateTracker
from poke_worlds.emulation.runes_of_virtue.base_metrics import RunesOfVirtueCoreMetrics


class RunesOfVirtueTracker(StateTracker):
    """
    StateTracker for Ultima: Runes of Virtue.
    Reports whether the player is currently in a menu.
    """

    def start(self):
        super().start()
        self.metric_classes.extend([RunesOfVirtueCoreMetrics])
