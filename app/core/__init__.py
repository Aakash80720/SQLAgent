# Add the following to expose 'settings' from the 'config' module
from core.config import settings

__all__ = ["config", "session", "settings"]