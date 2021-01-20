import requests
import os
import json
from config import BEARER_TOKEN


def init_search_url(query):
    query = query
    url = "https://api.twitter.com/2/tweets/search/recent?query={}".format(
        query
    )
    return url


def create_url(next_token='', query):
    query = query
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&next_token={}".format(
        query, next_token
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    query = "chicago"
    bearer_token = BEARER_TOKEN
    next_token = ''
    # each search return 10 tweets, range(2) will return 2*10 tweets
    for i in range(2):
        if i == 0:
            url = init_search_url(query)
        else:
            url = create_url(query, next_token)
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url, headers)
        next_token = json_response['meta']['next_token']
        result = json.dumps(json_response, indent=4, sort_keys=True)
    print(result)


if __name__ == "__main__":
    main()
