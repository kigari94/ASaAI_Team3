#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from UniCrawler.spiders import haw, htw, htwk, tuberlin

def main():
    """ Main program """
    # Code goes over here.
    process = CrawlerProcess(get_project_settings())

    htwkSpider = htwk.HtwkSpider
    htwSpider = htw.HtwSpider
    tuBerlinSpider = tuberlin.TuBerlinSpider

    #process.crawl(haw.CrawlingSpider)
    process.crawl(htwSpider)
    #process.crawl(htwkSpider)
    #process.crawl(tuBerlinSpider)
    #process.crawl(bhtBerlinSpider)

    process.start()


    htwSpider.write_json(htwSpider)
    #htwkSpider.write_json(htwkSpider)
    #tuBerlinSpider.write_json(tuBerlinSpider)

    return 0


if __name__ == "__main__":

    main()