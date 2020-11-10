import requests

domain='amwanjau.com'

subfile=open('./subdomains.txt','r')
content=subfile.read()
subdomains=content.splitlines()

for subdomain in subdomains:
     url=f'https://{subdomain}.{domain}'
     try:
          requests.get(url)
     except requests.ConnectionError:
          pass
     else:
          print(f'Discovered subdomain: {url}')