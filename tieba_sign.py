import asyncio
import datetime
import json
import os
import re
import sys

import httpx
from bs4 import BeautifulSoup
from loguru import logger

script_path = os.path.split(os.path.realpath(sys.argv[0]))[0]


def load_cookie_from_config():
    with open(f'{script_path}/cookie.json', 'r') as f:
        content = f.read()
        return json.loads(content)['baidu_cookie']


class TiebaSigner:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Cookie': load_cookie_from_config()
        }
        logger.add("run.log", rotation="10 MB", retention=datetime.timedelta(days=10))

    async def fetch_url(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            return response.text

    async def get_like_list(self):
        logger.info("开始获取账号关注的贴吧列表")
        url = "https://tieba.baidu.com/f/like/mylike"
        try:
            html_str = await self.fetch_url(url)
            pn_list = re.findall(r'<a href="/f/like/mylike\?&pn=(.*?)\">', html_str, re.S)
            page_num = pn_list[-1]
        except IndexError:
            logger.error("cookie为空或者已过期，请在cookie.json文件中填写正确的cookie后重试")
            return
        tasks = []
        for i in range(1, int(page_num) + 1):
            page_url = f"https://tieba.baidu.com/f/like/mylike?&pn={i}"
            tasks.append(self.fetch_url(page_url))
        logger.info(f"列表获取成功，总共签到{page_num}页")
        html_responses = await asyncio.gather(*tasks)
        n = 0
        for html_str in html_responses:
            contain = BeautifulSoup(html_str, "html.parser")
            first = contain.find_all("tr")
            for result in first[1:]:
                n += 1
                second = result.find_next("td")
                name = second.find_next("a")['title']
                tbs = second.find_next("span")['tbs']
                await self.sign(name, tbs)
        logger.info(f"执行完毕，共签到{n}个贴吧")

    async def sign(self, kw, tbs):
        sign_url = "https://tieba.baidu.com/sign/add"
        data = {
            'ie': 'utf-8',
            'kw': kw,
            'tbs': tbs,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(sign_url, headers=self.headers, data=data)
            json_data = response.json()
            if 'error' in json_data and not json_data['error']:
                rank = json_data['data']['finfo']['current_rank_info']['sign_count']
                num = json_data['data']['uinfo']['total_sign_num']
                logger.info(f"{kw}吧 签到成功✔！, 签到排名：{rank}, 已签到 {num}天")
            else:
                logger.warning(f"{kw}吧 签到失败✘, 返回信息: {json_data.get('error', 'Unknown error')}")


if __name__ == '__main__':
    if sys.version_info >= (3, 7):
        asyncio.run(TiebaSigner().get_like_list())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(TiebaSigner().get_like_list())
