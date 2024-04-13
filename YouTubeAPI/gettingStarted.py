#!/usr/bin/python3
import os
from googleapiclient.discovery import build
api_key = os.environ.get("API_KEY")

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    id = 'UCxMsgwldMZiuFTD6jjv32yQ'
)

try:
    response = request.execute()
except Exception as e:
    print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
for key, value in response.items():
    print(f"{key} is {value}")