import sys
import asyncio
import argparse

import config
from media_platform.douyin import DouYinCrawler
from media_platform.xhs import XiaoHongShuCrawler


class CrawlerFactory:
    @staticmethod
    def create_crawler(platform: str):
        if platform == "xhs":
            return XiaoHongShuCrawler()
        elif platform == "dy":
            return DouYinCrawler()
        else:
            raise ValueError("Invalid Media Platform Currently only supported xhs or douyin ...")


async def main():
    # define command line params ...
    parser = argparse.ArgumentParser(description='Media crawler program.')
    parser.add_argument('--platform', type=str, help='Media platform select (xhs|dy)...', default=config.platform)
    parser.add_argument('--keywords', type=str, help='Search note/page keywords...', default=config.keyword)
    parser.add_argument('--lt', type=str, help='Login type (qrcode | phone)', default=config.login_type)
    parser.add_argument('--phone', type=str, help='Login phone', default=config.login_phone)

    args = parser.parse_args()
    crawler = CrawlerFactory().create_crawler(platform=args.platform)
    crawler.init_config(
        keywords=args.keywords,
        login_phone=args.phone,
        login_type=args.lt
    )
    await crawler.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()
