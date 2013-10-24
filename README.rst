django-turnapi
=======================
TURN API for django

*TURN Server*

https://code.google.com/p/rfc5766-turn-server/

*TURN Server API Proposal*

http://tools.ietf.org/html/draft-uberti-rtcweb-turn-rest-00

*Old TURN REST API on Google Docs*

https://docs.google.com/document/d/1mG7eXFQ5o-ypMWQ1IzdkBQL0UBkLN1xXUJhJcIF5ujQ

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
    TURN_REALM = "mystite.com"
    TURN_SEPARATOR = ":"
    TURN_AUTH = True

2. Add turn api to your app settings::

    from turnapi import sites

    url(r'^turn$', include(sites.urls()) ),

-------
License
-------
MIT
