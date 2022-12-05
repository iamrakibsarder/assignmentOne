import random

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

first_sentence = [
    f'{phone_name} is one of the Best phone in the market',
    f'{phone_name} is the latest model of Xiaomi',
    f'The phone that comes with great display and camera is {phone_name}'
]
second_sentence = [
    f'It is made in {country}',
    f'{country} made this Awesome phone',
    f'{country} is the place where it made'
]
third_sentence = [
    f"It's price is about {price} which is {bdt} in Bangladeshi Taka",
    f'The phone costs {price} or {bdt} Taka',
    f'One need to have {price} or {bdt} Bangladeshi Taka to purchase the phone'
]
randomChoice1 = random.choice(first_sentence)
randomChoice2 = random.choice(second_sentence)
randomChoice3 = random.choice(third_sentence)
sentence = f'{randomChoice1}. {randomChoice2}. {randomChoice3}'

# description = f"{phone_name} is one of the Best phone in the market. It is made in {country}. It's price is about {price} which is {bdt} in Bangladeshi Taka"

print(sentence)


