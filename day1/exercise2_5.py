import pandas as pd

configs = {
    "local": {
        "url": "./winemag-data-130k-v2.csv",
    },
    "remote": {
        "url": "https://raw.githubusercontent.com/ltdaovn/dataset/master/wine-reviews/winemag-data-130k-v2.csv"
    }
}
config = configs["local"]
# disable certificate check

#
# pip install certifi
# /Applications/Python\ 3.6/Install\ Certificates.command
#

print('Loading data...')
reviews = pd.read_csv(
    config["url"], 
    index_col=0,
)


print('Changing column names...')
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'local'})
print(renamed)

print('ReIndexing to "wine"')
reindexed = reviews.rename_axis('wines', axis='rows')
print(reindexed)

# TODO: Other 2 examples are about joining 2 database; you should do this laterly