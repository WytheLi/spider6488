import datetime
import importlib
import time
import schedule
from crochet import setup

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner, CrawlerProcess


setup()


def start_spider():
    # 先加载配置文件
    # process = CrawlerProcess(get_project_settings())
    # process.crawl(LuckAirshipSpider)
    # # process.crawl(lie_3)
    # process.start()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("###################   " + now_time + "   ###################")

    # https://www.cnblogs.com/WalkOnMars/p/11934535.html
    runner = CrawlerRunner(get_project_settings())
    from spider6488.spiders import com1680380_k3
    importlib.reload(com1680380_k3)
    # module = importlib.import_module('spider6488.spiders.com1680380_k3')
    # cls = getattr(module, 'Com1680380K3Spider')
    # # cls = classes(1)
    runner.crawl(com1680380_k3.Com1680380K3Spider)
    d = runner.join()


def main():
    print('###################   爬虫主程序启动   ###################')
    # schedule.every().day.at("11:06").do(start_spider)
    schedule.every(3).minutes.do(start_spider)

    # schedule.every().day.at("17:00").do(start_spider)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
