# structure
# country,description,designation,points,
# price,province,region_1,region_2,taster_name,
# taster_twitter_handle,title,variety,winery
import scrapy
import json

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
count = 0

def isFloat(x):
    try: 
        float(x)
    except:
        return False 
    return True

def writeHeader(file, header):
    file.write('%s\n' % ','.join(header))

def writeData(file, header, data):
    values = [str(count)]
    for field in header:
        if field == '':
            continue
        value = data.get(field, '')
        values.append(json.dumps(value))
    file.write('%s\n' % ','.join(values))

with open('wine.csv', 'w') as f:
    writeHeader(f, header)
    writeData(f, header, sample)