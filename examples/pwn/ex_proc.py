#!/usr/bin/env python
from ptrlib import *

# create process
p = Process(["/usr/bin/env", "cat"], cwd="/tmp")

p.sendline("Test 1")
print(p.recvline())

p.sendline("Test 2")
p.shutdown("send")  # close write pipe
print(p.recvline()) # still receivable

try:
    p.sendline("Test 3") # can no longer write
except Exception as e:
    print(e)

# close pipe
p.close()
