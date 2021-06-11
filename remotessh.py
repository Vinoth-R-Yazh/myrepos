import subprocess
import os
#Perform multi command task in remote servers
# By Vinoth_Ravi
#Servers List
hosts=open('/home/wb512863/script/server_list.txt', 'r')
#Commands List
cmd1=open('/home/wb512863/script/commands', 'r')
cmdList=[]
for cm in cmd1:
    cmdList.append(cm)
for host in hosts:
    #hosts List:
    host=host.strip()
    proc = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode == 0:
        ssh = subprocess.Popen(["ssh", host],stdin =subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)
	# Send ssh commands to stdin to perform the task
        for cm in cmdList:
            ssh.stdin.write(cm)
        ssh.stdin.close()

	# Fetch output:
        with open('Output.log','a') as output:
            output.write("-------------------------------------------------------------------------")
            for line in ssh.stdout:
                print(line.strip())
	        output.write("\n" + line)
    else:
        print(host, 'is down!')
