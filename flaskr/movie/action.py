import requests
import os
import re

class HandlerGetMovies(object):
    """
    获取豆瓣电影信息
    """
    # base_url = 'https://movie.douban.com'

    def __init__(self):
        self.base_url = 'https://movie.douban.com'
        self.sleep_time = 1
        self.retry_count = 10

    def get_page_html(self):
        if self.retry_count == 0:
            print('get movie fail')
            return
        # proxies = {'https': 'http://127.0.0.1:9080'}
        url = self.base_url + '/cinema/nowplaying/wuhan'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
        except Exception as e:
            print(e)
            self.retry_count -= 1
            self.get_page_html()
        page_html = response.text
        print(page_html)

