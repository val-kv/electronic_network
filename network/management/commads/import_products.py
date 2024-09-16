import json
from network.models import Product

with open('electronics_network/products.json') as f:
    products = json.load(f)
for item in products:
    Product.objects.create(
        name=item['name'],
        price=item['price'],
        description=item['description']
    )
