""" Implemente Shared Key Updater """

from turnapi import settings

import redis

from threading import Timer
import time

import logging

logger = logging.getLogger( 'turnapi.api' )

to = settings.TURN_KEY_TTL

from datetime import datetime 

keyUpdater = None

# Keys Updater
def genKey( data, first = False ):
  logger.debug( "Gen new key %s " % ( datetime.now() ) )

  shared_secret = data['shared secret']
  redis_con = data['redis connection']

  logger.debug( "Shared Secret (Old): %s" % ( shared_secret ) )

  # TODO: Gen random secret
  # Mod 10 to keep number lengt equal to 1 xD
  index = ( int(shared_secret[-1:] ) + 1 ) % 10
  shared_secret = shared_secret[:-1] + str( index )
  if not first:
    data['shared secret'] = shared_secret

  # the keys are always synchronized on timestamp
  ts = int( time.time() )
  ts = int(ts / to) * to

  # if the first gen a key behind otherwise
  # generates the next one
  if not first:
    ts += to

  logger.debug( "Set key %d => %s " % ( ts, datetime.fromtimestamp( ts ) ) )
  key = "turn/secret/%d" % ( ts )
  ret = redis_con.setnx( key, shared_secret )
  if ret == 1:
    logger.debug( "Set Key TTL %d, expire at %s" % (to, datetime.fromtimestamp( ts + to ) ) )
    redis_con.expireat( key, ts + to )
  else:
    data['shared secret'] = redis_con.get( key )

  logger.debug( "Shared Secret (New): %s" % ( shared_secret ) )

  if first:
    return

  # Schedule next update
  nxt = datetime.fromtimestamp( ts + to * 2 / 3 )
  now = datetime.now()
  waitTime = (nxt - now).total_seconds()
  if waitTime <= 0:
    waitTime = 1

  logger.debug( "Next Key at %s (%d)" % ( datetime.fromtimestamp( time.time() + waitTime), waitTime ) )

  keyUpdater = Timer( waitTime, genKey, (data, False) )
  keyUpdater.start()
  return
# end genKey

def Start( data ):
  logger.debug( "Start auto key generator!" )
  genKey( data )
  # generates the previous key if not define
  genKey( data, True )
# end Start

def Stop():
  logger.warning( "Not Imlemented" )
# end Stop
