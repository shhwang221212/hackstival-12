from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import time
import os
import logging

load_dotenv()

DEVELOPER_KEY = os.getenv('GOOGLE_DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
    
def youtube_search(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    request = youtube.search().list(
        part = 'snippet',
        q = query, # 'boating|sailing -fishing'과 같이 여러 조건으로도 검색할 수 있음
        type = 'video',
        maxResults = 5,
        # publishedAfter = '', # 특정 날짜 이후 게시된 비디오만 검색 ex. 2023-01-01T00:00:00Z
        # publishedBefore = '', # 특정 날짜 이전에 게시된 비디오만 검색 ex. 2023-12-31T23:59:59Z
    )
    response = request.execute()
    time.sleep(1) # 프로세스 일시정지 / Connection Reset By Peer 방지
    
    for idx, item in enumerate(response['items']):
        if item['id']['kind'] == 'youtube#video':
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            print(f"idx: {idx}, title:{title}, videoId:{video_id}")
    
try: 
    youtube_search('python')
except ConnectionResetError as e:
    logging.error("Youtube Search API ConnectionResetError")
    logging.error(e)
except Exception as e:
    logging.error("Youtube Search API Error")
    logging.error(e)
