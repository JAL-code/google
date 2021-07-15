#!/usr/bin/env python3
import os
import sys
import subprocess

filename = sys.argv[1]

if not os.path.exists(filename):
    with open (filename, "w") as f:
        f.write("#!/usr/bin/env python3")
        f.write("import os, sys, re")
    subprocess.run(["chmod","+x",filename])
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
