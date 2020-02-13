import ftplib
import os

def putfile(site, file, rdir='.', ldir='.', verbose=True):
    if verbose:
        print('Uploading', file) #print the message for uploading
    os.chdir(ldir)
    local = open(file, 'rb') # open local file
    remote = ftplib.FTP()
    # connect remote site
    remote.connect(site,1040)
    remote.encoding = 'GB18030'
    remote.login('user', '12345')
    remote.cwd(rdir)
    remote.storbinary('STOR' + file, local) # begin to upload the file
    #ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    remote.quit()
    local.close()
    if verbose:
        print('Upload Done') # finish the uploading

if __name__ == '__main__':
    import getpass
   # ftphost = input('Please input the host address')
    #filename = input('which file name')
    #username = input('username')
    #password = getpass.getpass(prompt='password?')
    site = '127.0.0.1'
    filename = '1245.txt'
    username = 'user'
    password = '12345'
    putfile(site, filename)
