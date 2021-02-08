import requests
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
        # print(page_html)
        HandlerGetMovies.parse_page_html(page_html)

    @staticmethod
    def parse_page_html(page_html):
        pattern = re.compile(r'<div id="nowplaying">(.*)?</div>', re.S)
        # 获取热映html
        result_list = re.findall(pattern, page_html)
        pattern2 = re.compile(r'<li.*?data-title="(.*?)".*?data-score="(.*?)".*?data-star="(.*?)".*?data-release="(.*?)".*?data-duration="(.*?)".*?data-region="(.*?)".*?data-director="(.*?)".*?data-actors="(.*?)".*?data-category="(.*?)".*?<li class="poster">.*?<a href="(.*?)".*?src="(.*?)".*?</a>', re.S)
        # 获取所有热映的影片信息
        result_list2 = re.findall(pattern2, result_list[0])
        print(result_list2)  # 还要提取详情页面的图片和剧情简介


