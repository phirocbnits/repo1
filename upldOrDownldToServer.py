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
ftp_client=ssh.open_sftp()
#for uploading file in client server
#put(src,destination).. dest=/home/usr/given_file
ftp_client.put("tempfile","tempfile")
#for downloading file from client server
#ftp_client.put("tempfile","tempfile")
#close connection
ssh.close()