from poke_worlds.utils import verify_parameters, log_error
from poke_worlds.emulation.parser import StateParser


class RunesOfVirtueParser(StateParser):
    """
    Minimal parser scaffold for Ultima: Runes of Virtue.
    """

    VARIANT = "runes_of_virtue"

    def __init__(self, pyboy, parameters):
        verify_parameters(parameters)
        if f"{self.VARIANT}_rom_data_path" not in parameters:
            log_error(
                f"ROM data path not found for variant: {self.VARIANT}. Add {self.VARIANT}_rom_data_path to config files.",
                parameters,
            )
        self.rom_data_path = parameters[f"{self.VARIANT}_rom_data_path"]
        super().__init__(pyboy, parameters)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(variant={self.VARIANT})"
