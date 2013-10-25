"""api.py: Implemente rfc5766-turn-server HTTP server """

from django.http import HttpResponse
from django.utils import simplejson

import time
import hmac
from hashlib import sha1 as  hash_alg
import base64

from turnapi import settings

import redis

import logging

# REST API or dynamic Long term credentials
if settings.TURN_AUTH:
  from rfc5766_turn_server_auth import calc_key
else:
  from rfc5766_turn_server import calc_key

from shared_key_updater import Start

logger = logging.getLogger( 'turnapi.api' )

if settings.TURN_REDIS_URL is not None:
  redis_server = redis.StrictRedis.from_url( settings.TURN_REDIS_URL )
elif settings.TURN_REDIS_UNIX_DOMAIN_SOCKET_PATH is None:
  redis_con = redis.StrictRedis(
    host     = settings.TURN_REDIS_HOST,
    port     = settings.TURN_REDIS_PORT,
    db       = settings.TURN_REDIS_DB,
    password = settings.TURN_REDIS_PASSWORD
  )
else:
  redis_server = redis.StrictRedis(
    unix_socket_path = settings.TURN_REDIS_UNIX_DOMAIN_SOCKET_PATH,
    db               = settings.TURN_REDIS_DB,
    password         = settings.TURN_REDIS_PASSWORD,
  )

realm = settings.TURN_REALM

# Move this configurations to anywhere else!
# SHared Secret
shared_secret = settings.TURN_SHARED_SECRET

shared_secret += '0'

data = {
    'shared secret' : shared_secret,
    'redis connection' : redis_con,
}

Start( data )

def turn( req ):
  query = req.GET

  service  = query.get( 'service',  None )
  username = query.get( 'username', None )
  ttl      = query.get( 'ttl'     , settings.TURN_KEY_TTL )

  # username: the TURN username to use, which is a colon-delimited
  # combination of the expiration timestamp and the username parameter
  # from the request (if specified)
  timestamp = str( int( time.time() ) + ttl )
  username = str( timestamp + settings.TURN_SEPARATOR + username if username else timestamp )

  # Call key
  shared_secret = data['shared secret']
  temp_pass = calc_key( username, realm, shared_secret )

  if not settings.TURN_AUTH:
    pKey = 'turn/user/%s/key' % ( username )
    kto  = settings.TURN_CREDENTIAS_TIMEOUT # seconds

    # Store credentials into Redis
    redis_con.setex( pKey, kto, temp_pass )

    # return plain text pass
    temp_pass = shared_secret
  # end if

  items = {
    "username" : username,
    "password" : temp_pass,
    "ttl"      : ttl,
    "uris"     : settings.TURN_API_URLS
  }

  logger.debug( 'Response: ' + str(items) )

  # Send JSON response
  items = simplejson.dumps( items )
  response = HttpResponse( items, content_type = 'application/json; charset=utf8' )

  return response
# end turn function
