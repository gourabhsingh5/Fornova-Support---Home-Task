#!/usr/bin/env python
# coding: utf-8

import requests
import math
from pprint import pprint
import pandas as pd


# for getting 25 hotel IDs

url = "https://www.qantas.com/hotels/api/ui/locations/London,%20England,%20United%20Kingdom/availability?checkIn=2024-08-03&checkOut=2024-08-05&adults=2&children=0&infants=0&sortBy=popularity&propertyTypes=&facilities=&subRegions=&limit=25&payWith=cash&page=2"
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
  'cookie': 'pbe_user_id=ea0aebd5-bf82-4fbc-857a-417ea081628c; qh_user_id=bf15eca5-d244-4069-88c8-523136305847; qantas_isDevice=type^#desktop|os^#Windows NT; optimizelyEndUserId=oeu1722229679206r0.11646333370833961; _hjSessionUser_1001219=eyJpZCI6IjY1N2FlNGY5LTI2OTMtNWZhNi05MDZlLTY5MTQwNDQ1M2U1MiIsImNyZWF0ZWQiOjE3MjIyMjk2OTEzNjcsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1711787642.1722229692; _gcl_au=1.1.961780450.1722229692; _y2=1%3AeyJjIjp7IjI1NDA4MCI6MjQ4MzAxNzU0fX0%3D%3ANjQyNTY2MDQ4%3A99; AKA_A2=A; bm_ss=ab8e18ef4e; _abck=A79ED486EEE51E59C4A5BC54F606F111~0~YAAQrI0sMQIjXgGRAQAAredHAgx/G2OnemUbC4+4UViNCoOCTnA5gN+yH4YjOqoipKrAjXhWin7ri2enWzyQorD7PZXC+U+ZpZoK+SHVHpyIuvzcxClV+Ueed+hqAeTVLFvxrxVpccV0sz3Uyl5moBJavuiqOoGHEVehT4i7WIO2q6ifZl4GMVxLnIgy5ak8NX4v6nD5jFnR+m/Wr6FS4CMsnFyYM/dZSL8O4+6JRXn/XuWo6DT/86K6NEc1lDPXE1IUng84XgveqiwnqnfnEIBSpjqG+ebZnrfBWEmTnCkJENNSlQGaG5WAYuj6WKysAd3bxqbZx4/FH65pZ6sQ1eIF3o8aL5rTwd116G3V2enw7pB9kKhQ7yhqjOHtqzQdw2i87F4Vur7XwXp4BEHCDL2qkKaax8YF~-1~-1~-1; initalReferrerHotels=; qtspersisted=_f77dc3521ab54b5f86c47742458edbb9a753692abc39406b9c1cb8e1873662e8_b93cc020b21349f29d3bfe8c88721f42_1722229702289_45035996276881129_1722320155634_5; _hjSession_1001219=eyJpZCI6ImQxMThmNDdjLTYyNTEtNDVkNS1iNzk4LTNmM2VkMjU2MmMyYyIsImMiOjE3MjIzMjAxNTcxMjUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga=GA1.2.265119221.1722229688; _gat_UA-32359880-1=1; _gat_UA-259752839-1=1; qtssession=45035996276881129_1722320219026_1722320155634_2028_9847d5958cde454eb9bf9bcf54dc9593; _yi=1%3AeyJsaSI6eyJjIjowLCJjb2wiOjI5NzgzMjk1MDAsImNwZyI6MjU0MDgwLCJjcGkiOjkyMzI4MjE0NTAxLCJzYyI6NCwidHMiOjE3MjIyODU3NTQwNTJ9LCJzZSI6eyJjIjo1LCJlYyI6NiwibGEiOjE3MjIzMjAyMzMyNzQsInAiOjEsInNjIjo3M30sInUiOnsiaWQiOiI4MTQ2ZTMxYS05ZGU5LTRhNWMtODk1Zi00ZWVlZTExYTQ2ZGEiLCJmbCI6IjAifX0%3D%3ALTE4MDY5MDc0ODg%3D%3A99; bm_mi=5DAE840BCA0F077464E86735AECBC529~YAAQrI0sMUlEXgGRAQAAH0hJAhgr6nmSRd/ubCnBXn8V3Dnq2iv/ZsR1WVCg+uSg/D4fygGWRdhiLEy7asQpNNpSSOschGNwHY0qMRlTJVdTZ5Ih8r9PMDp4rrBkd4k9iuyBVJ/tipdR0jnlK2LgNKo/en6pJbpG621cfhYbbS2w6XzjyLCp+uoc/+bIrzDJdLTqxRHqbYD0R6f5i2s2LtmZXqPnZY/rO9jM2FHtHB6RSpYE00MRKi+BCfOJ6I/8/UXbJviBkSxUvYxqwP1EZ5RykVI8pVdIi0rCaNMROoaCrlbmj92IOvL51ndZrIfMKBoW4DBey79285efgaeB1ebwIap1~1; bm_sz=1E6079346337A5ECB0BDFC8D0571FF4D~YAAQrI0sMUxEXgGRAQAAH0hJAhiT2FrnDnk6d/KLJzn9h+eByvyDTcEeaFF3LreRNXJosqsuVhPPv8M/EGhPZGkM1KRw0dIPluMROtje7WZ/IVRlSt9kNtDikxevFY0S0dAIh8MIbcNdLI0ao23Sil6aGXrTR2VL1pVpj0WgtI9BA5QkKUppyMwNUzUSMjIBV11Pqs6623h3jtsFmKW4+x5D0tR14uR39JITFEBJMUU6i6L/FLxN6kUb+5mkjSKQsq0Z+p8sHPzW/bOaQLT9FBf5gBvQzQ0dXJqfvg3TpRO0w+y6s8XqvzFbm6sQmfeSO9uRzPM34aVtkF0wIVfE/EA/Yw3Ui1CaztB2tAKKi1GzQDGBWe52uBbmOdniDrZ4arXCyNl7zcuoZoLEYZEgG2RkQohENgsRog==~4404034~4473667; RT="z=1&dm=www.qantas.com&si=c2669558-4160-48ec-bbc7-5b848a4e8304&ss=lz80xx9m&sl=b&tt=k51&bcn=%2F%2F684d0d4a.akstat.io%2F&ld=1uwa&ul=201q&hd=20sv"; _ga_2JVDJ9RW0S=GS1.1.1722320153.6.1.1722320234.60.0.0; ak_bmsc=9DA1CFDBC79FF8BD89CFCA8A74E8FB55~000000000000000000000000000000~YAAQrI0sMY5EXgGRAQAAEkpJAhjuF7HmmttzRBY1fXYhgU/Keo1hZJXbre0OJbaBeCv1SGb7p7zDLVSIzMu4PwIl7NIa8130PUkcxQxPRflQM0g2DvmlLQCxWBd4PWqcaRdDY7HQk7ncx1h3mJMY/A25LjX5391l6R6dT+fqpSZa2LSGqiqrA2bl5uCfzLszEjJF8Ek/AXbtniMqgjmu5AEVz0QFfsP2l+sKW3TjOHGnj376rN9qC7qdVkdhTYgn6diveHnk+U8pyxWrK3qsuaLf2kEcBmxJoHCcs9o9OXNgD5smyXZn136OIv0Y9/5NQgSg6uIjTNu60b1ozoXcDYOIoAN277WfHzSwMjY7I9wzIkdj8hVsiTdRI9vhoQtuSHwy9aSMS0k0rsLkex6A07MiV73kY16JmEziSEgx4rzAKb8wTbiRzpaNjiLdIswa6LCH6Ws0QDQ3CnXQ8cZULtCg4DHYKFMC8c6Z87kPAeNxKNYUy5cKDdAcHg==; bm_s=YAAQrI0sMalEXgGRAQAAzEpJAgGeoU4VF7x+94J19EMZHwwLcpk1E01G8VyRiJQrUEaXAzqDANbmlX07BcF/83hwoYSwVtgvRi/Izij7jaTCN/5LB+3peLZtlWwAB7nAt/+4IE9x8Fws/4Z6WqComvAWoog6ncpMpOq3WsfSVxHlu+8GZK0NC3luuy51vMUFw2T8N7KDj/1se/ttISdMoKsEzguSZyiapF5VPqXZmgji1tUi0DOtl6IGCUxvQ8ZwmoKU5+MJmlUlKhOy+/iETxwlNKX5HPCNSrEZcuL/7zuhGVdJ48megzCBkljTO/rj0QWqImO7kVidbI0ebDs5H0XvgENQvg==; bm_sv=CEBA9C6F1894ABC63F90111B582352AD~YAAQrI0sMapEXgGRAQAAzEpJAhgHKWYeufgQlBwy0077Gd5sAkBEeRIqEjlxKj5hTYxsZ4wK7uL/BSNKxAC1TOckFcTaGYneOBYf5CP3wXnojgzgwDZIKOZLGbyssyj+5lhUCBUKtQijSRfnSoz30ukR0KjE85nuuCjt5v/Nah9W+gdF9CUV2ig3Vkbzomoa+7PAnzDnHwqqAhN0gyYwSZSYWQ8bcWzqcdY9zsGD2PlvjQcFWUH8Y/BdP5bHlF5xnA==~1; _abck=A79ED486EEE51E59C4A5BC54F606F111~-1~YAAQ3o0sMQtt6wKRAQAAuK7qBwwNmxFPEZfCnVpscFEl1WFTVXHdG8N1IgrQESnGcNbk6sRrMa5uB0V76ruhtEAznljTwIKrePwxxg+uNwyqTycRrBdPw4RWdxInSt8a7V1PqZuYkhJR9DSqYQvtJiVuKGlzHsI0fXb7ePXksu4YyOyDCZDOhEs+Doq98eNFWkNB0TFUYeunPBFZ9TTtFoUwEt4dPL4XQc2A+cRxXdqXpBtTHxlAjdH/Nww72IVa7yfy0stSG/ZYJhd8pz2UNyfPgH3xtUC8aqfw8BZ4xV+RrUvQcjh+drfiyY3vhQrwnYT3/fxrAMWKj9e7gEqhakOWVEs2xlv6XdsNLJK5/xSOC3/eQyW+ygD2CUGliw==~0~-1~-1; bm_s=YAAQrI0sMTf7XgGRAQAAdaBQAgFn2ecffjL9a5sGZCIL6b6Ky/4JXt8a7NIcEbbebUidTHdB70DOMdGEjKFKQxHjceuMngcd7PDo9sKHnjMlpOoIbxLpIJgu+3OQ1XbdA8YwpWpa9635YD93LTqoVtvd58kxYxFQvZOip8tyYWL1XuHSYqB0tppnvtlmOTJMcLrxJlIO0sTcNYYW07Sf+2vbEe4CfQXNq0m77K3VX9jmJb71pI3TiUyiKl3mB43QT3tUkkkZRSBmiYVKn+KL5p0EKMjIgiafnHUX09k4pOetzybK0GFns+zf2wQ30kSkpbpvLjC8cXepY+lRK4pldz/9oILibg==; usercontext=region#AS|country#IN|locale#en|dep#BOM',
  'if-none-match': 'W/"1c576-PdPkPW3jXe5pNfbffBGYrO0JI3U"',
  'priority': 'u=1, i',
  'qh-meta': '{"qhUserId":"bf15eca5-d244-4069-88c8-523136305847"}',
  'referer': 'https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2024-08-13&checkOut=2024-08-14&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'd5de18dfc2af4aa0b7c0c9efd8e32579-821d5b6e8ad3b06e-1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
