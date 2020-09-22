# structure
# country,description,designation,points,
# price,province,region_1,region_2,taster_name,
# taster_twitter_handle,title,variety,winery
import scrapy
import json
import scrapy

header = [
    '', 'country','description','designation','points',
    'price','province','region_1','region_2','taster_name',
    'taster_twitter_handle','title','variety','winery'
]

sample = {
    'country': 'US',
    'description': 'Ah good',
    'designation': 'Alcohol',
    'points': 15, 
    'price': 35,
    'province': 'Cali',
    'region_1': 'West',
    'region_2': 'East',
    'taster_name': 'foo',
    'taster_twitter_handle': '@bar',
    'title': 'Good good',
    'variety': 'Gim',
    'winery': 'Basker'
}

FROM_PAGE = 1
TO_PAGE = 2

count = -1

def isFloat(x):
    try: 
        float(x)
    except:
        return False 
    return True

def writeHeader(file, header):
    file.write('%s\n' % ','.join(header))

def writeData(file, header, data):
    global count
    count += 1
    values = [str(count)]
    for field in header:
        if field == '':
            continue
        value = data.get(field, '')
        values.append(json.dumps(value))
    file.write('%s\n' % ','.join(values))

f = open('wine.csv', 'w')

class WineSpider(scrapy.Spider):
    DOWNLOAD_DELAY = 0.25
    name = 'winespider'

    def start_requests(self):
        for i in range(FROM_PAGE, TO_PAGE+1):
            yield scrapy.Request(
                url='https://www.winemag.com/?s=&drink_type=wine&page=%d' % i,
                callback=self.parsePageList
            )
            
    def parsePageList(self, response):
        pageLinks = response.xpath('//a[@class="review-listing row"]/@href').extract()
        for pageLink in pageLinks:
            print(pageLink)
            yield scrapy.Request(
                url=pageLink,
                callback=self.parseReviews
            )
        
    def parseProfilePage(self, response):
        handle = response.xpath('string(//li[@class="info-item twitter"])').extract()
        review = response.meta.get('review')
        if len(handle):
            handle = handle[0]

        review['taster_twitter_handle'] = handle
        # TODO: Write 
        writeData(f, header, review)
        return review
        
    def parseReviews(self, response):
        result = {}
        description = response.xpath('string(//p[@class="description"])').extract()[0]
        points = int(response.xpath('//span[@class="rating"]//text()')[0].extract())
        title = response.xpath('//h1/text()').extract()[0]

        result['title'] = title
        result['description'] = description
        result['points'] = points

        detailPane = response.xpath('//ul[@class="primary-info"]/*')
        for line in detailPane: 
            # get which field name:
            field = line.xpath('.//div[@class="info-label medium-7 columns"]/span/text()').extract()[0]
            value = line.xpath('string(.//div[@class="info medium-9 columns"]/span)').extract()
            
            if value:
                value = value[0]
            field = field.lower()

            if field == 'appellation':
                converted = value.split(',')[::-1]
                len_converted = len(converted)
                for i in range(4-len_converted):
                    converted.append('')
                country, province, region_2, region_1 = converted

                result['region_1'] = region_1.strip()
                result['region_2'] = region_2.strip()
                result['province'] = province.strip()
                result['country'] = country.strip()
            elif field == "price":
                # print('PRICE:', value)
                commasPos = value.find(',')
                if commasPos < 0: 
                    commasPos = len(value)
                value = value[1:commasPos]
                result['price'] = value
            else:
                result[field.lower()] = value

        taster_name = response.xpath('string(//span[@class="taster-area"])').extract()
        taster_link = response.xpath('//span[@class="taster-area"]/a/@href').extract()[0]
        
        result['taster_name'] = taster_name[0]
        # get handle
        
        print('NAME:', taster_link)
        handleDict = yield scrapy.Request(
            url = taster_link, callback=self.parseProfilePage, 
            meta = {
                'review': result
            }
        )
