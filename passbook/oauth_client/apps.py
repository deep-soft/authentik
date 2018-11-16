"""passbook oauth_client config"""
from importlib import import_module
from logging import getLogger

from django.apps import AppConfig

from passbook.lib.config import CONFIG

LOGGER = getLogger(__name__)

class PassbookOAuthClientConfig(AppConfig):
    """passbook oauth_client config"""

    name = 'passbook.oauth_client'
    label = 'passbook_oauth_client'
    verbose_name = 'passbook OAuth Client'

    def ready(self):
        """Load source_types from config file"""
        source_types_to_load = CONFIG.y('oauth_client.source_tyoes')
        for source_type in source_types_to_load:
            try:
                import_module(source_type)
                LOGGER.info("Loaded %s", source_type)
            except ImportError as exc:
                LOGGER.debug(exc)
