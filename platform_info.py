import sys
from platform import uname
print("Python {}.{}.{} on".format(*sys.version_info) +
      " {0} {4}: {5}".format(*uname()))
print(sys.version_info)
print("""
Underlying platform 
system   : {0} 
node     : {1}
release  : {2}
version  : {3}
machine  : {4}
processor: {5}""".format(*uname()))
