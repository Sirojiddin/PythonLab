# TODO New probe
import sys
import platform

info = 'Os info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture()
)
# print(info)
with open('os_infi.txt','w') as ff:
    ff.write(info)