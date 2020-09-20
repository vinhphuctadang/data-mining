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


# get data types:
print('Data type of points:', reviews.points.dtype)

stringPoints = reviews.points.astype('str')
print('Data to string:', stringPoints)

countNulls = reviews.price.isnull().sum() 
print('Number of null price:', countNulls)

region_values = reviews.region_1.fillna('Unknown').value_counts().sort_values(0, ascending=False)
print(region_values)
