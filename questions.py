import requests

headers = {
    'x-api-key': 'sec_Ukn8HzBwnANHMxiE0gMGUF9QdVfPpjzS',
    "Content-Type": "application/json",
}

data = {
    'sourceId': "src_fpXRsEbqBUGo8m1Bq9xyn",
    'messages': [
        {
            'role': "user",
            'content': "do que se trata esse pdf?",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)