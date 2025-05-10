# ../settings_advert/strings.py

"""Translations functionality for the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from translations.strings import LangStrings

# Plugin
from .info import info

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "config_strings",
    "settings_strings",
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
config_strings = LangStrings(info.name + "/config_strings")
settings_strings = LangStrings(info.name + "/strings")
