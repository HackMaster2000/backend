from app.models import Product
from app.products import products

def insertProducts():
    for product in products:
        p = Product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            stock=product['stock'],
            image=product['image'],
        )
        p.save()