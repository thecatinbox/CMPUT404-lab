import requests

# Print out the version of the requests library
print(requests.__version__)

# GET the Google homepage
print(requests.get("http://www.google.com/"))

# Download from GitHub and print out its own source code from GitHub
x = requests.get("https://raw.githubusercontent.com/thecatinbox/CMPUT404-lab/main/lab1/find_version.py")
print(x.text)
