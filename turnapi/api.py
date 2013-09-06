"""api.py: Implemente rfc5766-turn-server HTTP server """

from django.http import HttpResponse
from django.utils import simplejson

import time
import hmac
from hashlib import sha1 as  hash_alg

from turnapi import settings

import redis

import logging

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

def turn( req ):
  query = req.GET

  service  = query.get( 'service',  None )
  username = query.get( 'username', None )
  ttl      = query.get( 'ttl'     , None )

  # Move this configurations to anywhere else!
  # SHared Secret
  shared_secret = settings.TURN_SHARED_SECRET
  # Separator
  SEPARATOR = ':'

  # Get request timestamp (Seconds since 1970)
  timestamp = str( int( time.time() ) )

  # Username is the paramter plus timestamp with an separator
  # if username not defined just use timestamp as username
  #
  # NOTE:
  #  * force if to be a str, otherwise HMAC throws a TypeError Exception!
  username = str( username + SEPARATOR + timestamp if username else timestamp )

  # Use HMAC SHA1 to create temporary key
  password = hmac.new( username, shared_secret, hash_alg).hexdigest()

  uKey = 'turn/user/%s/key' % ( username )
  pKey = 'turn/user/%s/password' % ( username )
  kto  = settings.TURN_CREDENTIAS_TIMEOUT # seconds

  # Store credentials into Redis
  redis_con.setex( uKey, kto, username )
  redis_con.setex( pKey, kto, password )

  items = {
    # "username" : "foo:" + timestamp,
    "username" : username,
    "password" : password,
    "ttl" : ttl if ttl else 86400,
    "uris" : settings.TURN_API_URLS
  }

  logger.debug( 'Response: ' + str(items) );

  # items = serializers.serialize('json', items, indent=4)
  items = simplejson.dumps( items )
  return HttpResponse( items, content_type = 'application/json; charset=utf8' )
