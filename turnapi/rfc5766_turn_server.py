import hmac
from hashlib import md5

def calc_key( username, realm, passwd):
  """
  Calculate temporary key
  """
  k = username + ':' + realm + ':' + passwd
  m = md5()
  m.update( k )
  return m.hexdigest();

if __name__ == "__main__":
  """
  Simple example
  """
  print "TURN Server rfc5766-turn-server test"
  expected = "7da2270ccfa49786e0115366d3a3d14d"
  result = calc_key( 'gorst', 'north.gov', 'hero' )
  print "Success!" if expected == result else "Error"
  print result
