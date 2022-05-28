import sys
import requests
from requests.exceptions import HTTPError

if __name__ == "__main__":
    try:
        url = "https://" + sys.argv[1]
        response = requests.get(url)
        if (response.status_code == 200):
            response.encoding = 'utf-8'
            print(response.content)
    except HTTPError as http_err:
        print("HTTP Error ocurred: " + http_err)
    except IndexError as index:
        print("No URL")
    except Exception as err:
        print("Error: " + err)

        # TODO: parse HTML and grep "rss"
