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

print('Median of points:', reviews.points.median())

print('Countries:', reviews.country.unique())

reviews_per_country = reviews.country.value_counts
print('Value count:', reviews_per_country)

# what is this for ???
# Centering simply means subtracting a constant from every value of a variable
centered_price = reviews.price - reviews.price.mean()
print('Center prices:', centered_price)

bargain = reviews.points / reviews.price
idMax = bargain.idxmax() # argmax in numpy

print('Bargain max:\n', reviews.loc[idMax, ["title"]])
# stat description

tropical = reviews.description.map(lambda x: 'tropical' in x).sum()
fruity    = reviews.description.map(lambda x: 'fruity' in x).sum()
# descriptor_counts = pd.Series([tropical, fruit], index=['tropical', 'fruity'])
# print('Descriptor counts:\n', descriptor_counts)
# we can do this way
meta = {
    'tropical': [tropical],
    'fruit': [fruity]   
}
df = pd.DataFrame(meta)
print('Fruit and tropical:', df)

# stars
reviews.apply(lambda row: (3 if row.country=='Canada' or row.points >= 95 else 2 if row.points >= 95 else 1), axis='columns')
print(reviews)