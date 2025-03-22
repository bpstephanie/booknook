# BookNook

BookNook is your one-stop destiantion for all things literary. Our platform not only offers a wide range of book and book-related products, but also fosters a vibrant community through our interactive forum. Whether you're looking to purchase the latest bestseller or connect with fellow book enthusiasts, BookNook has you covered. Engage with other like-minded individuals in a space that's comforting.

![Responsive BookNook](documentation/)

Welsome to <a href="https://bn-booknook-017930c30e2f.herokuapp.com/">BookNook</a>

## Contents
* [**BookNook**](<#booknook>)
* [**Contents**](<#contents>)
* [**Project**](<#project>)
  * [Objectives](<#objectives>)
  * [Customer Goals](<#customer-goals>)
  * [Business Goal](<#business-goal>)
  * [Business Model](<#business-model>)
  * [Marketing Techniques](<#marketing-techniques>)
  * [Project Managment](<#project-management>)
    * [Github Kanban Board](<#github-kanban-board>)
    * [MoSCoW Prioritization](<#moscow-prioritization>)
    * [Epics](<#epics>)
  * [Database Schema (ERD)](<#database-schema>)
* [**User Experience UX/UI**](<#user-experience-ux/ui>)
  * [User Stories](<#user-stories>)
  * [Design Choices](<#design-choices>)
    * [Typography](<#typography>)
    * [Colour Scheme](<#colour-scheme>)
    * [Wireframes](<#wireframes>)
  * [Site Structure](<#site-structure>)
* [**Features**](<#features>)
  * [Existing Features](<#existing-features>)
    * [Navbar](<#navbar>)
      * [Logged in User](<#logged-in-user>)
    * [Small Screen Main Menu](<#small-screen-main-menu>)
      * [Logged in User](<#logged-in-user>)
    * [Home Page](<#home-page>)
    * [Products Pages](<#products-pages>)
      * [All Products Page](<#all-product-page>)
      * [By Genre/By Category](<#by-genre/-by-category>)
    * [Product Detail](<#product-detail>)
    * [Bag](<#bag>)
      * [Saved For Later](<#saved-for-later>)
    * [Checkout](<#checkout>)
    * [Order Processing](<#order-processing>)
    * [Checkout Success](<#checkout-success>)
    * [Order Email Confirmation](<#order-email-confirmation>)
    * [Webhook Success](<#webhook-success>)
    * [Profile](<#profile>)
      * [Delivery Details](<#delivery-details>)
      * [Personal Info](<#personal-info>)
      * [Order History](<#order-history>)
        * [Order Confirmation](<#order-confirmation>)
      * [My Reviews](<#my-reviews>)
      * [My Wishlists](<#my-wishlists>)
      * [Forum Interaction](<#forum-interaction>)
      * [Rewards and Benefits](<#rewards-and-benefits>)
      * [Downloads](<#downloads>)
    * [Community](<#community>)
      * [Forum](<#forum>)
      * [Post List](<#post-list>)
    * [BookNook Management](<#booknook-management>)
      * [Product Management](<#product-management>)
      * [Forum Management](<#forum-management>)
    * [Contact Form](<#contact-form>)
    * [Login](<#login>)
    * [Signup](<#signup>)
    * [Logout](<#logout>)
    * [Password Reset](<#password-reset>)
    * [Password Reset Done](<#password-reset-done>)
    * [FAQs](<#faqs>)
    * [Privacy Policy](<#privacy-policy>)
    * [Terms and Conditions](<#terms-and-conditions>)
    * [Newsletter Signup](<#newsletter-signup>)
    * [Footer](<#footer>)
    * [Error Pages](<#error-pages>)
      * [403](<#403>)
      * [404](<#404>)
      * [500](<#500>)
    * [CRUD Functionality](<#crud-functionality>)
  * [**Future Features**](<#future-features>)
  * [**Social Media Pages**](<#social-media-pages>)
    * [Facebook](<#facebook>)
    * [Instagram](<#instagram>)
* [**Technologies Used**](<#technologies-used>)
  * [Languages](<#languages>)
  * [Frameworks and Software](<#frameworks-and-software>)
  * [Python Packages](<#python-packages>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
  * [**To Fork the Project**](<#to-fork-the-project>)
  * [**To Clone the Project**](<#to-clone-the-project>)
  * [**To Deploy Locally on GitHub**](<#to-deploy-locally-on-github>)
  * [**To Deploy on Heroku**](<#to-deploy-on-heroku>)
  * [**AWS Amazon S3 Settings**](<#aws-amazon-s3-settings>)
* [**Credits**](<#credits>)
  * [**Content**](<#content>)
* [**Acknowledgements**](<#acknowledgements>)

# Project


# User Experience UX/UI
  - ## User Stories
  - ## Design Choices
    - ### Typography
      - Google fonts were used for BookNook.
      - Lora was used because it combines readability with elegance, which I believe is perfect for a literary-focuded platform. The serif style provides a classic design which resonates well with book lovers.

      ![Lora Font](documentation/)

      - Source Sans 3 was used for the forum because it offers a clean, modern look that enhanced readability and encourages user engagement. It's well suited for various screen sizes and different resolutions.

      ![Source Sans 3](documentation/)

      - Roboto was used for a consistent and professional look across all pages. It's readbility makes it ideal for a wide range of content.

      ![Roboto](documentation/)

      [Back To Top](<#contents>)

    - ### Colour Scheme
    - ### Wireframes
  - ## Site Structure

  The BookNook site structure is very straightforward and easy to understand.
  
  On larger screens and up the navbar at the top  has links to product pages, which have sorting and filtering features links. Users can access the forum, partners and about us pages in the community section. The logo always directs users back to the homepage. Users can access their profile from the account button and when signed in, a  logout link and wishlist link, when signed out, login and register links are present. If a staff member is signed in, a link to the product management page is present. To the right is the button to the shopping bag. In the center is a large search bar. 
  
  On small and medium screens there is a slide out menu, on this menu, users can find login and register links if not signed in and logout profile and wishlist links if signed in. There is the search bar, products, forum, partners, contact us and about us links. On the navbar, links to the homepage and bag are present at all times. If a staff member is signed in, they can access the product management page from the slide out menu.

  A footer is present at the bottom at all times, which has links to, about us, contact us and frequently asked questions in the shopping with us section. Social media links are present in the follow us section. And the privacy policy is present in the legal section.

  In the forum section, users can see all threads on one page by clicking on the category buttons to the left. By clicking on a thread title, users are redirected to the thread page where they can click the 'Back to Forum' button to go back without using back buttons.

  All users' accessible content is on the profile page, users can click on the buttons to the left to see their delivery details, personal info(bio), order history, reviews, wishlists, saved items, forum interaction, rewards and benefits, and see whether or not they are signed up to the newsletter. In all profiles sections, where content refers to threads, posts, products etc, links are everywhere for users to navigate to those pages.

  On the product management page, staff can add either a book or an accessory by choosing which form they see from the buttons on the left. 



## Business Plan