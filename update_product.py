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

# Find the book with pk=1 and update the corresponding product
for book in books_data:
    if book['pk'] == 1:
        fields = book['fields']
        product = Product.objects.filter(id=1).update(
            name=fields['name'],
            friendly_name=fields['friendly_name'],
            slug=fields['slug'],
            description=fields['description'],
            price=fields['price'],
            rating=fields.get('rating', None),
            image=fields.get('image', None),
            img_url=fields.get('img_url', None),
            created_at=fields['created_at'],
            updated_at=fields['updated_at'],
        )
        print(f'Updated Product: {1} - {fields["name"]}')
        break

print("Product updated successfully.")
