import requests 
from requests.auth import HTTPBasicAuth
url = 'http://10.100.1.1/goform/WPSSetup'
payload = {'WPSEnable':'0','wpsConfigEnable':'','wpsConfig':'0'}
result = requests.post(url, data=payload, auth=HTTPBasicAuth('cisco', 'admin'))
result.status_code