response = requests.request("GET", url, headers=headers)


id_data=response.json()

hotel_ids=[]
for ids in id_data['results']:
    hotel_ids.append(ids['property']['id'])


# for getting combination of 25 random checkin- checkout dates


import random
from datetime import datetime, timedelta

def generate_random_dates_for_aug_sept(start_date, end_date, num_pairs):
    date_pairs = []
    days_between_dates = (end_date - start_date).days

    for _ in range(num_pairs):
        random_days_for_checkin = random.randint(0, days_between_dates)
        checkin_date = start_date + timedelta(days=random_days_for_checkin)
        checkout_duration = random.randint(2, 3)
        checkout_date = checkin_date + timedelta(days=checkout_duration)
        if checkout_date > end_date:
            checkout_date = end_date
        date_pairs.append((checkin_date, checkout_date))
    return date_pairs

start_date = datetime(2024, 8, 1)
end_date = datetime(2024, 9, 30)

random_date_pairs = generate_random_dates_for_aug_sept(start_date, end_date, 25)
checkin_date=[]
checkout_date=[]

for i, (checkin, checkout) in enumerate(random_date_pairs, start=1):
    checkin_date.append(checkin.strftime('%Y-%m-%d'))
    checkout_date.append(checkout.strftime('%Y-%m-%d'))


