# Data Team Testing
A testing repo for the data team of DeFiLib.

# Possible data architectures

## Data source APIs list
| API | PROS | CONS |
| :------------ |:---------------:| -----:|
| Coingecko | keyless, no restriction but attribution is required (gecko logo) | 10-30 calls per minute |
| CoinMarketCap |   | No historical data, Personal use restriction |
| Coinapi.io  | OHLCV (Open, High, Low, Close, Volume) timeseries data, extensive docs | 100 daily requests |

## DB
| DB | PROS | CONS |
| :------------ |:---------------:| -----:|
| Cloud-based | scalable | money |
| Local Stand-alone | free | user installation |
| Local embedded | free, easy | small/medium size projects |

### DB Cloud-based
Oracle: \
MongoDB instance on Atlas cloud: it needs an account or a certificate.

### DB Local Stand-alone
MongoDB: it needs a local installation.
### DB Local embedded
Local DB with a maintened Python library: \
SQLite: well-known relational DB \
TinyDB: NOSQL document-oriented (JSON) \
ZODM: object-oriented, rigid data structure \

# First attempt
Data source API: CoinGecko \
DB: local embedded TinyDB \