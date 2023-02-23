from mongodb_atlas_cloudbased.mongodb_cloudbased import DB
from pprint import pprint


#########################################################################
################### MongoDB based on Atlas cloud ########################
######################################################################### 
# Class initialization
db = DB()
db._add_db("assets_data")
db._add_collection("test_collection")

# read data from DB
posts = db.collection.find_one( { "bitcoin" : { "$exists" : 1 } } )
pprint(posts["bitcoin"])
