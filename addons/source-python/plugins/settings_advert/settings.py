# ../settings_advert/settings_advert.py

"""Send adverts to players telling them the settings commands."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from settings.player import PlayerSettings

# Plugin
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
