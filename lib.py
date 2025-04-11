import os 
import shutil 


path="C:\\" if os.name =="nt" else "/mnt/c"

total,used,free = shutil.disk_usage(path)
print("OS name: %s" % os.name)
print("running on the path %s" % path)
print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))


