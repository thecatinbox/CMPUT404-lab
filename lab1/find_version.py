import requests

print(requests.__version__)
x = requests.get("https://raw.githubusercontent.com/thecatinbox/CMPUT404-lab/main/lab1/find_version.py")
print(x.text)