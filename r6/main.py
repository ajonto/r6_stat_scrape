from r6.spiders.r6Spider_spider import r6Spider_spider
from scrapy.crawler import CrawlerProcess

class main():
#crawl and create csv output
    def main():
        process = CrawlerProcess({'FEED_FORMAT': 'csv', 'FEED_URI': 'spider.csv'} )
        process.crawl(r6Spider_spider)
        process.start()
        print(" Results exported to spider.csv")



    if __name__ == '__main__':
        main()


        