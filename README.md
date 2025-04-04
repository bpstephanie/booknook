# BookNook

BookNook is your one-stop destination for all things literary. Our platform offers a wide collection of books and book-related products, while also fostering a vibrant community through an interactive forum. Whether you're searching for the latest bestseller or looking to connect with fellow book enthusiasts, BookNook has something for everyone. Join a welcoming space where readers can engage, share, and celebrate their love of literature.

![Responsive BookNook](documentation/screenshots/booknook.png)

Welcome to <a href="https://bn-booknook-017930c30e2f.herokuapp.com/">BookNook</a>

 
## Contents
* [**BookNook**](<#booknook>)
* [**Contents**](<#contents>)
* [**Project**](<#project>)
  * [Objectives](<#objectives>)
  * [Customer Goals](<#customer-goals>)
  * [Business Goal](<#business-goal>)
  * [Business Model](<#business-model>)
  * [Marketing Techniques](<#marketing-techniques>)
    * [Email Campaigns](<#email-campaigns>)
    * [Content Marketing](<#content-marketing>)
    * [Social Media Marketing](<#social-media-marketing>)
    * [Social Media Meta Tags](<#social-media-meta-tags>)
    * [Collaborations](<#collaborations>)
    * [Search Engine Optimisation (SEO)](<#search-engine-optimisation>)
  * [Database Schema (ERD)](<#database-schema>)
  * [Project Managment](<#project-management>)
    * [MoSCoW Prioritization](<#moscow-prioritization>)
    * [Epics](<#epics>)
    * [Github Kanban Board](<#github-kanban-board>)
* [**User Experience UX/UI**](<#user-experience-ux/ui>)
  * [User Stories](<#user-stories>)
  * [Design Choices](<#design-choices>)
    * [Typography](<#typography>)
    * [Colour Scheme](<#colour-scheme>)
    * [Wireframes](<#wireframes>)
  * [Site Structure](<#site-structure>)
* [**Features**](<#features>)
 * [Existing Features](<#existing-features>)
    * [Navigation Bar](<#navigation-bar>)
      * [Search Bar](<#search-bar>)
    * [Logged In Visual](<#logged-in-visual>)
    * [Item In Bag Visual](<#item-in-bag-visual>)
    * [Home Page](<#home-page>)
      * [Newsletter Signup](<#newsletter-signup>)
    * [Footer](<#footer>)
    * [Products Pages](<#products-pages>)
      * [All Products Page](<#all-products-page>)
      * [All Books Page](<#all-books-page>)
      * [All Accessories Page](<#all-accessories-page>)
      * [By Genre/By Category Pages](<#by-genre/-by-category-pages>)
    * [Product Detail](<#product-detail>)
      * [Reviews](<#reviews>)
    * [Bag](<#bag>)
      * [Saved For Later](<#saved-for-later>)
    * [Checkout](<#checkout>)
    * [Order Processing](<#order-processing>)
    * [Checkout Success](<#checkout-success>)
    * [Profile](<#profile>)
      * [Delivery Details](<#delivery-details>)
      * [Personal Bio](<#personal-bio>)
      * [Order History](<#order-history>)
      * [My Reviews](<#my-reviews>)
      * [My Wishlists](<#my-wishlists>)
      * [Wishlists vs Saved For Later](<#wishlists-vs-saved-for-later>)
      * [My Saved Items](<#my-saved-items>)
      * [Forum Interaction](<#forum-interaction>)
      * [Rewards and Benefits](<#rewards-and-benefits>)
      * [Newsletter](<#newsletter>)
      * [Downloads](<#downloads>)
    * [Forum](<#forum>)
      * [Post List](<#post-list>)
    * [Product Management](<#product-management>)
    * [Contact Us](<#contact-us>)
    * [Contact Success](<#contact-success>)
    * [About Us](<#about-us>)
    * [Partners](<#partners>)
    * [FAQs](<#faqs>)
    * [Privacy Policy](<#privacy-policy>)
    * [Login](<#login>)
    * [Signup](<#signup>)
    * [Logout](<#logout>)
    * [404](<#404>)
  * [Future Features](<#future-features>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
  * [**Amazon Web Services**](<#amazon-web-services>)
    * [**S3 Bucket**](<#s3-bucket>)
    * [**Creating AWS Groups**](<#creating-aws-groups>)
    * [**Django AWS Connect**](<#django-aws-connect>)
  * [**Stripe API**](<#stripe-api>) 
  * [**To Deploy on Heroku**](<#to-deploy-on-heroku>)
  * [**To Deploy Locally on GitHub**](<#to-deploy-locally-on-github>)
  * [**To Fork the Project**](<#to-fork-the-project>)
  * [**To Clone the Project**](<#to-clone-the-project>)
* [**Technologies Used**](<#technologies-used>)
* [**Credits**](<#credits>)
  * [**Content**](<#content>)
* [**Acknowledgements**](<#acknowledgements>)


# Project
  ## Objectives
  - Build a user-friendly, responsive platform to sell books and merchandise.
  - Create a vibrant online community through forums for literary discussions and reviews.
  - Ensure seamless navigation, from browsing to purchasing, across all devices.
  - Optimize for accessibility and inclusivity to appeal to a wide audience.

  [Back To Top](<#contents>)

## Customer Goals
  - Provide a convenient way for users to discover and purchase books and merchandise.
  - Create a welcoming and interactive space for book enthusiasts to connect.
  - Simplify the shopping process with clear navigation, a wishlist, save for later section, and secure payment options.

  [Back To Top](<#contents>)

## Business Goal
  - Generate consistent revenue through sales of products.
  - Establish BookNook as a recognized and trusted brand in the literary an e-commerce spaces.
  - Expand the platform's offerings over time, such as introducing BookNook events, online and in-person, exclusive content and premium memberships.

  [Back To Top](<#contents>)

## Business Model
  BookNook operates as a literary e-commerce platform following a Business-to-Customer (B2C) model. By offering a curated selection of books and book-related products alongside an interactive community for book lovers, BookNook creates a unique blend of commerce and connection. Customers make purchases directly through the platform without intermediaries, ensuring a seamless shopping experience. This direct model not only facilitates clear communication with customers but also allows BookNook to adapt swiftly to their needs and preferences.

  - ### Revenue Streams:
    - Product sales (book, book-themed merchandise).

    Once BookNook has more customers and consistent interaction and engagement in the forum:
    - Membership plans or subscriptions for exclusive perks (e.g. early access to book releases, book signings or discounts).

  - ### Cost Structure:
    - Operational costs, such as website maintenance and marketing.
    - Supplier relationships for product procurement.
    - Shipping and logistics for order fulfillment.

  - ### Customer Segments (Target Market):
    - Primarily 18-45, including young adults, students and working professionals who have discretionary spending for books and related accessories. Equally inclusive, with a slight lean towards female readers who, statistically, purchase more books.

  - ### Value Proposition:
    - A one-stop platform for book shopping and community interaction.
    - High-quality products with engaging content to elevate the customer experience.

  [Back To Top](<#contents>)

## Marketing Techniques
  - ### Email Campaigns
    - Send newsletters with personalized book recommendations (to users
    with profiles) and popular book recommendations to users without accounts, discounts, and updates.

  Through strategically placed sign-up forms on the homepage and profile section, BookNook makes it effortless for customers to subscribe. These newsletters, enriched with visually appealing content that is both desktop- and mobile-friendly, provide personalized book recommendations to users with profiles and popular recommendations to those without. Additionally, they feature special offers, discounts, and updates. These emails not only keep customers informed but also enhance their literary journey by offering tailored insights and exclusive deals, fostering a meaningful and lasting connection between BookNook and its readers.

  [Back To Top](<#contents>)
    
  - ### Content Marketing
    - Share book recommendations, reviews or reading tips through the forum.

  The forum exists as a way to form a strong community for BookNook. The big players in the bookstore market have immense brand awareness and the competition is extraordinary. This is one of the reasons why BookNook was created not just to be a bookstore, but as a community for like-minded individuals to share and feel welcome. It is the online equivalent of an independent bookshop you find in a little town. By nurturing this online equivalent of an independent bookshop, BookNook not only builds brand loyalty but also positions itself as a haven for literary enthusiasts who seek genuine engagement over mass-market anonymity.

  [Back To Top](<#contents>)
    
  - ### Social Media Marketing
    - Run targeted ad campaigns on platforms like Facebook, Instagram, and TikTok.
    - Host interactive events such as a book club or live Q&A sessions with authors.

    BookNook has an online presence through Facebook and Instagram with dedicated business pages that serve as hub for engaging content. TikTok is next on the agenda, broadening the reach to a younger, tech-savvy audience. Regular posts and targeted ad campaigns create consistent visibility across all platforms. Facebook’s catalogue and ‘shop now’ button seamlessly redirect customers to the BookNook website, while Instagram Stories and Reels capture attention through visually dynamic content.

    <a href="https://www.facebook.com/profile.php?id=61574089695787">Facebook Profile</a>, <a href="https://www.instagram.com/booknook_uk/">Instagram Profile</a>


    <details><summary>Facebook Profile Photo and Cover Photo</summary>

    ![Facebook Profile Photo and Cover Photo](documentation/screenshots/social-media/facebook1.png)

    </details>

    <details><summary>Facebook Profile Photo and Cover Photo</summary>
    
    ![Facebook](documentation/screenshots/social-media/facebook2.png)

    </details>

    <details><summary>Instagram Profile</summary>
  
    ![Instagram Profile](documentation/screenshots/social-media/instagram.jpg)

    </details>

    <details><summary>Sample Posts on Instagram</summary>
    
    ![Instagram Post 1](documentation/screenshots/social-media/i-post1.jpg)

    ![Instagram Post 2](documentation/screenshots/social-media/i-post2.jpg)

    </details>

    [Back To Top](<#contents>)
    
    - ### Social Media Meta Tags
    Social media meta tags enhance the way BookNook's content appears when shared on platforms like Facebook and LinkedIn. These tags ensure that posts include a compelling title, description and image that draw attention and engage users.

    1. og:title: "BookNook - For Book Lovers Everywhere" grabs attention by succinctly summarizing the brand's appeal to book enthusiasts.

    2. og:description: A short but inviting explanation that entices potential visitors to explore the platform and join the BookNook community.

    3. og:type: Specifies that BookNook is a website, helping platforms optimize the display of the link.

    4. og:url: Ensures users are directed to the correct page, enhancing trust.

    The meta tags play a vital role in social media marketing by improving click-through rates, increasing engagement and boosting brand visibility.

    [Back To Top](<#contents>)
  
  - ### Collaborations
    - Partner with influencers, authors, or publishers to amplify reach.

    Collaborations with influencers, authors or publishers are key to amplifying BookNook's reach. Future initiatives could include live-streamed interviews with rising authors or exclusive signed editions made available through BookNook, making the platform a destination for unique literary experiences. Through such partnerships, BookNook doesn't just sell books, it brings readers closer to the stories and creators they admire and cherish, further strengthening its community-centered vision.
  
  [Back To Top](<#contents>)

  ### Search Engine Optimisation (SEO)
  #### Keywords
  I used [Semrush](https://www.semrush.com/) to check keywords with low competition, using a combination of short and long-tail keywords to include in my site meta tags.

  The keywords used:
  - reading culture
  - book community
  - reads
  - ya fiction
  - bookmarks for books
  - collectible books,
  - independent bookshop
  - literary forum
  - literary gift ideas
  - book collectors
  - keen reader
  - happy reader

  [Back To Top](<#contents>)

  #### Sitemap
  I used [XML Sitemaps]() to create a sitemap to improve SEO.

  #### Robots.txt File
  I generated a robots.txt file to improve SEO. This file tells search engines which pages are available to crawl and which to ignore.

  ```
  User-agent: *
  Disallow:
  Sitemap: https://bn-booknook-017930c30e2f.herokuapp.com/
  ```

  ## Database Schema (ERD)
  My entity relationship diagram was created using [LucidChart](https://www.lucidchart.com/). The ERD is a visual representation of the database structure.

  <details><summary>ERD: Planning Stage</summary>
    
  ![ERD Plan](documentation/screenshots/erd-plan.png)

  </details>
  
  <details><summary>ERD: Final Stage</summary>
    
  ![ERD Final](documentation/screenshots/erd-final.png)

  </details>

  [Back To Top](<#contents>)

  ## Project Management
  To organise the project effectively, [GitHub](https://github.com/)'s labelling system was used to classify user stories and epics for broader milestones. This ensures a clear and manageable structure, allowing me to track progress and maintain focus on key deliverables. 

  Before initiating the software development portion of the project, a moderate amount of planning was done. This included thinking of ways to compete against well-established businesses in the same sector, creating wireframes and planning the models and their relationships.

  Having this research was essential to stay on track. I sometimes feel overwhelmed by the enormity of a project which is why I planned an end goal to get to. To maintain flexibility, I intoduced epics and their respective user stories incrementally, allowing room for inspiration and additional features during development.

  I found it difficult to organise my sprints on the project board therefore I opted for pen and paper. I know this is not ideal but for this project it was the right decision for me and it is the best way I could keep things organised.

  I kept a detailed account of all bugs in a separate file, some of which I fixed straight away and others were left until all the important features were implemented.

  I admit that I sometimes found it difficult to not race ahead and do the 'exciting' features, but the adding of epics in parts helped with this.

  This project not only refined my technical and organisational skills but also deepened my uderstanding of the balance between structured planning and adaptability. From integrating advanced features to overcoming development challenges, this journey has been invaluable in preparing me for future full-stack projects adn fostering a user-centered approach to design.

  [Back To Top](<#contents>)

  - ### MoSCoW Prioritization
  To effectively manage requirements and ensure a clear focus on deliverables, I utilized MoSCoW prioritisation. This method helped me categorise features into MustHaves, Should-Haves, Could-Haves and Won't Haves. 

  - **Must-Haves**: guaranteed to be delivered (70% of stories)
  - **Should-Haves**: adds value but is not vital (15% of stories)
  - **Could-Haves**: has a small impact if left out (15% of stories)
  - **Won't-Haves**: not a priority right now


  - ### Epics
  To ensure structured and goal-oriented development, I used epics within GitHub to organized related tasks groups. Each group represented a key area of functionality for the BookNook project.

  They were as follows:
  - BookNook Planning and Design
  - Viewing and Navigation
  - Registration and User Accounts
  - User Engagement
  - Shopping Bag and Save for Later
  - Checkout
  - User Profile
  - Forum
  - Administration and Moderation
  - Website Informational Pages
  - Marketing and Community Engagement

  **GitHub Kanban Board**

  <details><summary>Project Board</summary>
    
  ![Project Board](documentation/screenshots/kanban-board.png)

  </details>

[Back To Top](<#contents>)


# User Experience UX/UI
## User Stories

### BookNook Planning and Design
The initial stages of the design and planning of the BookNook e-commerce platform. This epic involves creating wireframes, designing an Entity-Relationship Diagram (ERD), and developing epics and user stories to guide the development process.
(MUST HAVE)


1. **Create epics and user stories:** As a developer, I can create epics and site user, developer and site owner stories, So that I have a structured guide for the project.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Create epic and story templates.
- Criteria 2: Add epics to project board.
- Criteria 3: Assign stories to epics.

2. **Create wireframes:** As a developer, I can create wireframes, so that I can plan the appearance and structure of my e-commerce site.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The wireframes should plan a comprehensive design, including the layout and placement of vital components.
- Criteria 2: The wireframes should be clear so as to be used as a reference when writing the necessary code.

3. **Design ERD:** As a developer, I can design an Entity-Relationship Diagram, so that I can plan my database models.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Use Lucid Chart to plan database.
- Criteria 2: The ERD should accurately display the relationships between the models.
- Criteria 3: The ERD should include tables, primary and foreign keys, and relationships.

4. **Write Business Plan:** As a site owner, I can write a business plan, so that I have a clear road map for my e-commerce platform.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The plan should include a detailed description of the concept, mission and vision.
- Criteria 2: The plan should include analysis of the target market including needs and trends.
- Criteria 3: The plan should include a detailed marketing strategy including branding, promos, social media presence and specific marketing techniques.
- Criteria 4: The plan should include future development and enhancements.


[Back To Top](<#contents>)

### Viewing and Navigation
5. **Browsing products:** As a shopper, I can view a list of products, so that I can select which to purchase.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Shopper can view a list of well organised products on products page.
- Criteria 2: The list should be displayed clearly and easily navigable.
- Criteria 3: Upon clicking on an individual item, the shopper should be taken to it's individual page.

6. **Create product details:** As a shopper, I want to view individual product details, so that I can see name, description, price, rating and image.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Upon selecting a product, shopper is taken to individual product page displaying necessary information.
- Criteria 2: The product details must be accurate and clear.
- Criteria 3: The page should display any extra information such as sales and/or offers.

7. **Create purchases total:** As a shopper, I want to see my purchases total at any time, so that I stay within my budget and do not overspend.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The platform should display the running total clearly for shoppers to see what the contents of their bag totals.
- Criteria 2: The bag total should update in real time.

8.  **View categories:** As a site user, I can views a specific category of products, So that I can filter the ones I like and want to purchase.
(WON'T HAVE)

Acceptance Criteria:
- Criteria 1: The platform should display different categories of products on the homepage.
- Criteria 2: Upon selecting a category, the list of products displayed should only be those of that category.
- Criteria 3: The category filter should be user-friendly and intuitive.

9.  **Add to wishlists - logged in user:** As a site user (logged-in), I want to add items to my wishlist from product pages,so that I can save items for later.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: When a user clicks "Add to Wishlist", the item is added to their wishlist.
- Criteria 2: Only logged-in users can save wishlists.

10.  **View wishlists:** As a site user, I want to view my wishlists, So that I can review the items I've saved.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The wishlist is accessible from the navigation menu or user profile.
- Criteria 2: The wishlist displays all saved items with their images, names and prices.
- Criteria 3: The wishlist displays a no item messages if no items are in the wishlist.
- Criteria 4: Items links back to their respective product pages.

11.  **Deleting wishlist items:** As a site user, I want I want to be able to remove items from my wishlist, So that I can manage it effectively.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Users can remove items individually from the wishlist.
- Criteria 2: A confirmation dialog appears before removing and item.
- Criteria 3: The wishlist updates dynamically after an item is removed.

12.  **Deleting wishlists:** As a site user, I want I want to be able to delete entire wishlist, So that I can keep only items and wishlists I want.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Users can delete entire wishlists.
- Criteria 2: A confirmation dialog appears before deleting the wishlist.
- Criteria 3: The wishlist section on the profile updates dynamically after the deletion of a wishlist.


[Back To Top](<#contents>)

### Registration and User Accounts
Site users can register to the site, receive confirmation after signing up and view user profile.

13. **Account registration:** As a site user, I can easily sign up, so that I can have a personal account and view my profile.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The registration button should be displayed clearly on the platform.
- Criteria 2: Users should be able to register with an email address and password.
- Criteria 3: Users should receive and confirmation email and/or message upon successful registration.

14. **Account login/logout:** As a site user, I can easily login/logout, So that I can see my profile/keep my information secure.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Login/logout buttons should be clearly displayed across all pages on the platform.
- Criteria 2: The login/logout process should be simple but secure, requiring minimal steps to carry out.
- Criteria 3: Upon login, site users should have access to their profile and account information.

15. **Password recovery:** As a site user, I can easily recover my password in case I forget, So that I can recover access to my account.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Access to the 'forgot my password' button should be visible on login form and anywhere it is needed.
- Criteria 2: The site user should receive instruction on the process.
- Criteria 3: The process should be simple but secure to carry out.

16. **Create user profile:** As a site user, I can view my personal profile, so that I can see my personal order history, order confirmations, save payment information, and view personal favourites.

Acceptance Criteria:
- Criteria 1: The site user should be able to view their own dedicated profile page.
- Criteria 2: It should display all information saved clearly.
- Criteria 3: It should have CRUD functionality on all items that the site user can edit.


[Back To Top](<#contents>)

### User Engagement
To boost user interaction and create a community-driven platform.

17. **Leaving reviews:** As a site user, I want to leave a review for a product I purchase, so that I can share my feedback.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Users can only leave reviews for products they have purchased.
- Criteria 2: The review form includes a rating (1-5) and a text comment field.
- Criteria 3: A success message is shown after submission.
- Criteria 4: Reviews are saved to the database and displayed on the product page.

18. **Viewing reviews:** As a site user, I want to view reviews for a product, so that I can make an informed decision on whether or not to buy it.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The product page displays user reviews, showing ratings, review and usernames.
- Criteria 2: Reviews are sorted by most recent or highest-rated by default.

19. **Update/Delete reviews:** As a site user, I want to update or delete my reviews, so that I can manage my reviews.

Acceptance Criteria:
- Criteria 1: Users can edit or delete their reviews via their profile or the product page.
- Criteria 2: Changes are updated in the database and reflected in real time.

20. **Adding comments on reviews:** As a site user, I want I want to comment on reviews, So that I can engage with other users.
(WON'T HAVE)

Acceptance Criteria:
- Criteria 1: Users can comment on any review via a button below the review.
- Criteria 2: Comments are displayed in a threaded format under the review.
- Criteria 3: Comments are saved in the database.

21. **Editing/deleting comments on reviews:** As a site user, I want to edit or delete my comments, so that so I can control my interaction.
(WON'T HAVE)

Acceptance Criteria:
- Criteria 1: Users can delete their comments.
- Criteria 2: Users can edit their comments.
- Criteria 3: A confirmation modal is displayed upon pressing delete to confirm choice.

22. **Reporting reviews/comments:** As a site user, I want I want to report inappropriate reviews or comments, So that I can help maintain the site's safety/quality.
(WON'T HAVE)

Acceptance Criteria:
- Criteria 1: Users can report reviews or comments via a "Report" button.
- Criteria 2: Reported content is flagged in the database for admin review.
- Criteria 3: A success notification or message is shows after reporting.

23. **Newsletter signup:** As a site user, I want to sign up for newsletters, so that I can receive updates and special offers from the company.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The newsletter sign up form should be available on the homepage and profile.
- Criteria 2: The form should have fields for name and email address.
- Criteria 3: The form should have a submit button.
- Criteria 4: The form should display a validation error if the email field is empty or contains an invalid email address.
- Criteria 5: The form should display a success message upon successful submission.
- Criteria 6: The user should receive a confirmation email after signing up.
- Criteria 7: The user should be able to unsubscribe from the newsletter at any time via a link in the email or from their profile.


[Back To Top](<#contents>)

### Shopping Bag and Save for Later
Develop a shopping bag system and implement a secure and efficient checkout process. Allow users to save items that they intend to purchase soon but not immediately.

24. **View shopping bag:** As a site user, I want to add items to my bag, so that I can see them and their prices and purchase them later.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to add, update quantities and remove items from their shopping bag.
- Criteria 2: The shopping bag should display the total price of selected items.

25. **View saved items:** As a site user (logged in), I want to view my items saved for later, so that I can review them when I am ready to purchase.
(SHOULD HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to access "Saved Items" section from their account or shopping bag.
- Criteria 2: The saved items should display name, image and price of each item.

26. **Save items for later:** As a site user, I want to save items for later, so that I can purchase them at a future date without adding them to my cart immediately.
(SHOULD HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to save items for later from the product detail page or shopping bag.
- Criteria 2: A confirmation message should be displayed when an item is successfully saved for later.
- Criteria 3: Saved items should be stored in the user's account and remain accessible across sessions.

27. **Move saved items to bag:** As a site user, I want to move saved items to my shopping bag, so that I can proceed to checkout and purchase them.
(SHOULD HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to move items from "Saved Items" to the shopping bag with a single click.
- Criteria 2: A confirmation message should be displayed when an item is successfully moved.
- Criteria 3: The item should be removed from "Saved Items" and added to the shopping bag.

28. **Remove saved items:** As a site user, I want to remove items from my saved list, so that  I can keep my list up-to-date with only the items I am interested in.
(SHOULD HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to remove items from the "Saved Items" section.
- Criteria 2: A confirmation message should be displayed when an item is successfully removed.
- Criteria 3: The item should be removed from the "Saved Items" section and no longer be accessible.


[Back To Top](<#contents>)

### Checkout
Implement a secure and efficient checkout process.

29. **Proced to checkout:** As a site user, I want to proceed to checkout and make a payment, So that I can complete my purchase.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: Users should be able to proceed to checkout and enter payment details.
- Criteria 2: The checkout process should confirm the order and provide an order number.

30. **Order confirmation page display:** As a site user, I want to view my order confirmation after checkout, so that I can make sure all items are correct and I haven't made any mistakes.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: After completing the checkout process, the user is redirected to an order confirmation page.
- Criteria 2: The order confirmation page displays the order number, order date, items in order, and customer details.

31. **Order confirmation email:** As a site user, I want to receive an email confirmation after checking out, so that I have the confirmation of what I have purchased in my records.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The user receives an order confirmation email with the same details as the order confirmation page.
- Criteria 2: The email is sent to the user's registered email address immediately after the order is placed.


[Back To Top](<#contents>)

### User Profile
All things related to user profiles and what they can do once logged in.

32. **Update delivery details:** As a site user, I want to update my delivery details, so that my orders are sent to the correct address.
(MUST HAVE)

Acceptance Criteria:
- Criteria 1: The user can update their phone number, postal code, town or city, street address 1, street address 2, county, and country.
 - Criteria 2: The updated details are saved and displayed correctly.

33. **Update personal bio:** As a site user,
I want to update my personal information,
So that my profile reflects my current preferences and interests.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The user can update their bio and favourite books.
 - Criteria 2: The updated information is saved and displayed correctly.

34. **Rewards and benefits:** As a logged-in user,
I want to view the rewards and benefits available to me,
So that I can take advantage of them.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The user can view a list of rewards and benefits.
 - Criteria 2: Each reward or benefit displays relevant details and instructions on how to redeem it.

35. **Participating in reading challenges:** As a logged-in user, I want to participate in reading challenges, so that I can engage with the community and earn rewards.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: The user can view and join reading challenges.
 - Criteria 2: The user can track their progress in each challenge.

36. **Editing threads in profile:** As a logged-in user, I want to edit and update my threads from my profile, so that I can update the content of my threads.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: An 'Edit Thread' button is displayed under each thread.
 - Criteria 2: Upon clicking the button, user is redirected to edit thread page, which is pre-filled with current thread content
 - Criteria 3: Upon submitting, user is redirected back to their profile with the update thread content displayed.

37. **Deleting threads in profile:** As a logged-in user, I want to delete my threads from my profile, so that I can remove unwanted threads.

Acceptance Criteria:
 - Criteria 1: A 'Delete' button should be displayed under each thread.
 - Criteria 2: Upon clicking 'Delete', a modal appears to confirm cancellation or to cancel.

38. **Viewing thread detail page (post) list from profile:** As a logged-in user, I want to be taken to the post list of a thread upon clicking the thread title in my profile, so that I can view all content within the thread.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: Thread titles should be displayed as clickable links.
 - Criteria 2: Upon clicking a thread title, the user is redirected to the post list page to see all content within the thread.

39. **Viewing replies to deleted threads:** As a logged-in user, I want replies to deleted threads to still be in my profile, so that I can access the content of the replies even if the thread is deleted.
(WON'T HAVE)

Acceptance Criteria:
 - Criteria 1: Replies to deleted threads are displayed in user's profile.
 - Criteria 2: Given a thread is marked as deleted, upon clicking the thread title, the user should be redirected to the thread page of the deleted thread.
 - Criteria 3: All replies to the deleted thread should be visible on the thread page, regardless of thread's deleted status.


[Back To Top](<#contents>)

### Forum
Forum categories, threads and posts.

40. **View forum categories:**
As a site user, I want to see a list of all categories on the forum homepage, so that I can choose a category to explore.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: User can see a list of all categories on the forum homepage.
 - Criteria 2: Each category displays it's name and when clicked displays it's description.

41. **View threads in a category:** As a site user, I want to view all threads within a selected category, so that I can read what the community is saying.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: User can click on a category button to view threads in that category.
 - Criteria 2: Threads are displayed with their title, creator, and creation date.

42. **Create a new thread:** As a logged-in user, I want to create a new thread in a category, so that I can start a discussion.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: User can access the "Create New Thread" button within a category.
 - Criteria 2: User can enter the thread title and content.
 - Criteria 3: User can submit the form to create the thread.
 - Criteria 4: The new thread appears in the selected category.

43. **Posts in threads:** As a site user, I want to view all posts within a thread, so that I can read the discussion.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: User can click on a thread title to view posts in that thread.
 - Criteria 2: Posts are displayed with their content, creator, and creation date.

44. **Reply to a thread:** As a logged-in user, I want to reply to a thread, so that I can contribute to the discussion.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: User can access the "Reply" button within a thread.
 - Criteria 2: User can enter their reply content.
 - Criteria 3: User can submit the form to post their reply.
 - Criteria 4: The new reply appears in the thread.


[Back To Top](<#contents>)

### Administration and Moderation
BookNook management of user reviews, forum posts, thread, categories. Adding products.

45. **Moderate threads and posts:** As a moderator, I want to manage threads and posts, so that I can ensure the forum content is appropriate.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: Moderator can access moderation tools.
 - Criteria 2: Moderator can edit or delete threads and posts.
 - Criteria 3: Moderator can view reports of inappropriate content.

46. **Manage categories, threads, posts:** As a site admin, I want to manage forum categories, threads and posts, so that I can organize and the forum and make sure all content is appropriate.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: Admin can access category, threads and posts management tools.
 - Criteria 2: Admin can create, edit, or delete categories, threads and posts.

47. **Add products to store:** As a site admin, I want to add products to the store, so that I can add incoming stock and keep the store up to date.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The admin should have access to a user-friendly interface which allows them to add new products to the site.
 - Criteria 2: There should be separate forms for each type of product with required fields such as author, isbn and author for books, and category for accessories.
 - Criteria 3: Once added, the added product should be visible to users on the site.

48. **Editing products:** As an admin, I want to edit products, so that I can keep all products available in the store up-to-date.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: There should be 'Edit' buttons on products and product detail pages, only available to the site admin.
 - Criteria 2: Upon clicking the button, the admin should be redirected to a user-friendly interface to edit existing product details.
 - Criteria 4: The fields should be automatically filled with current product details.
 - Criteria 5: The fields displayed should correspond to type of product.

49. **Deleting products:** As an admin, I want to delete products, so that I can remove products that are no longer being sold in the store.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: There should be 'Delete' buttons on products and product detail pages.
 - Criteria 2: Upon clicking the button, a modal should appear confirming deletion.
 - Criteria 3: Once the deletion is confirmed, the product should no longer be displayed in the store.


[Back To Top](<#contents>)

### Website Informational Pages
All pages that provide information about key things on the site.

50. **Send enquiry:** As a site user, I want to fill out a contact form, so that I can send a message to the company.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The contact us page should be accessible on all pages in navbar or footer.
 - Criteria 2: The form should include fields for name, email and message.
 - Criteria 3: The form should have a submit button.
 - Criteria 4: The form should display a validation error if any required field is empty.

51. **View BookNook's cotact information:** As a site user, I want to see the company's contact information on the Contact Us page, so that I can reach out via phone or email.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The page should display the company's phone number and email address.
 - Criteria 2: The contact information should be easily visible and accessible.

52. **Enquiry confirmation:** As a site user, I want to see a confirmation of sending an enquiry, so that I know my enquiry was sent successfully.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The user should be directed to the Contact Us Success page after submitting the form.
 - Criteria 2: The page should display a thank you message.
 - Criteria 3: The page should inform the user that their message has been received and will be responded to shortly.
 - Criteria 4: The page should provide a link to return to the homepage, products page or forum.

53. **View about us page:** As a site user, I want to learn about the company's history and mission on the About Us page, so that I can understand its background and values.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: The page should include a section about the company's history.
 - Criteria 2: The page should include a section about the company's mission and values.
 - Criteria 3: The content should be well-organized and easy to read.

54. **View company's team members:** As a site user, I want to see profiles of the company's team members on the About Us page, so that I can learn about the people behind the company.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: The page should display profiles of key team members.
 - Criteria 2: Each profile should include a photo, name, title, and brief bio.
 - Criteria 3: The profiles should be visually appealing and consistent in style.

55. **View privacy policy:** As a site user, I want to read the company's privacy policy, so that I understand how my personal information is handled.
(SHOULD HAVE)

Acceptance Criteria:
 - Criteria 1: The page should include a comprehensive privacy policy.
 - Criteria 2: The content should be clear, concise, and easy to understand.
 - Criteria 3: The policy should cover topics such as data collection, data usage, data sharing, and user rights.

56. **Contact company about privacy:** As a site user, I want to be able to contact the company regarding privacy policy concerns on the Privacy Policy Page, so that I can address any issues or questions I have.
(SHOULD HAVE)

Acceptance Criteria:
 - Criteria 1: The page should provide contact information for privacy-related inquiries.
 - Criteria 2: The contact information should be easily accessible and prominently displayed.

57. **View Ts & Cs:** As a site user, I want to read the company's terms and conditions, so that I understand the rules and guidelines for using the website.
(COULD HAVE)

Acceptance Criteria:
 - Criteria 1: The page should include a comprehensive terms and conditions document.
 - Criteria 2: The document should cover topics such as user responsibilities, prohibited activities, and limitations of liability.
 - Criteria 3: The content should be clear, concise, and easy to understand.


[Back To Top](<#contents>)

### Marketing and Community Engagement
All things related to marketing, social media, getting customers more involved in BookNook forum.

58. **Create and manage social media presence:** As a marketing manager, I want to create and manage a Facebook page for BookNook, so that brand visibility increases and BookNook can engage with the community.
(MUST HAVE)

Acceptance Criteria:
 - Criteria 1: A Facebook is created for BookNook.
 - Criteria 2: BookNook's logo appears as the profile picture.
 - Criteria 3: Regular posts, updates, promotions, and community engagement content are uploaded.
 - Criteria 4: Comments and messages and monitored and responded to.

  Task: **Create Facebook Page**
  Set up a Facebook page for BookNook to establish an online presence and engage with the community.
  (MUST HAVE)

  What Needs To be Done:

   - Create the Facebook page using the correct business information.
   - Add a profile picture and cover photo that represent BookNook.
   - Write a compelling bio and about section.

   Acceptance Criteria:
   - The Facebook page is created with accurate business information.
   - Profile picture and cover photo are uploaded and visually appealing.
   - Bio and about section are complete and engaging.


[Back To Top](<#contents>)

  ## Design Choices
  - ### Typography
    - Google fonts were used for BookNook.
    - Lora was used because it combines readability with elegance, which I believe is perfect for a literary-focuded platform. The serif style provides a classic design which resonates well with book lovers.

    ![Lora Font](documentation/screenshots/ux/lora.png)

    - Source Sans 3 was used for the forum because it offers a clean, modern look that enhanced readability and encourages user engagement. It's well suited for various screen sizes and different resolutions.

    ![Source Sans 3](documentation/screenshots/ux/source-sans-3.png)

    - Roboto was used for a consistent and professional look across all pages. It's readbility makes it ideal for a wide range of content.

    ![Roboto](documentation/screenshots/ux/roboto.png)

    [Back To Top](<#contents>)

  - ### Colour Scheme
  This colour palette was selected to enhance user experience and maintain a visual harmony throughout the application. The navy shade (#0b254b) was used for critical elements like the footer, banner above navigation and buttons on all pages except for the forum to provide a sense of stability and professionalism. In contrast the white (#fefefe) complemented the navy for the navigation bar and buttons, creating a clean and modern look.

  To infuse vibrancy and categorization, distinct colours were used for specific sections:

  - (#ffd968) for the community section to evoke warmth and engagement. While (#dc8a3f) was used for the forum buttons.
  - (#057d23) for the products section, reflecting trustworthiness.
  - (#0f5aac) was only used in the products section to distinguish genres from accessory categories.
  - (#f34dcf) for wishlists, bringing energetic and playful feel to the user's personal space.

  <details><summary>Colour Palette</summary>
  
  ![Colour Palette](documentation/screenshots/ux/colour-palette.png)

  </details>


  [Back To Top](<#contents>)

  - ### Wireframes
  I used Balsamiq to create the wireframes for this project. These were used as a guide. During development I would check the wireframes and see how I could display the information from a better UX standpoint. This is especially evident with the profile page.

  <details><summary>Home Page</summary>
  
  ![Home Page](documentation/screenshots/ux/wireframe-homepage.png)

  </details>

  <details><summary>Products Page</summary>
  
  ![Products Page](documentation/screenshots/ux/wireframe-products.png)

  </details>

  <details><summary>Product Detail Page</summary>
  
  ![Product Detail Page](documentation/screenshots/ux/wireframe-product-detail.png)

  </details> 

  <details><summary>Community Page</summary>
  
  ![Community Page](documentation/screenshots/ux/wireframe-community.png)

  </details>

  <details><summary>Bag Page</summary>
  
  ![Bag Page](documentation/screenshots/ux/wireframe-bag.png)

  </details>

  <details><summary>Profile Page</summary>
  
  ![Home Page](documentation/screenshots/ux/wireframe-profile.png)

  </details> 


  [Back To Top](<#contents>)

  ## Site Structure

  The BookNook site structure is very straightforward and easy to understand.
  
  On larger screens and up the navbar at the top  has links to product pages, which have sorting and filtering features links. Users can access the forum, partners and about us pages in the community section. The logo always directs users back to the homepage. Users can access their profile from the account button and when signed in, a  logout link and wishlist link, when signed out, login and register links are present. If a staff member is signed in, a link to the product management page is present. To the right is the button to the shopping bag. In the center is a large search bar. 
  
  On small and medium screens there is a slide out menu, on this menu, users can find login and register links if not signed in and logout profile and wishlist links if signed in. There is the search bar, products, forum, partners, contact us and about us links. On the navbar, links to the homepage and bag are present at all times. If a staff member is signed in, they can access the product management page from the slide out menu.

  A footer is present at the bottom at all times, which has links to, about us, contact us and frequently asked questions in the shopping with us section. Social media links are present in the follow us section. And the privacy policy is present in the legal section.

  In the forum section, users can see all threads on one page by clicking on the category buttons to the left. By clicking on a thread title, users are redirected to the thread page where they can click the 'Back to Forum' button to go back without using back buttons.

  All users' accessible content is on the profile page, users can click on the buttons to the left to see their delivery details, personal info(bio), order history, reviews, wishlists, saved items, forum interaction, rewards and benefits, and see whether or not they are signed up to the newsletter. In all profiles sections, where content refers to threads, posts, products etc, links are everywhere for users to navigate to those pages.

  On the product management page, staff can add either a book or an accessory by choosing which form they see from the buttons on the left.


  [Back To Top](<#contents>)

# Features
## Existing Feautures
### Navigation Bar
Featured on all pages, the fully responsive navigation bar includes links to the:
- Home page (the BookNook logo),
- Products page,
- Book by Genre page,
- Accessory by Categories page,
- Forum,
- Partners page,
- About Us page,
- Contact Us page,
- Bag,
- Login/Register pages for guests and logged out users
- My Profile page for logged in users
- Product Management for logged in staff.

In the centre of the navbar is a search bar where users can look up anything in the products, by name of product, or a word in the description.

The nav bar allows the user to easily navigate to the main pages across the site. On small and medium screens the navbar is collapsed, users see the logo hompage link on the left, a menu toggle and the bag on the right.

In the off-canvas menu, all links that are available on desktops are available there along with the search bar.

  <details><summary>NavigationBar whilst user is logged out - Desktop View</summary>
  
  ![Desktop Navbar whilst Logged out](documentation/screenshots/features/navbar-desktop-lo.png)

  </details>

  <details><summary>NavigationBar whilst user is logged in - Desktop View</summary>
  
  ![Desktop Navbar whilst Logged in](documentation/screenshots/features/navbar-desktop.png)

  </details>

  <details><summary>NavigationBar - Mobile View</summary>
  
  ![Mobile Navbar](documentation/screenshots/features/navbar-mobile.png)

  </details>

  <details><summary>NavigationBar - Off Canvas Menu whilst user is logged out</summary>
  
  ![Navbar Off Canvas Menu whilst User is Logged Out](documentation/screenshots/features/navbar-mobile-lo.png)

  </details>


  <details><summary>NavigationBar - Off Canvas Menu whilst user is logged in</summary>
  
  ![Navbar Off Canvas Menu whilst User is Logged in](documentation/screenshots/features/offcanvas-menu.png)

  </details>


[Back To Top](<#contents>)

#### Search Bar
If the user searches for something that is associated with one or more of the products, they will be taken to the products page and shown the items that meet their criteria. If what the user searches for doesn't match any product they will be shown an error message. If they leave the search bar blank, an error message will be shown stating that. If the user double clicks on the 'search' button they will be taken to the products page.

  <details><summary>Error Message - No Products Meet The Search</summary>
  
  ![Error Message - No Products Meet The Search](documentation/screenshots/features/unmet-criteria.png)

  </details>

  <details><summary>Error Message - Blank Search/No Input</summary>
  
  ![Error Message - Blank Search/No Input](documentation/screenshots/features/empty-search.png)

  </details>


[Back To Top](<#contents>)

### Logged In Visual
Once a user has logged in, there is visual feedback in the form of a message stating their logged in status. Where 'Account' is displayed for guest or logged out users, is a message 'Hi username' on the desktop view and in the off canvas menu, in the navy card at the top of the menu.

  <details><summary>Logged in Visual - Desktop View</summary>
  
  ![Logged in Visual - Desktop View](documentation/screenshots/features/loggedin-desktop.png)

  </details>

  <details><summary>Logged in Visual - Mobile View</summary>
  
  ![Logged in Visual - Mobile View](documentation/screenshots/features/loggedin-mobile.png)

  </details>


[Back To Top](<#contents>)

### Item In bag Visual
If a user adds something to their bag, the colour of the icon changes from black to a teal colour, this visual feedback is clear and will let the user know if they have forgotten that there is something in there. Also, the grand total is shown underneath the icon. This is the same for both mobile and desktop users.

  <details><summary>Item In bag Visual</summary>
  
  ![Item In bag Visual - Desktop View](documentation/screenshots/features/iib-desktop.png)

  </details>


[Back To Top](<#contents>)

### Home Page
The home page is the first page a user sees when coming to BookNook. The hero section includes a welcome message a call to action 'Shop Now' which takes the user to the products page. Below, there is a a newsletter signup form. The cursor style changes when a user hovers over the respective sections, letting them know the button is to be clicked and the newsletter is to be filled in.

<details><summary>Home Page - Desktop View</summary>

![Home Page - Desktop View](documentation/screenshots/features/homepage-desktop.png)

</details>

<details><summary>Home Page - Mobile View</summary>

![Home Page - Mobile View](documentation/screenshots/features/homepage-mobile.png)

</details>


[Back To Top](<#contents>)

#### Newsletter Signup
The user need to fill in their name and email and click the button to signup to the newsletter. Once their response is submitted, a success message is shown to the user and they receive an email confirmation. The email includes an unsubscribe link (however it currently does not work). For profile users, the functionality will be explained in the *[profile](<#profile>) section below. If the user enters an email that has already been signed up to the newsletter they will see an error message. Once signed up the user stays on the homepage.

  <details><summary>Newsletter Sign Up Success Message</summary>

  ![Newsletter Sign Up Success Message](documentation/screenshots/features/nl-success.png)

  </details>

  <details><summary>Newsletter Sign Up Error Message</summary>

  ![Newsletter Sign Up Error Message](documentation/screenshots/features/nl-error.png)

  </details>

  <details><summary>Newsletter Sign Up Email</summary>

  ![Newsletter Sign Up Email](documentation/screenshots/features/nlsignup-email.jpg)

  </details>


[Back To Top](<#contents>)

#### Footer
The footer has four sections which include 'Shopping', which includes links to the contact us page, and the faqs, 'Follow Us', which include links to the relevant social media sites for BookNook, currently BookNook has two active pages on Facebook and Instagram, 'Legal', which includes a link to the privacy policy and the 'Copyright' section. The footer can be seen across all pages and is fully responsive.

  <details><summary>Footer - Desktop View</summary>

  ![Footer - Desktop View](documentation/screenshots/features/footer-desktop.png)

  </details>

  <details><summary>Footer - Mobile View</summary>

  ![Footer - Mobile View](documentation/screenshots/features/footer-mobile.png)

  </details>


[Back To Top](<#contents>)

### Products Pages
#### All Products Page
The products page displays both books and accessories and can be sorted by, price, rating and name, all with options of ascending and descending. Above the products, there are two buttons 'Browse by Accessory Category' and 'Browse by Book Genre'. Clicking either of these will display all the categories/genres available currently in the accessories and books selections. Clicking any category or genre will redirect the user to a page with only products in that category/genre. The is also a back to top scroll arrow in the right bottom corner. By the user clicking this button, they do not have to scroll back to the top. On each product card, the user can see the name, rating, price and genre or accessory category. Users can click the genre/category to be redirected to a page displaying products of that genre/category. 

  <details><summary>Products Page - Desktop View</summary>

  ![Products Page - Desktop View](documentation/screenshots/features/products-desktop.png)

  </details>

  <details><summary>Products Page - Mobile View</summary>

  ![Products Page - Mobile View](documentation/screenshots/features/products-mobile.png)

  </details>

  <details><summary>Browse By Genre Buttons - Desktop View</summary>

  ![Browse By Genre Buttons - Desktop View](documentation/screenshots/features/genre-buttons.png)

  </details>

  <details><summary>Browse By Genre Buttons - Mobile View</summary>

  ![Browse By Genre Buttons - Mobile View](documentation/screenshots/features/genre-buttons-mobile.png)

  </details>

  <details><summary>Browse By Category Buttons - Desktop View</summary>

  ![Browse By Category Buttons - Desktop View](documentation/screenshots/features/acategory-buttons.png)

  </details>

  <details><summary>Browse By Genre Category - Mobile View</summary>

  ![Browse By Category Buttons - Mobile View](documentation/screenshots/features/acategory-buttons-mobile.png)

  </details>

  <details><summary>Sort Buttons</summary>

  ![Sort Buttons](documentation/screenshots/features/sort-buttons.png)

  </details>
  

[Back To Top](<#contents>)

#### All Books Page
The all books page diaplays all books currently being sold on BookNook, as there are no accessories in this section, the user can only 'Browse by Genre', it has the same functionality as on the all products page.

  <details><summary>All Books Page - Desktop View</summary>

  ![All Books Page- Desktop View](documentation/screenshots/features/all-bookspage.png)

  </details>

  <details><summary>All Books Page - Mobile View</summary>

  ![All Books Page - Mobile View](documentation/screenshots/features/all-bookspage-mobile.png)

  </details>


[Back To Top](<#contents>)

#### All Accessories Page
The all accessories page diaplays all accessories currently being sold on BookNook, as there are no books in this section, the user can only 'Browse by Category', it has the same functionality as on the all products page.

  <details><summary>All Accessories Page - Desktop View</summary>

  ![All Accessories Page- Desktop View](documentation/screenshots/features/all-accessoriespage.png)

  </details>

  <details><summary>All Accessories Page - Mobile View</summary>

  ![All Accessories Page - Mobile View](documentation/screenshots/features/all-accessoriespage-mobile.png)

  </details>


[Back To Top](<#contents>)

#### By Genre/ By Category Pages
These two pages are identical in their layout but each only display their product category. The pages display all genres/categories that have products associated with them in a list. Under each genre/category name is a row of the products. For genres/categories that have multipl books arrows appear to the left and right for users to be able to scroll. This style of page was chosen for the site as it is visually appealing for users to see all the different genres/categories on the same page but separately grouped. These pages have the sorting buttons ad with the other product pages. It should be noted that when sorting by name, price or rating, products are sorted within each group not across the page.

  <details><summary>By Genre Page - Desktop View</summary>

  ![By Genre Page- Desktop View](documentation/screenshots/features/bygenre-desktop.png)

  </details>

  <details><summary>By Genre Page - Mobile View</summary>

  ![By Genre Page - Mobile View](documentation/screenshots/features/bygenre-mobile.png)

  </details>

  <details><summary>By Category Page - Desktop View</summary>

  ![By Category Page- Desktop View](documentation/screenshots/features/by-category-desktop.png)

  </details>

  <details><summary>By Category Page - Mobile View</summary>

  ![By Category Page - Mobile View](documentation/screenshots/features/by-category-mobile.png)

  </details>

  <video width="320" height="240" controls>
    <source src="documentation/screenshots/features/bygenre-mobile-video.mp4" type="video/mp4">
    By Genre Page example of carousel.
  </video>


[Back To Top](<#contents>)

### Product Detail
This page shows all the information about a particular product. Depending on the product type, book or accessory, the relevant information is displayed. Users also have the option to 'Add to Wishlist' or 'Save For Later'. If the user clicks add to wishlist, a modal will appear asking them which wishlist they want to add it to or if they would like to create a new wishlist. Once confirmed a pink heart is displayed in the top left corner of the product image. Also the button itself changes to 'Remove from Wishlist' which if they press, removes the item from the wishlist.
The save for later button, add the item to the users Saved Items and redirects the user to the bag to see said item.

<details><summary>Product Detail - Desktop View</summary>

![Product Detail- Desktop View](documentation/screenshots/features/product-detail-desktop.png)

</details>

<details><summary>Product Detail - Mobile View 1</summary>

![Product Detail- Mobile View 1](documentation/screenshots/features/product-detail-mobile1.png)

</details>

<details><summary>Product Detail - Mobile View 2</summary>

![Product Detail- Mobile View 2](documentation/screenshots/features/product-detail-mobile2.png)

</details>

[Back To Top](<#contents>)

#### Reviews
The reviews section is located on the product detail below the product. Only users who have purchased the item and have an account can review the item. Reviews can be edited and deleted. There is also a total review count.

<details><summary>Reviews Section - Desktop View</summary>

![Reviews Section- Desktop View](documentation/screenshots/features/reviews-section-desktop.png)

</details>

<details><summary>Product Detail - Mobile View</summary>

![Reviews Section- Mobile View](documentation/screenshots/features/reviews-section-mobile.png)

</details>

### Bag
The Bag displays all items the user has added. In the bag, the name, the quantity, the price. There are buttons for the user to proceed to checkout.

<details><summary>Bag - Desktop View</summary>

![Bag- Desktop View](documentation/screenshots/features/bag-desktop.png)

</details>

<details><summary>Bag - Mobile View 1</summary>

![Bag- Mobile View 1](documentation/screenshots/features/bag-mobile1.png)

</details>

<details><summary>Bag - Mobile View 2</summary>

![Bag- Mobile View 1](documentation/screenshots/features/bag-mobile2.png)

</details>

[Back To Top](<#contents>)

#### Saved For Later
User can save as many products as they want in the Saved for Later. It is intended for people who intend to purchase soon but maybe not immediately. Users can add items from their saved for later to their bag and vice versa. They can also remove the item entirely.

<details><summary>Saved For Later - Desktop View</summary>

![Saved For Later - Desktop View](documentation/screenshots/features/saveforlater-desktop.png)

</details>

<details><summary>Saved For Later - Mobile View</summary>

![Saved For Later - Mobile View](documentation/screenshots/features/saveforlate-mobile.png)

</details>

[Back To Top](<#contents>)

### Checkout
The checkout page is where the user fills out their personal information, address and credit card details. If they are a logged in user they can save their details to their profile and updated them on the their profile for speedier checkouts in the future.  

<details><summary>Checkout - Desktop View</summary>

![Checkout - Desktop View](documentation/screenshots/features/checkout-desktop.png)

</details>

<details><summary>Checkout - Mobile View 1</summary>

![Checkout - Mobile View 1](documentation/screenshots/features/checkout-mobile.png)

</details>

<details><summary>Checkout - Mobile View 2</summary>

![Checkout - Mobile View 2](documentation/screenshots/features/checkout-mobile2.png)

</details>

<details><summary>Checkout - Mobile View 3</summary>

![Checkout - Mobile View 3](documentation/screenshots/features/checkout-mobile3.png)

</details>

[Back To Top](<#contents>)

### Order Processing
Once an order has been submitted, there is a loading overlay.

<details><summary>Order Overlay</summary>

![Order Overlay](documentation/screenshots/features/order-overlay.png)

</details>

[Back To Top](<#contents>)

### Checkout Success
Once and order has been confirmed, the user is taken to the checkout success page where they can see all necessary information regarding their order. They are shown a confirmation message, telling them an email has been sent to them. From this page they can navigate to their profile if they are logged in, the products page or the forum.

<details><summary>Checkout Success - Desktop View</summary>

![Checkout Success - Desktop View](documentation/screenshots/features/checkout-success-desktop.png)

</details>

<details><summary>Checkout Success - Mobile View 1</summary>

![Checkout Success - Mobile View 1](documentation/screenshots/features/checkout-success-mobile.png)

</details>

<details><summary>Checkout Success - Mobile View 2</summary>

![Checkout Success - Mobile View 2](documentation/screenshots/features/checkout-success-mobile2.png)

</details>

<details><summary>Confirmation Email Part 1</summary>

![Confirmation Email 1](documentation/screenshots/features/order-email1.jpg)

</details>

<details><summary>Confirmation Email Part 2</summary>

![Confirmation Email 2](documentation/screenshots/features/order-email2.jpg)

</details>


[Back To Top](<#contents>)

### Profile
All information on the profile page is on one page. By default the Delivery Details section is what is open when a user click on any profile button.

### Delivery Details
In this section, the users' delivery details are displayed. If they wish to update them, they just need to press the button. A form will appear below and once submitted, their details are updated straight away.

<details><summary>Delivery Details - Desktop View</summary>

![Delivery Details - Desktop View](documentation/screenshots/features/profile-dd-desktop.png)

</details>

<details><summary>Delivery Details - Mobile View</summary>

![Delivery Details - Mobile View](documentation/screenshots/features/profile-dd-mobile.png)

</details>


[Back To Top](<#contents>)

### Personal Bio
This section displays the users bio and favourite books, much like the section before, if they wish to update their bio, they click update and a form will appear. They can write something about theirselves and choose their favourite books from a list. They can select more than one, but currently you have to hold down shift to select more than one at the same time.

<details><summary>Personal Bio - Desktop View</summary>

![Personal Bio - Desktop View](documentation/screenshots/features/profile-pb-desktop.png)

</details>

<details><summary>Personal Bio - Mobile View</summary>

![Personal Bio - Mobile View](documentation/screenshots/features/profile-pb-mobile.png)

</details>


[Back To Top](<#contents>)

### Order History
This section displays the users order history, listing all the orders they have made whilst logged in. The styling for mobile views and desktop views is different as the desktop view had poor UX on a mobile screen. Users can click on the order number to be shown the order confirmation page.

<details><summary>Order History - Desktop View</summary>

![Order History - Desktop View](documentation/screenshots/features/profile-oh-desktop.png)

</details>

<details><summary>Order History - Mobile View</summary>

![Order History - Mobile View](documentation/screenshots/features/profile-oh-mobile.png)

</details>


[Back To Top](<#contents>)

### My Reviews 
This section displays all the reviews the user has written, users can edit and delete their reviews right on the profile page and upon submission of an edited post, it will update both on the profile and the reviews section on the product detail. As with all other delete buttons on BookNook, pressing the delete button will open up a Delete Confirmation Modal. Only once pressing delete in the modal will their review be delete. Below the displaying of reviews, users will see a list of products left to review. By clicking the Review Product button, they will be taken to the product detail page, where they can submit their review.

<details><summary>My Reviews - Desktop View 1</summary>

![My Reviews - Desktop View 1](documentation/screenshots/features/profile-mr-desktop1.png)

</details>

<details><summary>My Reviews - Desktop View 2</summary>

![My Reviews - Desktop View 2](documentation/screenshots/features/profile-mr-desktop2.png)

</details>

<details><summary>My Reviews - Mobile View 1</summary>

![My Reviews - Mobile View 1](documentation/screenshots/features/profile-mr-mobile1.png)

</details>

<details><summary>My Reviews - Mobile View 2</summary>

![My Reviews - Mobile View 2](documentation/screenshots/features/profile-mr-mobile2.png)

</details>

[Back To Top](<#contents>)

### My Wishlists
This section displays the users Wishlists, each wishlist is displayed on a card, and list the items vertically. Each wishlist item displays the image, the name and the price. If the wishlist item is a book, it will also display the author. The name of the item is a link to its respective product detail page. Users can either delete a wishlist item or delete an entire wishlist. In both cases, a Delete confirmation modal is opened, and the item or wishlist is only deleted if confirmed in the modal. It should be worth noting that if a user removes all items from a wishlist, it does not automatically delete, it stays available until it the wishlist has been deleted.

<details><summary>My Wishlists - Desktop View</summary>

![My Wishlists - Desktop View](documentation/screenshots/features/profile-mw-desktop.png)

</details>

<details><summary>My Wishlists - Mobile View</summary>

![My Wishlists - Mobile View](documentation/screenshots/features/profile-mw-mobile.png)

</details>


[Back To Top](<#contents>)

### Wishlists vs Saved For Later
Also I would like to explain why I have both Save For Later functionality and Wishlist functionality. After much research I found that Wishlists are more for long-term interest, users can save items they are considering for future purchase, without any immediate intention to buy. Whereas Saved For Later is more for short-term interest, with users generally adding items to their Saved Items that they plan to buy in the near future. Wishlists are for organisation and can be shared with friends and family for potential gifts. BookNook doesn't currently have the functionality to send wishlists to others, but it is something I would implementas soon as there is more traction in the user levels. Also Saved for Later has the ease of being able to move items back and forth from the bag to Saved Items. Ideally a store would want to make a sale, rather than a product go unpurchased but the convenience of the Save For Later functionality means that users have a higher chance of purchasing those items than if there were no Save For Later functionality.


[Back To Top](<#contents>)

### My Saved Items
This section displays the users with their items that they have Saved For Later. They can increase or decrease the quantity as long as it doesn't go lower than 1 or higher than 99. Unfortunately, at the time of writing this I have just seen a slight bug and it is too late to change this. The functionality is there, however the '+' and '-' buttons serve as sort of enter keys. So a user can enter a number with a keyboard or use the arrows inside of input rectangle and save it by pressing the plus or minus button. Aside from that a user can remove and Shared Item by pressing the remove button.

<details><summary>My Saved Items - Desktop View</summary>

![My Saved Items - Desktop View](documentation/screenshots/features/profile-msi-desktop.png)

</details>

<details><summary>My Saved Items - Mobile View</summary>

![My Saved Items - Mobile View](documentation/screenshots/features/profile-msi-mobile.png)

</details>


[Back To Top](<#contents>)

### Forum Interaction
This section displays the users with all their interaction in the forum. When a user clicks the section button, thress buttons are displayed, 'Threads', 'Posts', 'Forum'. The forum button takes them to the forum. The threads button opens up the threads section, where users can see all the thread they have written byt category. On each thread card, the thread itself is truncated to 30 words and has an edit and delete button. The edit button, takes the user to the Edit Thread page, where they ccan edit their thread and then be taken back to the Forum Interaction section in the profile.

If a user clicks on the posts button, they will be shown all the posts they have written with the thread title on each card too.  By pressing the edit button on the user will be taken to the edit post page, where they will be once again redirected back to the forum interaction section of the profile. If a user clicks on the thread title, they will be taken to the post list to see the thread in its' entirety.

Both threads and posts have Delete confirmation modals and it should be noted that the edit and delete buttons on the posts and threads were purposefullt designed differently. They act as a visual representation to the user that one if for posts and one is for threads.

<details><summary>Forum Interaction - Desktop View 1</summary>

![Forum Interaction - Desktop View 1](documentation/screenshots/features/profile-fi-desktop1.png)

</details>

<details><summary>Forum Interaction - Desktop View 2</summary>

![Forum Interaction - Desktop View 2](documentation/screenshots/features/profile-fi-desktop2.png)

</details>

<details><summary>Forum Interaction - Desktop View 3</summary>

![Forum Interaction - Desktop View 3](documentation/screenshots/features/profile-fi-desktop3.png)

</details>

<details><summary>Forum Interaction - Mobile View 1</summary>

![Forum Interaction - Mobile View 1](documentation/screenshots/features/profile-fi-mobile1.png)

</details>

<details><summary>Forum Interaction - Mobile View 2</summary>

![Forum Interaction - Mobile View 2](documentation/screenshots/features/profile-fi-mobile2.png)

</details>

<details><summary>Forum Interaction - Mobile View 3</summary>

![Forum Interaction - Mobile View 3](documentation/screenshots/features/profile-msi-mobile3.png)

</details>


[Back To Top](<#contents>)

### Rewards and Benefits
This section displays perks given to users.

<details><summary>Rewards and Benefits - Desktop View</summary>

![Rewards and Benefits - Desktop View](documentation/screenshots/features/profile-rb-desktop.png)

</details>

<details><summary>Rewards and Benefits - Mobile View</summary>

![Rewards and Benefits - Mobile View](documentation/screenshots/features/profile-rb-mobile.png)

</details>


[Back To Top](<#contents>)

### Newsletter
This section displays whether or not a user is signed up to the newsletter. If users aren't already signed up to the newsletter, they can sign up on the form. If they are signed up they can click the Unsubscribe button which will be confirmed by a success message.

<details><summary>Newsletter - Desktop View 1</summary>

![Newsletter - Desktop View 1](documentation/screenshots/features/profile-n-desktop1.png)

</details>

<details><summary>Newsletter - Desktop View 2</summary>

![Newsletter - Desktop View 2](documentation/screenshots/features/profile-n-desktop2.png)

</details>

<details><summary>Newsletter - Mobile View 1</summary>

![Newsletter - Mobile View 1](documentation/screenshots/features/profile-n-mobile1.png)

</details>

<details><summary>Newsletter - Mobile View 2</summary>

![Newsletter - Mobile View 2](documentation/screenshots/features/profile-n-mobile2.png)

</details>


[Back To Top](<#contents>)

### Downloads
This Downloads page has links to downloadable content onlhy available for users with accounts..

<details><summary>Downloads - Desktop View</summary>

![Downloads - Desktop View](documentation/screenshots/features/profile-rc-desktop.png)

</details>

<details><summary>Downloads - Mobile View</summary>

![Downloads - Mobile View](documentation/screenshots/features/profile-rc-mobile.png)

</details>


[Back To Top](<#contents>)

### Forum
The Forum is visually different from other pages on BookNook. The buttons are orange. This was a design desicion to make it stand out against the navy. The layout of the forum is very similar to the profile. Whilst the buttons are a differernt colour. The overall look of the page is inline with BookNook. Users can see different threads by click between the category buttons. Only staff member can add categories to the forum, in the front end or via admin. To see a full post list (thread with all the replies), the user must click on the thread title. On the forum page, signed in users can add threads by clicking the Create New Thread button. A model opens where the user need to write a thread title and content. 

<details><summary>Forum - Desktop View</summary>

![Forum - Desktop View](documentation/screenshots/features/forum-desktop.png)

</details>

<details><summary>Forum - Mobile View</summary>

![Forum - Mobile View](documentation/screenshots/features/forum-mobile.png)

</details>

[Back To Top](<#contents>)

#### Post List
On the post list users can see the intial thread and all its replies. On this page users can edit and delete their own threads and posts. Much like in the profile, to edit a post or thread, the user is taken to the Edit Post, or Edit Thread page respectively. Upon succussful submission on edited content, from both the edit post and edit thread pages, the user is redirected back to the thread they were on. 

<details><summary>Post List - Desktop View</summary>

![Post List - Desktop View](documentation/screenshots/features/post-list-desktop.png)

</details>

<details><summary>Post List - Mobile View</summary>

![Post List - Mobile View](documentation/screenshots/features/post-list-mobile.png)

</details>

[Back To Top](<#contents>)

### Product Management
On the product management page, staff can add new products to the store. There is a separate form for each type of product. Staff can also edit any product  by clicking the edit button on either the products page or the product detail page. Once they click Edit, they are taken to either the Edit Book or Edit Accessory Form and once they submit a valid form they are taken to the product detail page of the item they are editing. Next to the edit buttons are Delete buttons that trigger a Delete Confirmation Modal if clicked. These buttons or only visible to logged in staff members.

<details><summary>Product Management - Add Book - Desktop View</summary>

![Product Management - Add Book - Desktop View](documentation/screenshots/features/pm-ab-desktop.png)

</details>

<details><summary>Product Management - Add Book - Mobile View</summary>

![Product Management - Add Book - Mobile View](documentation/screenshots/features/pm-ab-mobile.png)

</details>

<details><summary>Product Management - Add Accessory - Desktop View</summary>

![Product Management - Add Accessory - Desktop View](documentation/screenshots/features/pm-as-desktop.png)

</details>

<details><summary>Product Management - Add Accessory - Mobile View</summary>

![Product Management - Add Accessory - Mobile View](documentation/screenshots/features/pm-aa-mobile.png)

</details>

<details><summary>Product Management - Edit Book/Accessory</summary>

![Product Management - Add Book/Accessory](documentation/screenshots/features/edit-product.png)

</details>

[Back To Top](<#contents>)

### Contact Us
On the Contact Us, the user can see BookNook's phone number and email address, as well an enquiry form. The content of these messages is stored in the backend and can be viewed in Admin.

<details><summary>Contact Us</summary>

![Contact Us](documentation/screenshots/features/contact.png)

</details>

[Back To Top](<#contents>)


### Contact Success
If a valid form is submitted, the user is redirected to the Contact Success page, where they are also shown a message conveying to them that the enquiry was successful and BookNook will reply to them in due course. On this page there are also two buttons to got to the shop or the forum.

<details><summary>Contact Success</summary>

![Contact Success](documentation/screenshots/features/contact-success.png)

</details>

[Back To Top](<#contents>)

### About Us
This page tells users where BookNook came from and what it is about. At the bottom, users can navigate to the products page or the forum.

<details><summary>About Us</summary>

![About Us](documentation/screenshots/features/about.png)

</details>

[Back To Top](<#contents>)
  
### Partners
This page tells users what charities we work witha nd there is a Call To Action button at the bottom, encouraging users that wish to, to partner with us. The button leads the user to the Contact Us page.

<details><summary>Partners</summary>

![Partners](documentation/screenshots/features/partners.png)

</details>

[Back To Top](<#contents>)

### FAQs
This page displays some common question and answers users may have about the shopping experience. If the cannot find their answer, there is a button down below to the Contact Us page.

<details><summary>FAQs</summary>

![FAQs](documentation/screenshots/features/faqs.png)

</details>

[Back To Top](<#contents>)

### Privacy Policy
This page displays the privacy policy for BookNook.

<details><summary>Privacy Policy</summary>

![Privacy Policy](documentation/screenshots/features/pp.png)

</details>

[Back To Top](<#contents>)

### Login

<details><summary>Login</summary>

![Login](documentation/screenshots/features/login-desktop.png)

</details>

[Back To Top](<#contents>)

### Signup

<details><summary>Signup</summary>

![Signup](documentation/screenshots/features/signup.png)

</details>

[Back To Top](<#contents>)

### Logout

<details><summary>Logout</summary>

![Logout](documentation/screenshots/features/signout.png)

</details>

[Back To Top](<#contents>)

### 404 Error Page

<details><summary>404 Error Page</summary>

![404 Error Page](documentation/screenshots/features/404-desktop.png)

</details>

[Back To Top](<#contents>)

## Future Features
I aimed to introduce some of the following features into my project. They are labelled as 'Won't Have' on my GitHub kanban board.

### Social Login
- Allow users to sign up to BookNook with social login options, such as Google and Facebook. This enhances the user experiance by a faster sign up time and an easier experience. Having to remember lots of password for different sites can deter new users.

### Discounts & Offers
- Offer users discount and offers can encourage more sales, not only this but special offers for account holders to show our appreciation for their business.

### Email Notifications
- Implement email notifications for when wishlist items go on sale and if any products in their saved for later are low on stock. 

### Forum Moderation
- Create a front-end admin page for forum moderation, enabling staff to review threads and posts. The forum threads and posts don't have to be approved to be seen by others. Letting staff see all content on an easy to use would make the forum better for everyone.

- Also giving a select few users to be moderators for specific categories or threads depending on how popular BookNook is.

### Reporting Inappropriate Content
- Allow users of the site to report any reviews, threads or posts for inappropriate content by a simple where they state the reason why. The content would be hidden from view until it is reviewed.

### Likes/Saves on Threads and Posts
- Allow users to like threads and posts and save threads and posts others have written to their profile.

### Active Rating
- Use the ratings users give in their reviews for each product.

### Increase Parameters to Search and Filtering
- Incorporate authors into the sorting buttons and search criteria.

### Styling
- Improve the styling of the forum, primarily the post list.

### Implement Reading Challenges
- For users with profiles, implement challenges that users can opt-in to.

### Events
- Add events for all users to see but only logged-in user to book. Events with publishers, authors, book-signings etc.

### Subscription Service
- Allow profile users to sign up to a subscription service where BookNook uses their favourite books section to curate books to send every month for a fee.


[Back To Top](<#contents>)

# Testing
Please refer [**_here_**](TESTING.md) for more information about testing on BookNook.


# Deployment
  ## Amazon Web Services
  - ### S3 Bucket
    1. Make an account on [Amazon Web Services](https://aws.amazon.com/).
    2. Type `s3` into the search bar and click on S3.
    3. Click `Create Bucket`.
      - Enter a bucket name. 
      - Select `ACLS enabled`. _Access control lists (ACLs) determines who can specify access to objects._
      - Select `Bucket owner preferred`. _New objects written to this bucket are owned by the bucket owner._
      - Deselect `Block all public access`. _This might result in objects within becoming public._
      - Check the box to acknowledge the risk of public access.
      - Click `Create Bucket`.
    
    [Back To Top](<#contents>)

    ### Enable Static Web Hosting
    1. Click on bucket name.
    2. Click on `Properties` tab.
    3. Scroll down to the `Static Web Hosting` section and click `Edit`.
    4. Click `Enable`.
    5. Enter `index.html` into the Index document input.
    6. Enter `error.html` into the Error document input.
    7. Click `Save Changes`.

    [Back To Top](<#contents>)

    ### Change CORS configuration
    1. Click on the `Permissions` tab.
    2. Click `Edit`.
    3. Add the following code for the CORS settings.
        ```
        [
          {
            "AllowedHeaders": ["Authorization"],
            "AllowedMethods": ["GET"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": []
          }
        ]
        ```
    4. Click `Save Changes`.

    [Back To Top](<#contents>)

    ### Add a Bucket Policy
    1. On the `Permissions` tab, scroll to the `Buclet Policy` section and click `Edit`.
    2. Click `Policy Generator`. _This will open in a new tab._
    3. For the policy type, select `S3 Bucket Policy`.
    4. For the principal, enter `*`.
    5. For the actions, select `GetObject`.
    6. Return to the bucket policy editor in the other tab, click the button under the heading 'Bucket ARN'.
    7. Paste the `ARN` into the `Amazon Resource Name (ARN) input`.
    8. Click `Add Statement`.
    9. Scroll down and click `Generate Policy`.
    10. Copy all the text in the pop up.
    11. Return to the policy editor in the other tab and paste in the policy code.
    12. Edit the `Resource` by adding `/*` to the end, to allow all acces to all the objects within the bucket.
    13. It should look like this: __replacing YOUR_ARN with your ARN__
        ```
        {
            "Version": "2012-10-17",
            "Id": "Policy1720032710777",
            "Statement": [
                {
                    "Sid": "Stmt1720024120521",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "YOUR_ARN/*"
                }
            ]
        }

        ```
    14. Scroll to the bottom and click `Save Changes`.

    [Back To Top](<#contents>)

    ### Edit the Access Control List (ACL) 
    1. On the `Permissions` tab , scroll down to the `Acces Control List (ACL)` section and click `Edit`.
    2. Click `List` in the Everyone row.
    3. Click the checkbox to indicate that you understand the effects of the changes.

    [Back To Top](<#contents>)

    ### Creating AWS Groups, Policies and Users
    **Create a user group**
      1. Search for `IAM` in the search bar at the top.
      2. Click on `IAM`.
      3. Click `User Groups` on the left navigation menu.
      4. Click `Create Group`.
      5. Enter a group name, for example `manage-_name of your bucket_`.
      6. Click `Create user group`.
  
    **Create a Policy**
      1. Click `Policies` on the left navigation menu.
      2. Click `Create Policy`.
      3. Click the `JSON` tab.
      4. Click the `Actions` dropdown.
      5. Click the `Import Policy`.
      6. Search for `S3`.
      7. Select `AmazonS3FullAccess`.
      8. Click `Import Policy`.
      9. Search for `S3` in the top search bar.
      10. __Right click__ `S3` and open in a new tab.

      In the new tab:
      11. Select you bucket.
      12. Click `Copy ARN`.
      13. Go back to the previous tab.

      In the previous tab:
      14. Add your `ARN` in quote to the `Resource` list __twice__, for the second one add `/*` after the ARN.
        15. It should look like this: __replacing YOUR_ARN with your ARN__
          ```
          {
              "Version": "2012-10-17",
              "Statement": [
                  {
                      "Sid": "Statement1",
                      "Effect": "Allow",
                      "Action": [
                              "s3:*"
                      ],
                      "Resource": [
                                "YOUR_ARN",
                                "YOUR_ARN/*"
                      ]
                  }
              ]
          }
          ```
      16. Scroll to the bottom and click `Next`.
      17. Enter a policy name and description. _For example, bucketname-policy , Access to S3 for projectname static and media files_.
      18. Scroll down and click `Create Policy`.
      19. You'll see a success message.

      [Back To Top](<#contents>)

      **Attach the policy to the group**
      1. Click `User groups` on the left navigation menu.
      2. Click on your group.
      3. Click the `Permissions` tab.
      4. Click the `Add permissions` dropdown.
      5. Click `Attach policies`.
      6. In the search bar, search for your policy. _You can search by the policay name or description you entered earlier._
      7. Select the checkbox beside your policy.
      8. Click `Attach policies`.

      [Back To Top](<#contents>)

      **Create a User**
      1. Click `Users` in the navigation menu on the left.
      2. Click `Create user`.
      3. Enter a user name.
      4. Click `Next`.
      5. Select the group you created previously.
      6. Click `Next`.
      7. Scroll down and click `Create user`.

      [Back To Top](<#contents>)
      
      **Create an Access Key**
      1. Click on your new user.
      2. Click `Security credentials`.
      3. Scroll down to the `Access keys` section and click `Create access key`.
      4. Select `Application running outside AWS`.
      5. Click `Next`.
      6. Click `Create access key`.
      7. Scroll down and click `Download .csv file`.
      8. Click `Done`.
      9. Open the .csv file in any text editor _such as Notepad or TextEdit_. It will look like this:
          ```
          Access key ID,Secret access key
          AKIA2FQOVY528F82BMXS,G4N7OfTaq/nfw8lz4R2hpRpILoqlS0BTv/3vCapl

          ```
          __Note: the values are separated by a comma, not a forward slash__ _Also these are not my AWS ACCES KEY ID or ACCESS KEY._
      10. Use the values in your Heroki config vars, for example:
          - AWS_ACCESS_KEY_ID = AKIA2FQOVY528F82BMXS
          - AWS_SECRET_ACCESS_KEY = G4N7OfTaq/nfw8lz4R2hpRpILoqlS0BTv/3vCapl


    [Back To Top](<#contents>)

    ### Django AWS Connect
      - Install the following packages to use AWS S3 Bucket in Django:

        ```
        pip install boto3
        pip install django-storages
        ```
      - Freeze those using the following command:
        `pip freeze --local > requirements.txt`
      - Add storages to your INSTALLED APPS in settings.py, it should look like this:
        ```
        INSTALLED_APPS = [
          `storages`,
        ]
        ```
      - Check if AWS variables are present in your env.py and if environment variable paths are in settings.py:
        ```
        import os
        from pathlib import Path
        import dj_database_url

        if os.path.isfile('env.py'):
          import env
        ```
      - Check if DATABASES are set up to connect with Heroku PostgreSQL server in product and SQLite3 in local development:
        ```
        if 'DATABASE_URL' in os.environ:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        ```
      - Set up media and static file storage in settings.py:
        ```
        STATIC_URL = "/static/"
        STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

        MEDIA_URL = "/media/"
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        ```
      - Set up S3 Bucket configuration in settings.py:
        ```
        if 'USE_AWS' in os.environ:
          # Cache control
          AWS_S3_OBJECT_PARAMETERS = {
              'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
              'CacheControl': 'max-age=94608000',
          }

          # Bucket Configuration
          AWS_STORAGE_BUCKET_NAME = '_bucketname_'
          AWS_S3_REGION_NAME = 'eu-west-2'
          AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
          AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
          AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

          # Static and media files
          STATICFILES_STORAGE = 'custom_storages.StaticStorage'
          STATICFILES_LOCATION = 'static'
          DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
          MEDIAFILES_LOCATION = 'media'

          # Override static and media URLs in production
          STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
          MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
        ```
      - Create a 'custom_storages.py' file in the root directory and add the following:
        ```
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage


        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

        ```
      - AWS S3 Bucket is now connected.
    

    [Back To Top](<#contents>)  

  ## Stripe API
  1. Make an account on [Stripe](https://stripe.com/gb).
  2. Navigate to the Stripe dashboard.
  3. Obtain your test API keys
  4. Use these keys:
    - STRIPE_PUBLIC_KEY = Publishable Key
    - STRIPE_SECRET_KEY = Secret Key
    - STRIPE_WH_SECRET = Webhook Signing Secret
  
  [Back To Top](<#contents>)

  ## Gmail API

  1. Enable 2-step verification in Gmail.
  2. Navigate to Security > App Passwords and generate a 16-character password for 'Mail' with a custom name.
  3. Save the generated password.
  4. Use these keys in Heroku:
    - EMAIL_HOST_USER = user's Gmail email address
    - EMAIL_HOST_PASS = user's 16-character API key
  
  [Back To Top](<#contents>)

  ## To Deploy on Heroku
  The site was developed using [VS Code](https://code.visualstudio.com/). All commit messages were pushed to [Github](https://github.com/) using the VS Code terminal. The finished project was deployed in [Heroku](https://dashboard.heroku.com/).

  Before starting the process on [Heroku](https://dashboard.heroku.com/), you first need to enter 'pip freeze > requirements.txt' in the terminal in your IDE. This adds a list of dependencies to your requirements.txt file needed for deployment. Commit these changes and push to GitHub before you deploy.

  You can also update your 'requirements.txt' file once you have already deployed to Heroku, by entering 'pip freeze > requirements.txt'. Don't forget to commit your changes and push to GitHub.

  The process of deploying to [Heroku](https://dashboard.heroku.com/) is as follows:

  1. Login to [Heroku](https://dashboard.heroku.com/) (or create an account).

  <details><summary>Heroku Step 1</summary>
  
  ![Heroku Step 1](documentation/screenshots/deployment/heroku-one.png)

  </details>
  
  2. In the top right hand corner there is a button 'New' that releases a dropdown menu, where you need to click 'Create a new  app'.

  <details><summary>Heroku Step 2</summary>
  
  ![Heroku Step 2](documentation/screenshots/deployment/heroku_two.png)

  </details>
  
  3. On the next page, you will need to add a name for your app and input what region you are in. Bear in mind that each app name is unique therefore you may need to try some different options out. Once you have decided on an app name and selected which region you are in. Click 'Create app'

  <details><summary>Heroku Step 3</summary>
  
  ![Heroku Step 3](documentation/screenshots/deployment/heroku_three.png)

  </details>
  
  4. On the next page, click the 'Settings' tab. Once you have clicked on the settings tab, click 'Reveal Config Vars' in the 'Config Vars' section. Next you will need to add values:

  | **Key**                  | **Value**                                      |
  |--------------------------|------------------------------------------------|
  | AWS_ACCESS_KEY_ID        | Insert your AWS access key ID here             |
  | AWS_SECRET_ACCESS_KEY    | Insert your AWS secret access key ID here      |
  | DATABASE_URL             | Insert your PostgreSQL database URL here       |
  | EMAIL_HOST_PASSWORD      | Insert your Email host password here           |
  | EMAIL_HOST_USER          | Insert your Email host username here           |
  | SECRET_KEY               | Any random secret key                          |
  | STRIPE_PUBLIC_KEY        | Insert your Stripe public key here             |
  | STRIPE_SECRET_KEY        | Insert your Stripe secret key here             |
  | STRIPE_WH_SECRET         | Insert your Stripe webhook secret here         |
  | USE_AWS                  | Set to True                                    |
  | DISABLE_COLLECTSTATIC    | 1 (temporary; can be removed for final deployment) |


  <details><summary>Heroku Step 4 - Settings Tab</summary>
  
  ![Heroku Step 4 - Settings Tab](documentation/screenshots/deployment/heroku_four_settings.png)

  </details>

  <details><summary>Heroku Step 4 - Config Vars Section</summary>

  ![Heroku Step 4 - Config Vars Section](documentation/screenshots/deployment/heroku_four_config.png)

  </details>
  
  5. In your IDE terminal, you need to type the following code to install the project requirements:

  - pip install gunicorn~=20.1
  - pip install -r requirements.txt
  - pip freeze --local > requirements.txt
  
  6. Next, create an env.py file at the root level directory, which must contain the following:

    - import os
    - 
    - os.environ.setdefault("DATABASE_URL", "CI database URL")
    - os.environ.setdefault("SECRET_KEY", " Your secret key")
  
  7. Next, create a file at the root level directory called Procfile. In this file enter:
    -  web: gunicorn my_project.wsgi
    - Replace my_project with your Django app name.

  8. Next, in your settings.py file, set DEBUG = 'DEVELOPMENT' in os.environ

  By doing this Debug will bet set to false in Heroku deployed site as there is no environment variable by that name but Debug is set to true whilst developing the project.

    **YOU SHOULD ALWAYS SET DEBUG TO FALSE BEFORE DEPLOYING FOR SECURITY**
  
  9. Add ",'your-deployed-url' " (without the double quotes) to the ALLOWED_HOSTS list in settings.py.

  10. Next, add commit and push your code to [Github](https://github.com/).

  11. Next, on [Heroku](https://dashboard.heroku.com/), you need to go to the 'Deploy' tab. For 'Deployment Method', click 'GitHub'. Search for the repository name you want to deploy and then click connect.

  <details><summary>Heroku Step 11 - Deploy Tab</summary>
  
  ![Heroku Step 11 - Deploy Tab](documentation/screenshots/deployment/heroku_six.png)

  </details>

  <details><summary>Heroku Step 11 - Connect to GitHub</summary>

    This sample repository has already been connected to Heroku so mine will look a little different from yours. However, where you can see 'App Connected to GitHub' on the image, you will see 'Connect to GitHub, next to that you'll be able to search for the repository you want to connect.

  ![Heroku Step 11 - Connect to Github](documentation/screenshots/deployment/heroku_six_connect.png)

  </details>

  12. Scroll down to the sections below, called 'Automatic Deploys' and 'Manual Deploy'. Here you need to choose which option best suits your project. Once selected, click 'Deploy Branch'.

      <details><summary>Heroku Step 12 - Deploy</summary>
      
      ![Heroku Step 12 - Deploy](documentation/screenshots/deployment/heroku_seven.png)

      </details>
  
  The live link can be found here - <a href="https://bn-booknook-017930c30e2f.herokuapp.com/">BookNook</a>


  [Back To Top](<#contents>)

  ## To Deploy Locally on Github
  This project can be cloned or forked in order to make a local copy on your own system.



  ## To Fork the Project
  A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changes can be made to the copy without affecting the original repository. The steps to fork the repository are as follows:

  1. Login to GitHub and locate the repository.

  2. On the right hand side of the page, in line with the repository name, is a button called 'Fork', click on the button to create a copy of the original repository in your GitHub Account.

      <details><summary>How to Fork</summary>
      
      ![How To Fork](documentation/screenshots/deployment/fork.png)

      </details>

  [Back To Top](<#contents>)

  ## To Clone the Project
  The steps to clone a project from GitHub are as follows:

  1. Under the repository’s name, click on the code tab.
  2. Copy the URL under the Clone with HTTPS section.
  3. In an IDE of your choice, open Git Bash.
  4. Change the current working directory to the location of where the cloned directory will be made.
  5. Type 'git clone' then paste the URL copied from GitHub.
  6. Upon pressing enter, the local clone will be created.

      <details><summary>How to Clone</summary>

      ![How To Clone](documentation/screenshots/deployment/clone.png)

      </details>
  
  ## Local Deployment
  
  After cloning or forking the project, follow these steps to run it locally:

  1. Install the necessary packages found within the requirements.txt file:
    `pip install -r requirements.txt`

  2. Create a new file called envy.py at the root level and include the following environment variables:

    ```
    import os

    os.environ['STRIPE_PUBLIC_KEY'] = 'Stripe public key'
    os.environ['STRIPE_SECRET_KEY'] = 'Stripe secret key'
    os.environ['STRIPE_WH_SECRET'] = 'Stripe webhook secret key'
    os.environ['SECRET_KEY'] = 'Your secret key'
    ```
  3. Run the Django App by typing the following in the terminal: 
    `python manage.py runserver`
  
  4. Stop the app once it is loaded by pressing CTRL+C (Windows/Linux) or ⌘+C (Mac).
  
  5. Make migrations by typing:
    ```
    python manage.py makemigrations --dry-run
    python manage.py makemigrations
    ```

  6. Migrate the data by typing:
    ```
    python manage.py migrate --plan
    python manage.py migrate
    ```

  7. Create a superuser by typing:
    `python manage.py createsuperuser`

  8. Start the Django app again by typing:
    `python manage.py runserver`


  [Back To Top](<#contents>)

# Technologies Used
## Frontend
* [HTML](https://html.spec.whatwg.org/): Essential for structuring website content, providing the foundational framework for web pages.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html): Vital for styling and layout, ensuring the site is visually appealing and user-friendly.
* [Bootstrap](https://getbootstrap.com/): Used to create a responsive design and incorporate prebuilt style and components, simplifying the design process.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Used for dynamic content and interactive features.
* [jQuery](https://jquery.com/): Utilized for simplifying DOM manipulation and handling AJAX requests.

[Back To Top](<#contents>)

## Backend
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/): Formed the backend development with server-side functionality and data management.
* [SQLite 3](https://www.sqlite.org/): Used as the database system in production for storing user data, model data and transaction records.
* [PostgreSQL](https://www.postgresql.org/): The database system used for development.
* [psycopg2](https://pypi.org/project/psycopg2/): The PostgreSQL adapter for Python, used to connect Django with the PostgreSQL database.

[Back To Top](<#contents>)

## Authentication & Security
* [Django Allauth](https://docs.allauth.org/en/latest/): Implemented for user authentication, registration, and account management.
* [Stripe](https://stripe.com/): Used for handling secure payment processing.
* [Gmail API](https://developers.google.com/workspace/gmail/api/guides): Utilized for email delivery and management.

[Back To Top](<#contents>)

## Deployment
* [Heroku](https://www.heroku.com/): Deployed the application using Heroku for scalability and ease of deployment.
* [Amazon Web Services](https://aws.amazon.com/): Used for storing static and media files.
* [Gunicorn](https://gunicorn.org/): Used as the WSGI HTTP server for running the Django application.

[Back To Top](<#contents>)

## Accessibility & Testing
* [WAVE](https://wave.webaim.org/): Used for web accessibility evaluation.

[Back To Top](<#contents>)

## Design & Documentation
* [LucidChart](https://www.lucidchart.com/): Used for creating Entity Relationship Diagrams.
* [Balsamiq](https://balsamiq.com): Used for the wireframes.
* [XML Sitemaps](https://www.xml-sitemaps.com/): Generated for improving SEO and site navigation.
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used for creating a privacy policy for the application. 

[Back To Top](<#contents>)

## Additional Tools
* [Visual Studio Code](https://code.visualstudio.com/): The code editor used for deployment.
* [Git](https://git-scm.com/) & [GitHub](https://github.com/): A repository hosting service for version control and project management.
* [Font Awesome](https://fontawesome.com/): Used for icons.
* [Google Fonts](https://fonts.google.com/): Utilized for custom web fonts.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used for enhancing the appearance of Django forms.
* [Pillow](https://pypi.org/project/pillow/): Used for image processing.
* [TinyPNG](https://tinypng.com/): Used for optimizing images.
* [Favicon](https://favicon.io/): Used for generating the favicon.


[Back To Top](<#contents>)

# Credits
- I used the "Boutique Ado" walkthrough from the course content as a foundation to implement necessary features for an e-commerce store. I customized the models, views, and templates to develop BookNook.

* Social Media Meta Tags: [CSS-Tricks](https://css-tricks.com/essential-meta-tags-social-media/?form=MG0AV3)
* SEO keyword list: [Moz](https://moz.com/?form=MG0AV3)
* Ajax: [W3 Schools](https://www.w3schools.com/jquery/jquery_ajax_intro.asp) and [jQuery Documentation](https://api.jquery.com/jQuery.ajax/) and [Stack Overflow](https://stackoverflow.com/questions/28417781/jquery-add-csrf-token-to-all-post-requests-data)
* Profile 'show content' buttons: [Aveva Help](https://aveva-help.industrial-software.com/AVEVA%20OMI%20SDK/ShowContentAPI.html)
* Profile Page, Favourite Books Selection: [Select2](https://select2.org/)
* Books Dataset: [Kaggle](https://www.kaggle.com/datasets/dk123891/books-dataset-goodreadsmay-2024)
  - I pruned this dataset to get the 103 books in my fixtures. The dataset provided me with book names, description, authors, image URLs, ratings, authors and genres. Through Python I got the image files and I had to manually look up the ISBNs.
* Accessory Names, Images, Descriptions and Hero Image: [Copilot](https://copilot.microsoft.com/)
* update_product.py and create_products_from_books.py: [Copilot]( https://copilot.microsoft.com/)
  -	Due to the way my models were set up for my products and books when I attempted to load the genres fixtures file followed by  books fixtures file, there was a problem as there were not any products for those books. I did some research but ultimately couldn’t quite get what to do therefore I asked the Microsoft AI and it gave me the code for ‘update_product.py’. When that worked, I created the second file, ‘create_products_from_books.py’ using the previous code to apply it to all the books.
* download_images.py: [Stack Overflow]( https://stackoverflow.com/questions/30229231/python-save-image-from-url) and [Copilot]( https://copilot.microsoft.com/)
  -	I used the Microsoft AI to make sure the code I had from stack overflow would work for me. It made some tweaks.



## Content
* Wireframes: [Balsamiq](https://balsamiq.com)
* Favicon: [Favicon](https://favicon.io/)
* Fonts: [Google Fonts](https://fonts.google.com/)
* Icons: [Font Awesome](https://fontawesome.com/)
* Colour Palettes: [Coolors](https://coolors.co/)
* Mock-up: [Am I Responsive](https://ui.dev/amiresponsive)
* Chrome for Developers: [Dev Tools](https://developer.chrome.com/docs/devtools)
* Images: [Freepik](https://www.freepik.com/), [Copilot](https://copilot.microsoft.com/)
* Styling: [Bootstrap](https://getbootstrap.com/)


[Back To Top](<#contents>)

# Acknowledgements

BookNook marks the completion of my Portfolio 5 Project for the Full Stack Software Developer Diploma at Code Institute. I am deeply grateful to my parents and sister for their unwavering support and encouragement throughout this journey, especially during the challenging moments. I extend my heartfelt thanks to my Code Institute mentor, Precious Ijege, for his invaluable guidance and advice, as well as the Slack community and everyone at Code Institute for their constructive feedback and assistance. A special thanks also goes to Emma Lamont, whom I had the pleasure of meeting at a hackathon, for her insights and helpful advice on this project.

