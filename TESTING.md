# Testing Contents
* [**Testing Contents**](<#testing-contents>)
  * [Validator Testing](<#validator-testing>)
    * [HTML](<#html>)
    * [CSS](<#css>)
    * [Python and Django](<#python-and-django>)
    * [JavaScript](<#javascript>)
  * [Lighthouse](<#lighthouse>)
  * [Browser Compatibility](<#browser-compatibility>)
  * [Manual Testing](<#manual-testing>)
  * [User Story Testing](<#user-story-testing>)
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
|all_genres.html|![Books by Genre](documentation/screenshots/validation/all-genres-html.png)|Pass|
|all_categories.html|![Accessories by Category](documentation/screenshots/validation/all-categories-html.png)|Pass|
|product_management.html|![Product Management](documentation/screenshots/validation/product-management-html.png)|Pass|
|edit_book.html||[Edit Book Page](documentation/screenshots/validation/edit-book-html.png)|Fail|
|edit_accessory.html|[Edit Accessory Page](documentation/screenshots/validation/edit-accessory-html.png)|Fail|
|about.html|![About](documentation/screenshots/validation/about.html)|Pass|
|contact.html|![Contact Us Page](documentation/screenshots/validation/contact-html.png)|Pass|
|contact_success.html|![Contact Us Success](documentation/screenshots/validation/contact-success-html.png)|Pass|
|faqs.html|![FAQs](documentation/screenshots/validation/faqs-html.png)||
|partners.html|![Partners](documentation/screenshots/validation/partners-html.png)|Pass|
|privacy_policy.html|![Privacy Policy Page](documentation/screenshots/validation/privacy-policy-html.png)|Pass|
|forum.html|![Forum](documentation/screenshots/validation/forum-html.png)|Pass|
|post_list.html|[Full Thread Page](documentation/screenshots/validation/post-list-html.png)|Pass|
|edit_thread.html|![Edit Thread](documentation/screenshots/validation/edit-thread-html.png)|Pass|
|edit_post.html|![Edit Post](documentation/screenshots/validation/edit-post-html.png)|Pass|
|bag.html|![Bag](documentation/screenshots/validation/bag-html.png)|Pass|
|checkout.html|![Checkout](documentation/screenshots/validation/checkout-html.png)|Pass|
|checkout_success.html|![Checkout](documentation/screenshots/validation/checkout-success-html.png)|Pass|
|profile.html|||
|downloads.html|![Downloads](documentation/screenshots/validation/downloads-html.png)|Pass|


[Back To Top](<#testing-contents>)

## CSS
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate all css file. The results are below:

|**Filename**|**Image**|**Pass/Fail**|
|------------|---------|-------------|
|base.css|![base.css](documentation/screenshots/validation/base-css.png)|Pass|
|forum.css|![forum.css](documentation/screenshots/validation/forum-css.png)|Pass|
|profiles.css|![Models](documentation/screenshots/validation/profile-css.png)|Pass|


[Back To Top](<#testing-contents>)

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


[Back To Top](<#testing-contents>)
  
## JavaScript

  [JS Hint]() was used to validate JavaScript code.

  |**Page**     |**Image**         | **Pass/Fail** |
  |-------------|------------------|---------------|
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


[Back To Top](<#testing-contents>)

# Lighthouse testing

|**Page**|**Desktop**|**Mobile**|
|--------|-----------|----------|
|Homepage|![Homepage Desktop](documentation/screenshots/validation/lighthouse/homepage-desktop.png)|![Homepage Mobile](documentation/screenshots/validation/lighthouse/homepage-mobile.png)|
|All Products Page|![Products Desktop](documentation/screenshots/validation/lighthouse/products-desktop.png)|![Products Mobile](documentation/screenshots/validation/lighthouse/products-mobile.png)|
|All Genres Page|![All Genres Desktop](documentation/screenshots/validation/lighthouse/all-genres-desktop.png)|![All Genres Mobile](documentation/screenshots/validation/lighthouse/all-genres-mobile.png)|
|All Categories Page|![All Categories Desktop](documentation/screenshots/validation/lighthouse/all-categories-desktop.png)|![All Categories Mobile](documentation/screenshots/validation/lighthouse/all-categories-mobile.png)|
|Product Detail Page|![Product Detail Desktop](documentation/screenshots/validation/lighthouse/product-detail-desktop.png)|![Product Detail Mobile](documentation/screenshots/validation/lighthouse/product-detail-mobile.png)|
|Edit Book Page|![Edit Book Desktop](documentation/screenshots/validation/lighthouse/edit-book-desktop.png)|![Edit Book Mobile](documentation/screenshots/validation/lighthouse/edit-book-mobile.png)|
|Edit Accessory Page|![Edit Accessory Desktop](documentation/screenshots/validation/lighthouse/edit-accessory-desktop.png)|![Edit Accessory Mobile](documentation/screenshots/validation/lighthouse/edit-accessory-mobile.png)|
|Product Management Page|![Product Management Desktop](documentation/screenshots/validation/lighthouse/product-management-desktop.png)|![Product Management Mobile](documentation/screenshots/validation/lighthouse/product-management-mobile.png)|
|About Us Page|![About Us Desktop](documentation/screenshots/validation/lighthouse/about-desktop.png)|![About Us Mobile](documentation/screenshots/validation/lighthouse/about-mobile.png)|
|Contact Us Page|![Contact Us Desktop](documentation/screenshots/validation/lighthouse/contact-desktop.png)|![Contact Us Mobile](documentation/screenshots/validation/lighthouse/contact-mobile.png)|
|Contact Sucess Page|![Contact Success Desktop](documentation/screenshots/validation/lighthouse/contact-success-desktop.png)|![Contact Success Mobile](documentation/screenshots/validation/lighthouse/contact-success-mobile.png)|
|FAQs|![FAQs Desktop](documentation/screenshots/validation/lighthouse/faqs-desktop.png)|![FAQs Mobile](documentation/screenshots/validation/lighthouse/faqs=mobile.png)|
|Privacy Policy|![Privacy Policy Desktop](documentation/screenshots/validation/lighthouse/privacy-policy-desktop.png)|![Privacy Policy Mobile](documentation/screenshots/validation/lighthouse/privacy-policy-mobile.png)|
|Partners Page|![Partners Desktop](documentation/screenshots/validation/lighthouse/partners-desktop.png)|![Partners Mobile](documentation/screenshots/validation/lighthouse/partners-mobile.png)|
|Forum|![Forum Desktop](documentation/screenshots/validation/lighthouse/forum-desktop.png)|![Forum Mobile](documentation/screenshots/validation/lighthouse/forum-mobile.png)|
|Post List Page|![Post List Desktop]((documentation/screenshots/validation/lighthouse/post-list-desktop.png))|![Post List Mobile](documentation/screenshots/validation/lighthouse/post-list-mobile.png)|
|Profile Page|![Profile Desktop](documentation/screenshots/validation/lighthouse/profile-desktop.png)|![Profile Mobile](documentation/screenshots/validation/lighthouse/profile-mobile.png)|
|Bag|![Bag Desktop](documentation/screenshots/validation/lighthouse/bag-desktop.png)|![Bag Mobile](documentation/screenshots/validation/lighthouse/bag-mobile.png)|
|Checkout Page|![Checkout Desktop](documentation/screenshots/validation/lighthouse/checkout-desktop.png)|![Checkout Mobile](documentation/screenshots/validation/lighthouse/checkout-mobile2.png)|
|Checkout Success|![Checkout Success Desktop](documentation/screenshots/validation/lighthouse/checkout-success-desktop.png)|![Checkout Success Mobile](documentation/screenshots/validation/lighthouse/checkout-success-mobile.png)|
|Login|![Login Desktop](documentation/screenshots/validation/lighthouse/login-desktop.png)|![Login Mobile](documentation/screenshots/validation/lighthouse/login-mobile.png)|
|Logout|![Logout Desktop](documentation/screenshots/validation/lighthouse/logout-desktop.png)|![Logout Mobile](documentation/screenshots/validation/lighthouse/logout-mobile.png)|
|Register|![Register Desktop](documentation/screenshots/validation/lighthouse/register-desktop.png)|![Register Mobile](documentation/screenshots/validation/lighthouse/register-mobile.png)|
|Forgot Password|![Forgot Password Desktop](documentation/screenshots/validation/lighthouse/forgot-desktop.png)|![Forgot Password Mobile](documentation/screenshots/validation/lighthouse/forgot-mobile.png)|
|Change Password|![Change Password Desktop](documentation/screenshots/validation/lighthouse/change-password-desktop.png)|![Change Password Mobile](documentation/screenshots/validation/lighthouse/change-password-mobile.png)

On Chrome when auditing the 'Checkout' page for mobile - message appeared stating I should try in incognit mode. The results are below.
<details><summary>Checkout Mobile - Incognito Mode</summary>

![Checkout Mobile - Incognito Mode](documentation/screenshots/validation/lighthouse/checkout-mobile.png)

</details>

Best Practices should be higher, however it is lower due to the presence of third party cookies due to Stripe.


[Back To Top](<#testing-contents>)

# Browser Compatibility

[Back To Top](<#testing-contents>)

# Manual Testing
## Home Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|


## All Products Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|


## By Genre Page (All Genres)

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## By Category Page (All Categories)

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Product Detail

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Edit Book Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Edit Accessory Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Search

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## About Us Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Contact Us Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Contact Us Success Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## FAQs Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Privacy Policy Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Partners Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Forum

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Post List Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Profile Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Bag

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Checkout Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Checkout Success Page

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Login

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Logout

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Register

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|

## Forgot Password

|**User Action**|**Expected Result**|**Pass/Fail**|**Comments**|
|---------------|-------------------|-------------|------------|


[Back To Top](<#testing-contents>)

# User Story Testing

## BookNook Planning and Design

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Create epics and user stories|Create epic and story templates|Verify templates are created|Pass||
||Add epics to project board|Check project board for epics|Pass||
||Assign stories to epics|Verify stories are assigned to epics|Pass||
|Create wireframes|Plan comprehensive design|Review wireframes|Pass||
||Clear reference for coding|Verify wireframes are clear and usable|Pass||
|Design ERD|Use LucidChart to plan database|Check ERD in LucidChart|Pass||
||Display relationships accurately|Verify relationships in ERD|Pass||
||Include tables, keys, relationships|Review ERD|Pass||
|Write Business Plan|Include condept, mission, vision|Review business plan in README|Pass||
||Analyze target market|Verify market analysis in README|Pass||
||Detail marketing strategy|Check marketing strategy in README|Pass||
||Include future development|Verify business model and future features sections in README|Pass||


[Back To Top](<#testing-contents>)

## Viewing and Navigation

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Browsing products|View list of products|Navigate to products page|Pass|
||List displayed clearly|Verify product list clarity|Pass|
||Click to individual page|Navigate to product page|Pass|
|Create product detail|View individual product page|Navigate to product detail|Pass||
||Accurate and clear details|Verify product details|Pass||
||Display extra information|Check for add to wishlist/save for later|Pass||
|Create purchases total|Display running total|Add items to bag to check total|Pass||
||Update in real time|Verify rela time updates|Pass||
|Add to wishlists - logged in user|'Add to wishlist' adds item|Check wishlist for added item|Pass||
||Only logged-in users can add items|Check product detail as guest|Pass||
|View wishlists|Accessible from navbar or profile|Check profile/Click navbar icon|Pass||
||Displays images/names/prices|Check wishlist view|Pass||
||'No item' message if empty|Check wishlist views|Fail|It was decided not to include this, as the wishlist visibly has no wishlist items in and instead has a delete wishlist button. If user no longer desires to keep said wishlist they can delete it.
||Items link to product page|Click item name|Pass||
|Deleting wishlist items|Able item deletion|Delete item|Pass|
||Confirmation message appears|Check message|Pass||
||Instant view update|Check view|Pass||
|Deleting wishlists|Able wishlist deletion|
||Confirmation message appears|Check message|Pass||
||Instant view update|Check view|Pass||



[Back To Top](<#testing-contents>)

## Registration and User Accounts

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Account registration|Display registration button|Check visibility of button|Pass||
||Register with email/password|Test registration process|Pass||
||Receive confirmation email|Verify email receipt|Pass||
|Account login/logout|Display login/logout buttons|Check visibility of buttons|Pass||
||Simple but secure process|Test login/logout functionality|Pass||
||Access profile after login|Verify profile access|Pass||
|Password recovery|Visible 'forgot password' button|Check visibility of button|Pass||
||Receive instructions|Test password recovery process|Pass||
||Simple but secure process|Verify recovery functionality|Pass||
|Create user profile|Able to view profile|Click account icon|Pass||
||Displays all information|View profile page|Pass||
||Has CRUD functionality|Check all content on profile page|Pass||


[Back To Top](<#testing-contents>)

## User Engagement

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Leaving reviews|Leave reviews for purchased products|Test review submission|Pass||
||Include rating and text|Verify review from fields|Pass||
||Show success message|Check for success notification|Pass||
||Save reviews to database|Verify database entry|Pass||
|Viewing reviews|Display reviews on product page|Navigate to product page|Pass||
||Sort reviews by recent|Verify sorting functionality|Pass||
|Update/Delete reviews|Edit or delete reviews|Test edit/delete review|Pass||
||Reflect changes in real-time|Verify real-time updates|Pass||
|Newsletter signup|Form on profile/home page|Check respective pages|Pass||
||Has name/username fields|Check forms|Pass||
||Has 'submit' button|Check forms|Pass||
||Invalid input displays error message|Enter invalid input|Pass||
||Success message upon valid submission|Enter valid input|Pass||
||Confirmation email reception|Check junk folder|Pass||
||Unsubscription on profile and email|Attempt on profile and by email|Pass/Fail|Users can unsubscribe from the profile, however I haven't been able to get the email link to work as of yet|


[Back To Top](<#testing-contents>)

## Shopping Bag and Save for Later

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|View shopping bag|Add, update, remove items|Test shopping bag functionality|Pass||
||Display total priceVerify total price display|Pass||
|View saved items|Access saved items section|Navigate to saved items|Pass||
||Display name, image, price|Verify item details|Pass|| 
|Save items for later|Save items from product page/bag|Test save functionality|Pass||
||Show confirmation message|Check for notification|Pass||
||Store items in accounts|Verify item storage|Pass||
|Move saved items to bag|Move items with single click|Test 'move' functionality|Pass||
||Show confirmation message|Check for notification|Pass||
||Item no longer in 'Saved'|Verify item absence|Pass||
|Remove saved items |Delete items from saved list|Test remove functionality|Pass||
||Show confirmation message|Check for notification|Pass||
||Deleted from saved items|Verify item deletion|Pass||


[Back To Top](<#testing-contents>)

# Checkout

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Proceed to checkout|Enter payment details|Test checkout process|Pass||
||Confirm order and provide number|Verify order confirmation|Pass||
|Order confirmation page display|Redirect to confirmation page|Test redirection|Pass||
||Display order details|Verify order details|Pass||
|Order confirmation email|Confirmation email reception|Verify email receipt|Pass||
||Include order details|Check email content|Pass||


[Back To Top](<#testing-contents>)

# User Profile

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Update delivery details|Update phone, address, etc.|Test update functionality|	Pass||
||Save and display correctly|	Verify saved details|Pass||
|Update personal bio|Update bio and favorite books|Test update functionality|Pass||
||Save and display correctly|Verify saved details|Pass||
|Rewards and benefits|View rewards and benefits|Navigate to rewards section|Pass||
||Display relevant details|Verify reward details|Pass||
|Editing threads|'Edit thread' button under each thread|Verify button visibility|Pass||
||Upon click, user redirected thread page with prefilled form|Test redirection and prefilled content|Pass||
||After submission, user redirected to forum section|Verify updated content in profile|Pass||
|Deleting threads|'Delete' under each thread|Verify button visibility|Pass||
||Upon click, confirmation modal appears|Test modal functionality|Pass||
|Viewing thread list|Thread titles are clickable links|Verify link|Pass||
||User redirected to post list upon click|Test redirection|Pass||


[Back To Top](<#testing-contents>)

# Forum

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|View forum categories|List all categories|Navigate to forum|Pass||
||Display name and description|Verify category details|Pass||
|View threads in a category|View threads in selected category|Navigate forum|Pass||
||Display title, creator, date|Verify thread details|Pass||
|Create a new thread|Access "Create New Thread" button|Test button functionality|Pass||
||Enter title and content|Verify form fields|Pass||
||Submit form to create thread|Test submission process|Pass||
||Display new thread in category|Verify thread appearance|Pass||
|Posts in threads|View posts in thread|Navigate to thread page|Pass||
|Display content, creator, date|Verify post details|Pass||
|Reply to thread|Access 'reply' button|Verify button visibility|Pass||
||Can enter reply|Test reply form|Pass||
||Can submit form|Test form submission|Pass||
||Reply appears in thread|Verify reply visible|Pass||


[Back To Top](<#testing-contents>)

# Administration and Moderation

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Add products to store|Access user-friendly interface|Test interface usability|Pass||
||Separate forms by product type|Verify form fields|Pass||
||Display added product to users/admin|Check product visibility|Pass||
|Editing products|Display 'Edit' buttons to staff|Verify button visibility|Pass||
||Redirect to edit interface|Test redirection|Pass||
||Pre-fill current product details|Verify form fields|Pass||
||Correspond fields to product type|Check field accuracy|Pass||
|Deleting products|Display 'Delete' buttons|Verify button visibility|Pass||
||Show confirmation modal|Test modal functionality|Pass||
||Remove product from store|Verify product removal|Pass||


[Back To Top](<#testing-contents>)

# Website Informational Pages

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Send enquiry|Accessible contact form|Navigate to contact page|Pass||
||Include name, email, message fields|Verify form fields|Pass||
|Display validation error|Test error handling|Pass||
|View BookNook's contact information|Display phone number and email|Verify contact details|Pass||
|Enquiry confirmation|Redirect to success page|Test redirection|Pass||
||Display thank you message|Verify success message|Pass||
||Inform user of message receipt|Check notification|Pass||
||Provide link to products/forum|Verify link functionality|Pass||
|View about us page|Include company history|Navigate to about us page|Pass||
||Include mission and values|Verify content|Pass||
||Well-organized and easy to read|Check readability|Pass||
|View privacy policy|Include comprehensive policy|Navigate to privacy policy|Pass||
||Clear, concise, easy to understand|Verify content clarity|Pass||
||Cover data collection, usage, sharing, rights|Check policy completeness|Pass||
|Contact company about privacy|Provide contact information|Verify contact details|Pass||
||Easily accessible and prominently displayed|Check visibility|Pass||


[Back To Top](<#testing-contents>)

# Website Informational Pages

|**User Story**|**Acceptance Criteria**|**Testing Method**|**Pass/Fail**|**Comments**|
|--------------|-----------------------|------------------|-------------|------------|
|Create and manage social media presence|BookNook Facebook page created|Verify Facebook page creation|Pass||
||BookNook's logo as profile picture|Check profile picture|Pass||
||Regular posts uploaded|Verify content|Pass?Fail|This is a future feature and was intended as an ongoing plan|
||Comments and messages are monitored and responded to|Test message responses|Pass/Fail|This is a future feature and was intended as an ongoing plan|

# Bugs

## Fixed Bugs

## Unresolved Bugs



