import os
import json
import platform
postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("Python version: {0}".format(platform.python_version())) 
response.close()