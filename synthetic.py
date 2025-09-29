import random
from faker import Faker

fake = Faker()
coupon_codes = [
    "SAVE10", "FREESHIP", "WELCOME20", "HOLIDAY15", "SPRINGSALE"
]
shipping_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]
customer_ids = list(range(101, 1000))

for i in range(1000):
    customer_id = random.choice(customer_ids)
    coupon_code = random.choice(coupon_codes)
    shipping_city = random.choice(shipping_cities)
    # output in neondb format
    print(f"INSERT INTO customers (customer_id, coupon_code, shipping_city) VALUES ({customer_id}, '{coupon_code}', '{shipping_city}');")
    #print(f"{customer_id},{coupon_code},{shipping_city}")

