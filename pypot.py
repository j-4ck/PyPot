import socket
import sys
import threading
import queue
from colorama import Fore, init
import pygeoip

q = queue.Queue()
jobs_to_do = []
pots = len(sys.argv)
jbs = 1

while jbs < pots:
	jobs_to_do.append(jbs)
	jbs += 1

def locate(ip):
	global country
	global code
	g = pygeoip.GeoIP('/root/GeoIP.dat')
	country = g.country_name_by_addr(ip)
	code = g.country_code_by_name(ip)

def listen(port):
	host = ''
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		s.bind((host, port))
	except:
		print 'Failed to bind socket for port: ' + str(port)
	conns = 0
	attackers = []
	while True:
		s.listen(1)
		conn, addr = s.accept()
		locate(addr[0])
		if country:
			endstr = Fore.WHITE + ', ' + Fore.GREEN + country + Fore.WHITE + ' / ' + Fore.GREEN + code
		else:
			endstr = ''
		print Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + '] Port ' + Fore.GREEN + str(port) + Fore.WHITE + ' recieved a connection from: ' + Fore.GREEN + str(addr[0]) + Fore.WHITE + ':' + Fore.GREEN + str(addr[1]) + endstr
		conns += 1
		if addr[0] not in attackers:
			attackers.append(str(addr[0]))
		else:
			pass
def create_worker():
	for threads in range(pots):
		t = threading.Thread(target=work, args=())
		t.daemon = True
		t.start()
def work():
	x = q.get()
	listen(int(sys.argv[x]))
def create_jobs():
	for job in jobs_to_do:
		q.put(job)
	q.join()

def main():
	# Pot limit issue fixed!
	#if len(sys.argv) > 11:
	#	print 'Please dont set anymore ports than 10!'
	#	sys.exit()
	if len(sys.argv) < 2:
		print 'Supply a port for the program to listen on!'
		sys.exit()
	print Fore.GREEN + '''
                __
     __/~~\-''- _ !
__- - (            |
     /             |
    /       ;o    o)
    |              ;
                   '
       \_       (..)
         ''-_ _ _ /
           /
          /

PyPot, by j4ck
''' + Fore.WHITE
	print 'Setting Honey Pot(s)...'
	for elem in sys.argv[1:]:
		print 'Set ' + Fore.GREEN + '~> ' + Fore.WHITE + elem
	print 'Listening...\n'
	create_worker()
	create_jobs()
if __name__ == '__main__':
	main()
