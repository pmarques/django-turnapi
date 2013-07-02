django-turnapi
=======================
TURN API for django

https://code.google.com/p/rfc5766-turn-server/

https://docs.google.com/document/d/1mG7eXFQ5o-ypMWQ1IzdkBQL0UBkLN1xXUJhJcIF5ujQ/edit?disco=AAAAAFxlldA&pli=1#

------------
Installation
------------
python setup.py install

----------
How to USE
----------

1. Configuration::

    TURN_REDIS_HOST = 'localhost'
    TURN_REDIS_PORT = 6379
    TURN_REDIS_DB   = 0 
    TURN_REDIS_PASSWORD = None
    TURN_REDIS_UNIX_DOMAIN_SOCKET_PATH = None
    TURN_REDIS_URL = None

    TURN_CREDENTIAS_TIMEOUT = 300                                                                                                                            
    TURN_API_URLS = []
    TURN_SHARED_SECRET = 'mySecrete'

2. Add turn api to your app settings::

    from turnapi import sites

    url(r'^turn$', include(sites.urls()) ),

-------
License
-------
MIT
