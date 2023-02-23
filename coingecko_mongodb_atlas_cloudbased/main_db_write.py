from coingecko_data_source.gecko_api import Gecko_API
from mongodb_atlas_cloudbased.mongodb_cloudbased import DB

# Classes initialization
source_api = Gecko_API()
db = DB()
db._add_db("assets_data")
db._add_collection("test_collection")

# get real-time price of a crypto asset
simple = source_api.simple_price("bitcoin", "usd")

# add data to the DB
db._add_post(simple)
print('Data added in Atlas MongoDB')