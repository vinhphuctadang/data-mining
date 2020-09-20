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

# print('Sample handles:', reviews.taster_twitter_handle.iloc[:100])
taster_twitter_handles = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print('Handles and review counts: \n', taster_twitter_handles)

best_rating_per_price = reviews.groupby('price').points.max().sort_index()
print('Best rating per price:\n', best_rating_per_price)

min_max_price_of_variety = reviews.groupby('variety').price.agg([min, max]) # TODO: Explore this and try another aggregation
print('Min-max variety:\n', min_max_price_of_variety)

# most expensive price of all varieties
sorted_price = min_max_price_of_variety.sort_values(by=['min', 'max'], ascending=False) # descending
print(sorted_price)

# taster average score
avgScore = reviews.groupby('taster_name').points.mean().sort_values(0, ascending=True)
print(avgScore)

print('Describe the avgScore: ', avgScore.describe()) 
# Output:
# Describe the avgScore:  count    19.000000
# mean     88.233026
# std       1.243610
# min      85.855422
# 25%      87.323501
# 50%      88.536235
# 75%      88.975256
# max      90.562551

# group contry and variety
contryVariety = reviews.groupby(['country', 'variety']).size().sort_values(0, ascending=False)
# .count(): sum the count of objects
# .size(): count number of objects get grouped
print(contryVariety)