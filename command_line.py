#first import buil-in module
#second import third-party module
#third import your own module
#sys as only identifiers not methods like sys.version,sys.api_version,sys.last_traceback
import sys
for i in sys.argv:
	print (i)
print ("length: ",len(sys.argv))