# Exctract data and write to CSV function


def extract_data(data):
    rates=[]
    count=0
    for rooms in data['roomTypes']:
        for d in rooms['offers']:
            count+=1
            rate_info = {
            'Room_name': rooms['name'],
            'Rate_name': d['description'],
            'Number of Guests': int(data['meta']['query']['children'])+int(data['meta']['query']['infants'])+int(data['meta']['query']['adults']),
            'Cancellation Policy': 'Non-refundable' if d['cancellationPolicy']['isNonrefundable'] else d['cancellationPolicy']['description'],
            'Price': math.ceil(float(d['charges']['total']['amount'])),
            'Currency': d['charges']['total']['currency'],
            'Top Deal': True if d['promotion'] else False
            }
            rates.append(rate_info)
    rates={data['id']:rates}
    pprint(rates)
    json_data={
        "hotel_id":data['id'],
        "check-in":str(data['meta']['query']['checkIn']),
        "check-out":str(data['meta']['query']['checkOut']),
        "rates":rates
    }
    df = pd.DataFrame([json_data])
    df.to_csv(r"C:\Users\goura\Downloads\output.csv", index=False, header=None, mode='a')
    


# calling API 25 times for hotels with checkin/ checkout dates and passing ot to function created above


for id,checkIn,checkOut in zip(hotel_ids, checkin_date, checkout_date):
    url = f"https://www.qantas.com/hotels/api/ui/properties/{id}/availability?checkIn={checkIn}&checkOut={checkOut}&adults=2&children=0&infants=0&payWith=cash"
    response = requests.request("GET", url, headers=headers)
    extract_data(response.json())


# in order to add header to CSV file


df1=pd.read_csv(r"C:\Users\goura\Downloads\output.csv", header=None)
df1.columns=['hotel_id','check-in', 'check-out', 'rates']
df1.to_csv(r"C:\Users\goura\Downloads\output.csv", index=False)
