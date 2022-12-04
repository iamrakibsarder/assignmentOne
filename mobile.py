mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
phone_name = mobile_data.get('data')[0].get('name')
country = mobile_data.get('data')[0].get('made')
price = mobile_data.get('data')[0].get('price')
exchange_rate = mobile_data.get('exchnage_rate')
splitted_price = mobile_data.get('data')[0].get('price').split()
bdt = int(splitted_price[0]) * exchange_rate



description = f"{phone_name} is one of the Best phone in the market. It is made in {country}. It's price is about {price} which is {bdt} in Bangladeshi Taka"

print(description)


