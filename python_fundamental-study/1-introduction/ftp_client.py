from ftplib import FTP

ftp = FTP('')
site = input('ip address ? :')
ftp.connect(site,1040)
ftp.login('user', '12345')
ftp.cwd('') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = '124.txt' #replace with your file in your home folder
 ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 #filename = '1245.txt' #replace with your file in the directory ('directory_name')
 filename = input('filename?:')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()




if __name__ == '__main__':

 # uploadFile()
 downloadFile()