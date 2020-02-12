#!/usr/bin/python3

from telnetlib import Telnet
import re
import time

def copyrouter(username, password, rackno, verno, routerno):
    if rackno == 'BJRack01':
		rackip = '172.17.100.111'
	elif rackno == 'BJRack02':
		rackip = '172.17.100.112'
	elif rackno == 'BJRack03':
		rackip = '172.17.100.113'

	portno = 2000 + int(routerno)

	tn = Telnet(rackip, portno)

#正则表达式匹配各种状态

	yesorno = re.compile(r'.*Please answer.*')
	exc = re.compile(r'.*>')
	configure = re.compile(r'.*\(config.*\)#')
	priv = re.compile(r'.*#')
	clearconfig = re.compile(r'Router(#|>)')
	passwd = re.compile(r'Password: ')

#多次回车确认状态

	tn.write(b'\n')
	tn.read_very_eager()
	time.sleep(1)
	tn.write(b'\r\n')
	tn.read_very_eager()
	time.sleep(1)
	tn.write(b'\n')
	tn.read_very_eager()
	time.sleep(1)
	tn.write(b'\r\n')
	tn.read_very_eager()
	time.sleep(1)
	tn.write(b'\n')

#获取位置状态信息

	rackreply = tn.expect([],timeout=1)[2].decode().strip()

#基于状态采取行为
	while True:
		tn.write(b'\n')
		rackreply = tn.expect([],timeout=1)[2].decode().strip()
		if yesorno.match(rackreply):
			#yes or no初始化状态
			tn.write(b'no\n\n\n')
			time.sleep(5)
			tn.write(b'\n')
			while True:
				tn.write(b'\n')
				yesornoreply = tn.expect([],timeout=1)[2].decode().strip()
				if clearconfig.match(yesornoreply):
					break
				else:
					tn.write(b'\r\n')
					time.sleep(1)
					tn.write(b'\n')
					tn.write(b'no\n\n\n')
			tn.write(b'\n')
			tn.write(b'enable\n')
			time.sleep(1)
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			time.sleep(1)
			tn.write(b'enable\n')
			time.sleep(1)
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'\n')
			break

		elif configure.match(rackreply):
			#全局配置模式
			tn.write(b'\n')
			tn.write(b'end\n')
			time.sleep(1)
			tn.write(b'end\n')
			time.sleep(1)
#			print('match configure')
			break

		elif exc.match(rackreply):
			#执行模式
			tn.write(b'\r\n')
			time.sleep(1)
			tn.write(b'\n')
			tn.write(b'enable\n')
			time.sleep(1)
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			time.sleep(1)
			tn.write(b'enable\n')
			time.sleep(1)
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'cisco\n\n')
			tn.write(b'\r\n')
			time.sleep(1)
			tn.write(b'\n')
			time.sleep(1)
#			print('match exec')
			break

		elif priv.match(rackreply):
			#特权模式
			tn.write(b'\r\n')
			time.sleep(1)
			tn.write(b'\n')
			time.sleep(1)
#			print('match priv')
			break
		else:
			tn.write(b'\r\n')
			time.sleep(1)
			tn.write(b'\n')
			time.sleep(1)
#			print(rackno + ' Router ' + str(routerno) + 'next')


#继续回车确认状态
	tn.write(b'\r\n')
	time.sleep(1)
	tn.write(b'\n')


#拷贝配置

	tn.write(b'\r\n')
	tn.write(b'end\n')
	time.sleep(1)
	tn.write(b'end\n')
	time.sleep(1)
	tn.write(b'\n')
	tn.write(b'enable\n')
	time.sleep(1)
	tn.write(b'cisco\n\n')
	tn.write(b'cisco\n\n')
	tn.write(b'cisco\n\n')
	time.sleep(1)
	tn.write(b'enable\n')
	time.sleep(1)
	tn.write(b'cisco\n\n')
	tn.write(b'cisco\n\n')
	tn.write(b'cisco\n\n')
	time.sleep(1)
	tn.write(b'\r\n')
	tn.write(b'\n')
	tn.write(b'terminal length 0\n\n')
	time.sleep(1)
	tn.write(b'terminal length 0\n\n')
	time.sleep(1)
	tn.write(b'\r\n')
	tn.write(b'\n')
	time.sleep(1)
	tn.read_very_eager()
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	tn.write(b'show run\n')
	rackreply = tn.expect([],timeout=10)[2].decode().strip()
	configfile = '/python/cgi-bin/tmpconfig/' + verno + '/' + 'R' + routerno + '.txt'
	config = open(configfile, 'w')
	config.write(rackreply)
	config.close()
	tn.close()

if __name__ == "__main__":
	copyrouter('labtest', 'Cisc0123', 'BJRack02', 've', '4')