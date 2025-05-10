# ../settings_advert/config.py

"""Configuration functionality for the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from config.manager import ConfigManager

# Plugin
from .info import info
from .strings import config_strings

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "message_frequency",
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with ConfigManager(info.name, "settings_advert_") as _config:
    message_frequency = _config.cvar(
        name="frequency",
        default=3,
        description=config_strings["Frequency"],
    )
