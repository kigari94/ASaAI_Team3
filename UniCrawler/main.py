#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from UniCrawler.spiders import haw, htw, htwk


def main():
    """ Main program """
    # Code goes over here.
    process = CrawlerProcess(get_project_settings())

    htwkSpider = htwk.HtwkSpider
    htwSpider = htw.HtwSpider

    #process.crawl(haw.CrawlingSpider)
    process.crawl(htwSpider)
    process.crawl(htwkSpider)
    process.start()


    htwSpider.write_json(htwSpider)
    htwkSpider.write_json(htwkSpider)

    return 0


if __name__ == "__main__":

    main()