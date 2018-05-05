import os
import webbrowser
import requests
from bs4 import BeautifulSoup
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''
def get_query_from_input(query=None):
    if query == None:
        query = raw_input('Enter the song to be played: ')
    query = query.replace(' ', '+')
    return query

def get_youtube_page(query):
    # search for the best similar matching video
    url = 'https://www.youtube.com/results?search_query=' + query
    source_code = requests.get(url,timeout=15)
    return source_code

def get_first_link_from_http(response):
    plain_text = response.text
    soup = BeautifulSoup(plain_text, "html.parser")
    # fetches the url of the video
    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
    first_song = songs[0].contents[0].contents[0].contents[0]
    link = 'https://www.youtube.com' + first_song['href']
    return link

def link_from_input_query(query=None):
    query = get_query_from_input(query)
    response = get_youtube_page(query)
    return get_first_link_from_http(response)

if __name__ == "__main__":
    link = link_by_input_query()
    webbrowser.open(link)