
import urllib
import json

import urllib.request with urllib.request.urlopen("https://graph.facebook.com/fql?q=SELECT%20post_id,%20actor_id,%20message%20FROM%20stream%20WHERE%20filter_key%20=%20%27others%27%20AND%20source_id%20=%20me()%20LIMIT%20100&access_token=CAACEdEose0cBADqpwvCl6uqZANWLTplfvp1zLciLKWY2ZCdZAPZA4VyeFEQu9YZCThOZCvTfV3udcDf8ZCzsgZBr8JYFpjc6fxn2kZApxLgwC4ZCulqJasIlv1rBhZA8WcBZA4zmafvjZA6kUr5cwLyaiDhL0yhjj9nvWJrYOUMCcnomsGEtjgHX8bncV7o1OwvJh7kmZCh9sSaER0ZAgZDZD") as url:

i=0
for item in data["data"]:
    print(i)
    print(item['message'])
    i=i+1
