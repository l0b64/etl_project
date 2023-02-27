import pandas as pd
import requests
import json


def extract_json_data_from_url(url):
    """
    This function fetch json data from a URL
    """
    response_from_api = requests.get(url)
    raw_data = response_from_api.text
    parsed_raw_data = json.loads(raw_data)
    return parsed_raw_data
