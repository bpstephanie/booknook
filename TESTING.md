* [**Testing Contents**](<#testing-contents>)
  * [Validator Testing](<#validator-testing>)
    * [HTML](<#html>)
    * [CSS](<#css>)
    * [Python and Django](<#python-and-django>)
    * [JavaScript](<#javascript>)
  * [Lighthouse](<#lighthouse>)
  * [Browser Compatibility](<#browser-compatibility>)
  * [Manual Testing](<#manual-testing>)
  * [Automated Testing](<#automated-testing>)
  * [Testing User Stories](<#testing-user-stories>)
  * [Additional Testing](<#additional-testing>)
    * [Wave](<#wave>)
    * [Responsiveness Testing](<#responsiveness-testing>)
  * [Known Bugs](<#known-bugs>)
    * [Unresolved Bugs](<#unresolved-bugs>)

# Validator Testing

## HTML

The [HTML W3C Validator] was used to validate all HTML files. The results are as follows:
|**Filename**|**Image**|**Pass/Fail**|
|------------|---------|-------------|
|index.html|![Homepage](documentation/screenshots/validation/index-html.png)|Pass|
|products.html|![Products Page](documentation/screenshots/validation/products-html.png)|Pass|
|product_detail.html|![Product Detail](documentation/screenshots/validation/product-detail-html.png)|Pass|
|all_genres.html|[Books by Genre](documentation/screenshots/validation/all-genres-html.png)|Pass|
|all_categories.html|[Accessories by Category](documentation/screenshots/validation/all-categories-html.png)|Pass|
|product_management.html|||
|edit_book.html|||
|edit_accessory.html|||
|about.html|![About](documentation/screenshots/validation/about.html)|Pass|
|contact.html|![Contact Us Page](documentation/screenshots/validation/contact-html.png)|Pass|
|contact_success.html|![Contact Us Success](documentation/screenshots/validation/contact-success-html.png)|Pass|
|faqs.html|![FAQs](documentation/screenshots/validation/faqs-html.png)||
|partners.html|![Partners](documentation/screenshots/validation/partners-html.png)|Pass|
|privacy_policy.html|![Privacy Policy Page](documentation/screenshots/validation/privacy-policy-html.png)|Pass|
|forum.html|![Forum](documentation/screenshots/validation/forum-html.png)|Pass|
|post_list.html|[Full Thread Page](documentation/screenshots/validation/post-list-html.png)|Pass|
|edit_thread.html|
|edit_post.html|||
|bag.html|![Bag](documentation/screenshots/validation/bag-html.png)|Pass|
|checkout.html|![Checkout](documentation/screenshots/validation/checkout-html.png)|Pass|
|checkout_success.html|![Checkout](documentation/screenshots/validation/checkout-success-html.png)|Pass|
|profile.html|||
|downloads.html|||

## CSS
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate all css file. The results are below:

|**Filename**|**Image**|**Pass/Fail**|
|------------|---------|-------------|
|base.css|![base.css](documentation/screenshots/validation/base-css.png)|Pass|
|forum.css|![forum.css](documentation/screenshots/validation/forum-css.png)|Pass|
|profiles.css|![Models](documentation/screenshots/validation/profile-css.png)|Pass|

## Python and Django
The CI Python Linter Validator was used to validate all python files which I created or edited. I corrected mistakes as I went with the VS Code Problems tab.

  | **App**     |   **Models**  |   **Urls**  |   **views**  |**Bag Tools**  | **Contexts**  | **Pass/Fail**  |
  |-------------|---------------|-------------|--------------|---------------|---------------|---------------|
  | **bag**     |![Models](documentation/screenshots/validation/bag-models.png)|![Urls](documentation/screenshots/validation/bag-models.png)|![Views](documentation/screenshots/validation/bag-views.png)|![Bag-Tools](documentation/screenshots/validation/bag-bagtools.png)|![Contexts](documentation/screenshots/validation/bag-contexts.png)| All Pass  |

  | **App**     |   **Urls**  |   **Views**  |   **Settings** |  **Pass/Fail** |
  |-------------|-------------|--------------|----------------|----------------|
  | **booknook**|![Urls](documentation/screenshots/validation/booknook-urls.png)|![Views](documentation/screenshots/validation/booknook-views.png)|![Settings](documentation/screenshots/validation/booknook-settings.png)| All Pass  |


  | **App**|   **Admin**  |   **Forms**  |   **Models**  |   **Signals**  | **Urls**   | **Views**  | **Webhook Handler**  | **Webhooks** | **Pass/Fail**  |
  |--------|--------------|--------------|---------------|----------------|------------|------------|----------------------|---------|-----------|
  | **checkout**   |![Admin](documentation/screenshots/validation/checkout-admin.png)|![Forms](documentation/screenshots/validation/checkout-forms.png)|![Models](documentation/screenshots/validation/checkout-models.png)|![Signals](documentation/screenshots/validation/checkout-signals.png)|![Urls](documentation/screenshots/validation/checkout-urls.png)|![Views](documentation/screenshots/validation/checkout-views.png)|![WebHook Handler](documentation/screenshots/validation/checkout-webhookhandler.png)|![WebHooks](documentation/screenshots/validation/checkout-webhooks.png)| All Pass |


  | **App**     |   **Admin**  |   **Forms**  |   **Models**  | **Urls**   | **Views**  | **Pass/Fail**  |
  |-------------|--------------|--------------|---------------|------------|------------|----------------|
  | **forum**   |![Admin](documentation/screenshots/validation/forum-admin.png)|![Forms](documentation/screenshots/validation/forum-forms.png)|![Models](documentation/screenshots/validation/forum-models.png)|![Urls](documentation/screenshots/validation/forum-urls.png)|![Views](documentation/screenshots/validation/forum-views.png)| All Pass  |


  | **App**     |   **Admin**  |   **Forms**  |   **Models**  | **Urls**   | **Views**  | **Pass/Fail**  |
  |-------------|--------------|--------------|---------------|------------|------------|----------------|
  | **home**    |![Admin](documentation/screenshots/validation/home-admin.png)|![Forms](documentation/screenshots/validation/home-forms.png)|![Models](documentation/screenshots/validation/home-models.png)|![Urls](documentation/screenshots/validation/home-urls.png)|![Views](documentation/screenshots/validation/home-views.png)| All Pass  |

  | **App**     |   **Admin**  |   **Forms**  |   **Models**  | **Urls**   | **views**  | **Pass/Fail**  |
  |-------------|--------------|--------------|---------------|------------|------------|----------------|
  | **info**    |![Admin](documentation/screenshots/validation/info-admin.png)|![Forms](documentation/screenshots/validation/info-forms.png)|![Models](documentation/screenshots/validation/info-models.png)|![Urls](documentation/screenshots/validation/info-urls.png)|![Views](documentation/screenshots/validation/info-views.png)| All Pass  |


  | **App**     |   **Admin**  |   **Forms**  |   **Models**  | **Urls**   | **Views**  | **Widgets** | **Pass/Fail**  |
  |-------------|--------------|--------------|---------------|------------|------------|-------------|----------------|
  | **products**|![Admin](documentation/screenshots/validation/products-admin.png)|![Forms](documentation/screenshots/validation/products-forms.png)|![Models](documentation/screenshots/validation/products-models.png)|![Urls](documentation/screenshots/validation/products-urls.png)|![Views](documentation/screenshots/validation/products-views.png)|![Widgets](documentation/screenshots/validation/products-widgets.png)| All Pass  |


  | **App**     |   **Admin**  | **Apps**|   **Forms**  | **Models**  | **Signals** | **Urls**   | **Views**  | **Pass/Fail**  |
  |-------------|--------------|---------|--------------|-------------|-------------|------------|------------|----------------|
  | **profiles**|![Admin](documentation/screenshots/validation/profiles-admin.png)|![Apps](documentation/screenshots/validation/profiles-apps.png)|![Forms](documentation/screenshots/validation/profiles-forms.png)|![Models](documentation/screenshots/validation/profiles-models.png)|![Signals](documentation/screenshots/validation/profiles-signals.png)|![Urls](documentation/screenshots/validation/profiles-urls.png)|![Views](documentation/screenshots/validation/profiles-views.png)| All Pass  |


  | **App**     |   **Admin**  |   **Forms**  | **Models**  | **Urls**   | **Views**  | **Pass/Fail**  |
  |-------------|--------------|--------------|-------------|------------|------------|----------------|
  | **wishlist**|![Admin](documentation/screenshots/validation/wishlist-admin.png)|![Forms](documentation/screenshots/validation/wishlist-forms.png)|![Models](documentation/screenshots/validation/wishlist-models.png)|![Urls](documentation/screenshots/validation/wishlist-urls.png)|![Views](documentation/screenshots/validation/wishlist-views.png)| All Pass  |


  Root Level Python Files

  |**Filename**              | **Image**                   | **Pass/Fail** |
  |--------------------------|-----------------------------|---------------|
  |Create Products From Books|![Create Products From Books](documentation/screenshots/validation/create-products-from-books.png)| Pass|
  |Custom Storages|![Custom Storages](documentation/screenshots/validation/custom-storages.png)| Pass|
  |Download Images|![Download Images](documentation/screenshots/validation/download-images.png)|Pass|
  |Update product|![Update Product](documentation/screenshots/validation/update-product.png)|Pass|


  ## JavaScript

  [JS Hint]() was used to validate JavaScript code.

  |**Page**|**Image**|**Pass/Fail**|

  |all_categories.html|![All Categories JS](documentation/screenshots/validation/all-categories-js.png)|Pass|

  |all_genres.html|![All Genres JS](documentation/screenshots/validation/all-genres-js.png)|Pass|
  |bag.html|![Bag JS](documentation/screenshots/validation/bag-js.png)|Pass|
  |countryfield.js|![Country Field JS](documentation/screenshots/validation/country-field-js.png)|Pass|
  |edit_accessory.html|![Edit Accessory JS](documentation/screenshots/validation/edit-accessory-js.png)|Pass|
  |edit_book.html|![Edit Book JS](documentation/screenshots/validation/edit-book-js.png)|Pass|
  |forum.html|![Forum JS](documentation/screenshots/validation/forum-js.png)|Pass|
  |post_list.html|![Post List JS](documentation/screenshots/validation/post-list-js.png)|Pass|
  |product_detail.html|![Product Detail JS](documentation/screenshots/validation/product-detail-js.png)|Pass|
  |product_management.html|![Product Management JS](documentation/screenshots/validation/product-management-js.png)|Pass|
  |products.html|![Products JS](documentation/screenshots/validation/products-js.png)|Pass|
  |profile.html|![Profile JS](documentation/screenshots/validation/profile-js.png)|Pass|
  |quantity_input_script.html|![Quantity Input Script JS](documentation/screenshots/validation/quantity-input-script-js.png)|Pass|
  |stripe_elements.js|![Stripe Elements JS](documentation/screenshots/validation/stripe-elements-js.png)| Pass|
  |wishlist_modal_script.html|![Wishlist Modal Script JS](documentation/screenshots/validation/wishlist-modal-script-js.png)
