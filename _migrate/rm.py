import os
import re
root="./"
for path, subdirs, files in os.walk(root):
    for name in files:
        sp = name.split(".")
        fname = "".join(sp[0:-1])
        if re.search(r"-(\d+)x(\d+)$", fname):
            os.remove(os.path.join(path, name))
            print(fname)