from django.conf import settings

TURN_REDIS_HOST = getattr(settings, 'TURN_REDIS_HOST', 'localhost')
TURN_REDIS_PORT = getattr(settings, 'TURN_REDIS_PORT', 6379)
TURN_REDIS_DB = getattr(settings, 'TURN_REDIS_DB', 0)
TURN_REDIS_PASSWORD = getattr(settings, 'TURN_REDIS_PASSWORD', None)
TURN_REDIS_UNIX_DOMAIN_SOCKET_PATH = getattr(
    settings, 'TURN_REDIS_UNIX_DOMAIN_SOCKET_PATH', None
)
TURN_REDIS_URL = getattr(settings, 'TURN_REDIS_URL', None)

TURN_CREDENTIAS_TIMEOUT = getattr(settings, 'TURN_CREDENTIAS_TIMEOUT', 300)
TURN_API_URLS = getattr(settings, 'TURN_API_URLS', [])
TURN_SHARED_SECRET = getattr(settings, 'TURN_SHARED_SECRET', 'mySecrete')
