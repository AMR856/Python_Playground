#!/usr/bin/python3
import os
from googleapiclient.discovery import build
import re
from datetime import timedelta
import sys

api_key = os.environ.get("API_KEY")

youtube = build('youtube', 'v3', developerKey=api_key)
# channel_id = str(sys.argv[2])
# playlist_number = int(sys.argv[3]) % 5
# channelId = 'UCxMsgwldMZiuFTD6jjv32yQ'
pl_request = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId = "UCxMsgwldMZiuFTD6jjv32yQ"
)

pl_response = dict()
try:
    pl_response = pl_request.execute()
except Exception as e:
    print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))

playlist_ids = []
for value in pl_response['items']:
    for key, val in value.items():
        if key == 'id':
            playlist_ids.append(val)


total_seconds = 0
next_page_token = None
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

print(playlist_ids)
while True:
    playlist_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId = "PLVblLQwRzdW2seSySMHxHZlEEKaP84H4G",
        maxResults=50,
        pageToken=next_page_token
    )

    playlist_response = dict()
    try:
        playlist_response = playlist_request.execute()
    except Exception as e:
        print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))

    videos_ids = []
    for value in playlist_response['items']:
        for key, val in value.items():
            if key == 'contentDetails':
                videos_ids.append(value[key]['videoId'])

    vid_request = youtube.videos().list(
        part='contentDetails',
        id=','.join(videos_ids)
    )

    vid_response = vid_request.execute()
    duration_list = []

    for item in vid_response['items']:
        for key, value in item.items():
            if key == 'contentDetails':
                duration_list.append(item[key]['duration'])
    # print(duration_list)
    for item in duration_list:

        hours = hours_pattern.search(item)
        minutes = minutes_pattern.search(item) 
        seconds = seconds_pattern.search(item)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()
        total_seconds = total_seconds + video_seconds
        next_page_token = playlist_response.get('nextPageToken')
    if not next_page_token:
        break

total_seconds = int(total_seconds)
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f"{hours} Hour, {minutes} Minutes, {seconds} Seconds")
