import requests

subject = 'Python (programming language)'

url = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'format':'json',
    'titles': subject,
    'prop': 'extracts',
    'exintro': True,
    'explaintext': True
}

response = requests.get(url, params=params)
data = response.json()

print(data)