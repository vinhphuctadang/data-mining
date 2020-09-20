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

# header
print('Data overview:')
print(reviews.head())

# all columns
print('Data columns:')
print(reviews.columns)

print('Description:')
desc = reviews.description
print(desc)

# first description
first_description = desc[0]
print('First description:', first_description)

first_descriptions = desc[:10]
print('First 10 descriptions:\n', first_descriptions, sep='')

sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
print('Sample reviews:\n', sample_reviews)


cols = ['country', 'province', 'region_1', 'region_2']
df = reviews.loc[[0, 1, 10, 100]][ cols]
print('New table:\n', df, sep='')

df = reviews.loc[0:99, ['country', 'variety']]
print('New table with country and variety:\n', df)


italian_wines = reviews[reviews["country"] == "Italy"]
print(italian_wines)

# cannot do like this:
# top_oceania_wines = reviews[(reviews["country"] == "Australia" | reviews["country"] == "New Zealand") & reviews["points"] >= 95]
# but this
top_oceania_wines = reviews[reviews["country"].isin(["Australia", "New Zealand"]) & (reviews["points"] >= 95)]
print(top_oceania_wines)