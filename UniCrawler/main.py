#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from UniCrawler.spiders import haw, htw, htwk, tuberlin, fhw, ul, uni

unilist = ["htw,htw-dresden.de,https://www.htw-dresden.de,studium/vor-dem-studium/studienangebot",
            "fhw,fh-wedel.de,https://www.fh-wedel.de,bewerben/bachelor"
            ]

def main():
    """ Main program """
    # Code goes over here.
    process = CrawlerProcess(get_project_settings())

    # for elem in unilist:
    #     name, domain, url, path = elem.split(",")
    #
    #     print(f"{name}")
    #
    #     uniSpider = uni.UniSpider
    #
    #     process.crawl(uniSpider(name,domain,url,path))
    #     process.start()
    #     uniSpider.write_json(uniSpider)
    #htwkSpider = htwk.HtwkSpider
    htwSpider = htw.HtwSpider
    #tuBerlinSpider = tuberlin.TuBerlinSpider
    #fhwSpider = fhw.FhwSpider
    #ulSpider = ul.UlSpider


    #process.crawl(haw.CrawlingSpider)
    process.crawl(htwSpider)
    #process.crawl(htwkSpider)
    #process.crawl(tuBerlinSpider)
    #process.crawl(fhwSpider)
    #process.crawl(ulSpider)


    process.start()


    htwSpider.write_json(htwSpider)
    #htwkSpider.write_json(htwkSpider)
    #tuBerlinSpider.write_json(tuBerlinSpider)
    #fhwSpider.write_json(fhwSpider)
    #ulSpider.write_json(ulSpider)

    return 0


if __name__ == "__main__":

    main()