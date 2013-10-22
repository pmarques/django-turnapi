import hmac
from hashlib import sha1 as  hash_alg
import base64

def calc_key( username, realm, shared_secret):
  """
  Temporary key is the Base 64 of HMAC-SHA1 of
  shared_secret and username
  """
  temp_pass = hmac.new( shared_secret, username, hash_alg).digest()
  temp_pass = base64.b64encode( temp_pass )

  return temp_pass

if __name__ == "__main__":
  """
  Simple example
  """
  print "TURN Server rfc5766-turn-server test"
  expected = "7da2270ccfa49786e0115366d3a3d14d"
  result = calc_key( 'gorst', None, 'hero' )
  print "Success!" if expected == result else "Error"
  print result
