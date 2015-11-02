import subprocess

# fs = open("sub.txt", "w")
# op = subprocess.Popen("/bin/ls", stdout=subprocess.PIPE)
# input()

x = subprocess.run(["ls"], subprocess.PIPE)
