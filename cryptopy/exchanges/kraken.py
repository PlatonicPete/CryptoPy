import Exchange

####   Kraken info   ######
#
# -Kraken API is a http api
# -Kraken returns data in JSON format


class Kraken(Exchange):
    
    base_url = "https://api.kraken.com/0/"
    
    def get_pair():
        pass
