import requests
from requests.auth import HTTPBasicAuth

# Define the URL and credentials
url = 'https://example.com/api/login'
username = 'DebraB@M365x960335.OnMicrosoft.com'
password = 'L3@kedcred'

# Perform the request with basic authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    print('Authentication successful!')
    print('Response:', response.json())
else:
    print('Authentication failed.')
    print('Status code:', response.status_code)
    print('Response:', response.text)
