import requests
import sys
import os

if 'REDIRECT_URL' not in os.environ or 'URL' not in os.environ:
    print('REDIRECT_URL and URL environment variables must be set')
    sys.exit(1)

REDIRECT_URL = os.environ['REDIRECT_URL']
URL = os.environ['URL']

response = requests.get(URL, allow_redirects=False)

if response.status_code != 301:
    print('Not redirected')
    sys.exit(1)

actual_redirect_url = response.headers['Location']
if actual_redirect_url != REDIRECT_URL:
    print(f'Incorrect redirect location: {actual_redirect_url}, expected: {REDIRECT_URL}')
    sys.exit(1)

print('Redirected successfully')
sys.exit(0)
