# ../settings_advert/settings_advert.py

"""Send adverts to players telling them the settings commands."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from core import AutoUnload
from filters.players import PlayerIter
from listeners.tick import Delay
from settings.player import PlayerSettings

# Plugin
from .config import message_frequency
from .messages import ADVERT_MESSAGE, MESSAGE_TOKENS
from .strings import settings_strings

# =============================================================================
# >> PLAYER SETTINGS
# =============================================================================
# Get a PlayerSettings instance
player_settings = PlayerSettings(
    name="Settings Advert",
    prefix="sa",
    text=settings_strings["Menu"],
)

# Add a setting to turn on/off the messages
user_message_setting = player_settings.add_bool_setting(
    name="Messages",
    default=True,
    text=settings_strings["Messages"],
)


# =============================================================================
# >> CLASSES
# =============================================================================
class _SettingsAdvert(AutoUnload):
    """Used to send messages to players a specific intervals."""

    def __init__(self):
        """Initialize the repeating delay."""
        self._delay = Delay(0, self.start_delay)

    def send_adverts(self):
        """Send all players advert messages."""
        for player in PlayerIter("human"):
            self.send_advert_to_player(player.index)

        self.start_delay()

    def start_delay(self):
        """Start the next delay in the loop to send messages."""
        self._delay = Delay(
            message_frequency.get_int() * 60, self.send_adverts,
        )

    @staticmethod
    def send_advert_to_player(index):
        """Send the adverts to the given player."""
        if user_message_setting.get_setting(index):
            ADVERT_MESSAGE.send(index, **MESSAGE_TOKENS)

    def _unload_instance(self):
        """Cancel the current delay on script unload."""
        self._delay.cancel()


settings_advert = _SettingsAdvert()
