import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("STATUS ANALYZER")
print(ascii_banner)
print("by Shoumik Chandra")
print("[!] Enter the website:")
url = str(input(' :- '))
request = requests.get(url)
print(request.status_code)
