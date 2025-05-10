# ../settings_advert/messages.py

"""Message functionality for the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Site-Package
from configobj import ConfigObj

# Source.Python
from messages import SayText2
from paths import CFG_PATH

# Plugin
from .strings import settings_strings

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "ADVERT_MESSAGE",
    "MESSAGE_TOKENS",
)


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_user_settings = ConfigObj(CFG_PATH / "core_settings.ini")["USER_SETTINGS"]

MESSAGE_TOKENS = {
    "say": ", ".join(
        map(
            str,
            filter(
                None,
                [
                    _user_settings["public_say_commands"],
                    _user_settings["private_say_commands"],
                ],
            ),
        ),
    ),
    "client": _user_settings["client_commands"],
}
if not list(filter(None, MESSAGE_TOKENS.values())):
    msg = "No settings commands set in core_settings.ini"
    raise ValueError(msg)

_key = (
    "Say" if not MESSAGE_TOKENS["client"]
    else "Client" if not MESSAGE_TOKENS["say"]
    else "Both"
)
ADVERT_MESSAGE = SayText2(settings_strings[f"Commands:{_key}"])
