import datetime
import time
from importlib import reload

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
    from spider6488.spiders import canada28
    reload(canada28)
    runner.crawl(canada28.Canada28Spider)

    from spider6488.spiders import pc_balls_luck28
    reload(pc_balls_luck28)
    runner.crawl(pc_balls_luck28.PcBallsLuck28Spider)

    from spider6488.spiders import luck_airship
    reload(luck_airship)
    runner.crawl(luck_airship.LuckAirshipSpider)

    from spider6488.spiders import chongq_ssc
    reload(chongq_ssc)
    runner.crawl(chongq_ssc.ChongqSscSpider)

    from spider6488.spiders import gold_luck11
    reload(gold_luck11)
    runner.crawl(gold_luck11.GoldLuck11Spider)

    from spider6488.spiders import beijing_happy8
    reload(beijing_happy8)
    runner.crawl(beijing_happy8.BeijingHappy8Spider)

    from spider6488.spiders import plan_beijing_pk10
    reload(plan_beijing_pk10)
    runner.crawl(plan_beijing_pk10.PlanBeijingPk10Spider)

    from spider6488.spiders import sg_airship
    reload(sg_airship)
    runner.crawl(sg_airship.SgAirshipSpider)

    from spider6488.spiders import chongq_luck_farm
    reload(chongq_luck_farm)
    runner.crawl(chongq_luck_farm.ChongqLuckFarmSpider)

    from spider6488.spiders import com1680380_ssc
    reload(com1680380_ssc)
    runner.crawl(com1680380_ssc.Com1680380SscSpider)

    from spider6488.spiders import com1680380_happy_very
    reload(com1680380_happy_very)
    runner.crawl(com1680380_happy_very.Com1680380HappyVerySpider)

    from spider6488.spiders import bj_pk10
    reload(bj_pk10)
    runner.crawl(bj_pk10.BjPk10Spider)

    from spider6488.spiders import gx_kl10
    reload(gx_kl10)
    runner.crawl(gx_kl10.GxKl10Spider)
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
