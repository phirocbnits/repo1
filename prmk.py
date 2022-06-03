#shebang not added
#running a ssh server with paramiko and executing a command in the slient server without logging in
import paramiko
import os
import time
#imposrt passwd from env variable. write in terminal $export PASS='<password>'
passwd = os.environ.get('PASS')
#open connection
ssh=paramiko.SSHClient()
#to automate the yes for every verification
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(username='nits',hostname='localhost',password=passwd)
#ssh.connect(username='nits',hostname='localhost',key_filename="<.pem file>")
stdin,stdout,stderr=ssh.exec_command("free -m")
#to add time to the process to run as it faces time err
time.sleep(5)
#to print the o/p file generated after executing the code
print(stdout.readlines())
#close connection
ssh.close()