import json
import os
import django
from products.models import Product

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booknook.settings')
django.setup()

# Path to the book fixtures file
fixtures_path = os.path.join('products', 'fixtures', 'books.json')

# Load the fixtures
with open(fixtures_path, 'r', encoding='utf-8') as f:
    books_data = json.load(f)

# Iterate over each book entry and create the corresponding product
# if it doesn't exist
for book in books_data:
    fields = book['fields']
    product, created = Product.objects.get_or_create(
        id=book['pk'],
        defaults={
            'name': fields['name'],
            'friendly_name': fields['friendly_name'],
            'slug': fields['slug'],
            'description': fields['description'],
            'price': fields['price'],
            'rating': fields.get('rating', None),
            'image': fields.get('image', None),
            'img_url': fields.get('img_url', None),
            'created_at': fields['created_at'],
            'updated_at': fields['updated_at'],
        }
    )
    if created:
        print(f"Created Product: {product.id} - {product.name}")
    else:
        print(f"Product already exists: {product.id} - {product.name}")

print("All products created or verified.")
