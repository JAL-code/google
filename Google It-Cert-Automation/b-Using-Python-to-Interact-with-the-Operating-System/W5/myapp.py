import os
import subprocess

#Modify the contents of a path enviroment variable by adding a directory
#copy the variable and add to system dictionary with path separation.
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
#call the myapp command with modified variable and the env to
#the child process will see.


result = subprocess.run(["myapp"], env=my_env)
