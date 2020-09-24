#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

OSName=form.getvalue("x")
#OSName=input("Name of OS:")
OSimage=form.getvalue("y")

cmd="sudo docker run -d -i -t --name {0} {1}".format(OSName,OSimage)

output=sp.getstatusoutput(cmd)


status=output[0]
op=output[1]

if status==0:
    print("Your Docker OS is launced {} ".format(OSName))
else:
    print("Try Again {}".format(op))


