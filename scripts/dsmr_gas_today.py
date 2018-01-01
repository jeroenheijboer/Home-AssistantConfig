import requests
import json

response = requests.get(
 'http://127.0.0.1/api/v2/consumption/today?ordering=-timestamp&limit=1',
 headers={'X-AUTHKEY': 'M9Q0HLJ1G9OFJKE45CVUFO6P78T7S3HROUUXAQ8RKH2FZRDVEHQELQG7YRMRNW3Z'},
)

if response.status_code != 200:
    print('Error: {}'.format(response.text))
else:

    print(response.json()['gas'])
