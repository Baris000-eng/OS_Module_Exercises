import os
pid = os.fork()
if pid == 0:
    print("Child Process")
else:
    print("Parent Process")
