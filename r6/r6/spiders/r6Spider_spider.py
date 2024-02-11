import scrapy
from urllib.parse import urlencode
from gui import values 

API_KEY = '8061dbbd-b3a4-44d2-9f15-3d61e4901abc'

# Creates gamer list from value given by user
def make_gamer_list():
    user_input= values['-GAMER-']
    if user_input =='':
            gamer_list = ['MaxUnknown19','Ajonto12','oSpiriTz']
    else:
        gamer_list = user_input.split()
    return gamer_list
# Scrapes for player rank if user selects it 
def scrape_rank(item,response):
    if values['-RANK-'] == True:
        rankName = response.css('div.trn-text--dimmed::text').get().strip()
        item['Rank'] = rankName
# Scrapes for player kd if user selects it
def scrape_kd(item,response):
    if values['-KD-'] == True:
        kd = response.css('div.trn-defstat__value[data-stat="PVPKDRatio"]::text').get().strip()
        item['KD'] = kd
#Creates proxy url for scrape    
def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class r6Spider_spider(scrapy.Spider):
    name = 'r6_stat_profile'
# Begins scrape 
    def start_requests(self):
        gamer_list = make_gamer_list()
        
        for gamer in gamer_list:
            r6_gamer_url = f'https://r6.tracker.network/profile/pc/{gamer}'
            yield scrapy.Request (url= get_scrapeops_url(r6_gamer_url), callback =self.parse_profile, meta={'gamer': gamer, 'r6_stat_url' :r6_gamer_url})
#Parses scrape 
    def parse_profile(self,response):
        item = {}
        item['Gamer'] = response.meta['gamer']
        item['R6_Stat_Url'] = response.meta['r6_stat_url']

        # Extract User Name 
        name_text = response.css("span.trn-profile-header__name::text").get()

        if name_text is not None:
        # If name_text is not None, strip it
            item['Name'] = name_text.strip()
            
        else:
        # Handle the case where name_text is None
            item['Name'] = 'Unknown Name'
            
        #Extract Rank
        scrape_rank(item,response)
        
        #Extract KD 
        scrape_kd(item,response)
       
        yield item 


        

