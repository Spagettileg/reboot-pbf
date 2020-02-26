# Re-Boot | Test Analysis & Report 

Access main [READEME](https://github.com/Spagettileg/reboot-pbf/blob/master/README.md) file

View [Re-Boot](https://reboot-pbf.herokuapp.com/) as a deployed project in Heroku

## Navigate to detail
[Introduction](#introduction)    

[Systems Based Testing](#systems-based-testing) || [Python3](#python3) | [Coverage](#coverage) | [Travis CI](#travis-ci)

[Manual Testing](#manual-testing) || [Registration Testing](#registration-testing) | [Password reset testing](#password-reset-testing) | [Product Testing](#product-testing) | [Navigation Testing](#navigation-testing) 

[Code Validation](#code-validation) || [Responsiveness and Rendering](#responsiveness-and-rendering) | [Browser Compatability](#browser-compatability) | [Known Bugs](#known-bugs)

## Testing

### Introduction
A combination of system based and manual testing processes was applied to this project to ensure the UXD was upheld. To make sure the data was correctly loaded, images would be successfully rendered and dynamic links would accurately support the user to navigate through this application.

The software has been thoroughly tested in many ways. JavaScript and its associated functions have all undergone extensive manual testing. JS hint was used to help validate the Javascript code.

Django `DEBUG` has helped identity logic errors when trying to get `Python3` application, `sqlite3` (development db) and `postgreQSL` (production db) to all correctly interact. For your information, `sqlite3` serves to provide backup to `postgreSQL` in the event `postgreSQL` is not available.

Manual testing has been based upon a walkthrough of key process steps the User will experience. This is coupled with process alignment to CRUD (Create, Read, Update & Delete).

All possible user actions were mimicked to put the tester in the shoes of the user.

### Systems Based Testing 
- CRUD Operations tested = **READ**
 
- To view the existence of Re-Boot app in sqlite3 database, run the following command in the ubuntu bash console:
`sqlite3 db.sqlite3`

followed by `sqlite> .databases`

Result = `main: /home/ubuntu/environment/reboot-pbf/db.sqlite3`

- Django `DEBUG = True`to ensure real time debugging of code

- To ensure project development code would successfully render in the web browser, run the following command:
`python3 manage.py runserver $IP:$PORT`
 
Result:

```
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2020 - 10:14:00
Django version 3.0.2, using settings 'reboot.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
```

#### Python3 
To run the existing Python tests:

1. Activate your virtual environment
 
2. Enter the following command in the `ubuntu bash` terminal:
`python manage.py test`

3. To run the tests within a specific app only, then key the following command in the `ubuntu bash` terminal:
`python manage.py test <app name here>`. Results of test(s) will show in the console

**Important**: The `python` component assumes you are working with a windows operating system. Your `python` command may differ, such as `python3` or `py`

#### Coverage
[Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) was used to provide alerts on tests that were complete and tests that remained oustanding. It's not always possible to achieve 100% success, yet Re-Boot excellent performance is supported by a good range of tests per app. 

How to run coverage
1. Activate your virtual environment
 
2. In the terminal enter the following command: 
`coverage html`

3. htmlcov directory is automatically created in the root directory. Proceed to open this directory
4. Find index.html file and click open
5. Run index.html file in the browser to see the summary output. View can be modified by using the search filter i.e. key `accounts` to narrow search result to all files sitting in the `accounts` app

#### Travis CI
- [Travis](https://docs.travis-ci.com/) was used throughout the unit testing of this project to provide continuous integration analysis with the deployed site

- A `markdown` format helps create a url link that you need to copy and paste into the `README.md` document. The link injects a real time status of all intregation tests run by Travis

- Create a new `.travis.yml` file in the root directory

For Django, the following code is required to help produce a Travis status visual display in `README.md` document

```
language: python
python:
    - "3.6.7"
install: "pip install -r requirements.txt"
script:
    - SECRET_KEY="Whatever" ./manage.py test
```

### Manual Testing
##### Registration Testing

###### •	Username (registration.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Key url address in web browser
2.	Click on 'register' in the navbar
3.	Click in 'username' field 
4.	Key in username (max character length = 150)
5.	If empty fields exist when clicking 'Register', then user will get error message with request to complete missing data
6.	If username already taken by another user, then warning message appears to invite user for a different username
7.	Click in 'email address' field 
8.	Key in email address (no limit on character length)
9.	If empty fields exist when clicking 'Register', then user will get error message with request to complete missing data
10.	If email address already taken by another user, then warning message appears to invite user for a different email address
11.	Once all information has been successfully validated then user to click 'Register' button
12.	If user has already registered then they can click on a link to move to login screen

###### •	Password (registration.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.  Click in 'password' field (placeholder message support user with data requirements)
2.	If empty fields exist when clicking 'Register', then user will get error message with request to complete missing data
3.	If password already taken by another user, then warning message appears to invite user for a different password
4.	User is then invited to re-key their password (placeholder message support user with data requirements)
5.	If empty fields exist when clicking 'Register', then user will get error message with request to complete missing data
6.	If re-keyed password does not match, then warning message appears to invite user re-key password to ensure a match
7.  Click 'Register' button to complete the registration process
8.  If user has already registered then they can click on a link to move to login screen

###### •	Username (login.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Key url address in web browser
2.	Click on 'Login' in the navbar
3.	If user has selected login by mistake, they can click on a link to move to register screen
4.	Click in 'username' field (placeholder text helps the user with data entry)
5.	Key in username 
6.	If empty fields exist when clicking 'Log in', then user will get error message with request to complete missing data
7.	If username does not match registered user details, then warning message appears to invite user for a different username

###### •	Password (login.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	If user has selected login by mistake, they can click on a link to move to register screen 
2.  Click in 'Password' field (placeholder text helps the user with data entry)
3.	Key in password 
4.	If empty fields exist when clicking 'Log in', then user will get error message with request to complete missing data
5.	If password does not match registered user details, then warning message appears to invite user for a different password
6.  Click 'Log in' button to complete the authentication process

##### Password reset testing

###### •	Reset form (password_reset_form.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE** 
1. User can access password reset function either by login page or MyReBoot, if the user is already registered 
2. Click either a reset link or button to move to dedicated password reset screen
3. User to enter a valid email address

###### •	Reset done form (password_reset_done.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE** 
1. Confirmation message to user stating an email will be sent direct to their specified email address with guidance on securely resetting their passowrd 

###### •	Reset email form (password_reset_email.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE** 
1. Upon completion of the password reset form, the user should view their emai inbox. Also check their spam folder too    
2. Email from Re-Boot will provide a link 
3. User to click the link to move to a secure environment for their password reset

###### •	Reset confirm form (password_reset_confirm.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE** 
1. User is invited to create a new password and then re-key the same password for security purposes 
2. Click in 'password' field (placeholder message support user with data requirements)
3. If empty fields exist when clicking 'Change my password', then user will get error message with request to complete missing data
4. If password already taken by another user, then warning message appears to invite user for a different password
5. User is then invited to re-key their password (placeholder message support user with data requirements)
6. If empty fields exist when clicking 'Change my password', then user will get error message with request to complete missing data
7. If re-keyed password does not match, then warning message appears to invite user re-key password to ensure a match
8. Click 'Complete my password' button to complete the registration process

###### •	Reset complete form (password_reset_complete.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE** 
1. User will receive confirmation message that their password has successfully reset
2. Click 'Log in' button
3. User to initiate login process with new password

##### Product Testing
###### •	BootShop Page (products.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1. User to click on 'BootShop' in navbar 
2.	All Users should see 2 different options
    - Juniors
    - Adults
3. Product summary cards appear with following content:
    - Customer category: 'Juniors' or 'Adults'
    - Product image
    - Product make (brand)
    - Product size
    - Product price (£5.00 for juniors & £10.00 for adults)
4. Click on 'Read More' button, if further product information is required
5. Screen view is the same for both logged in and logged out users, at this stage

*Observation*: A tablet device portrait view appears to have pushed all product images outside of their respective recipe card space. As a fix, the number of cards in a row has been reduced from 4 to 3 by adjusting bootstrap grid from `row-cols-md-4` to `row-cols-md-3`. 	

###### •	Detailed Product View (productdetail.html) tests
- CRUD Operations tested = **CREATE, READ, UPDATE & DELETE**
1.  All Users will be presented with an individual product card containing the following information:
    - Customer category: 'Juniors' or 'Adults'
    - Product image
    - Product make (brand)
    - Product size
    - Product colour
    - Product studs (Screw in or moulded)
    - Product quality (Brand New, Almost New and Used Boots)
    - Product price
    - Rugby Icon graphic 

*Observation*: Both product and rugby icon images were too large and disproportionate to remainder of recipe detail view. Fix created to set height and width of images to 200px (12.5rem)      
2.  Should the rugby boot product information be readily accepted by the unregistered user, then they have the chance to foramlly register to proceed with a purchase of their chosen product

3.	A logged in user can follow next steps, as follows:
    - Confirm quantity of product being purchased. As each donated product is unique, then the user needs to ensure that `1` is present  
    - Click on 'Add To Cart' 
    - Cart contents page reveals products in scope for purchase
    - Product card now shows a delete button, in case the user no longer wished to proceed with purchase
        - User to key `0`in quantity input box and click 'Delete'
        - If product deleted, then the shopping cart will reduce by -1, but not less than zero   
    - If more than one product is held within the cart, a running total appears to help the user understand total cost
    - Click 'Checkout' button to proceed to confirm users payment details

4.	Logged in users will get a summary view of their chosen product in the checkout page, buthe delete button has now disappeared. If the user is still unsure on their purchase they can click on the browser back tab to the cart content page to delete their product entry   

5.  Payment details in the checkout page appear under 2 sections. All fields are required to be completed:
    - Personal Information
        - Full name
        - Phone number
        - Country
        - Postcode
        - Town or city
        - Street Address1
        - Street Address2
        - County
    - Card Information
        - Credit card number
        - Security code (CVV)
        - Month (card expiry)
        - Year (card expiry)

6. Once all system validation check on data have been coompleted, then user to click 'Submit Payment'  

*Observation*: For development purposes, Stripe recognises card number 4242424242424242 and a security code of 111. User need s to make sure the Card expiry month and year are current and not historical, as the latter will realise an error message 

7. Successful purchase will realise a `You have successfully paid` message and user will then be routed to the home page

###### •	MyReBoot Page > Donate boots (create_product.html) tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Go to home page an sign in
2.	Click on 'MyReBoot' in the navbar
3.	Read MyReBoot dashboard and click 'Donate' button
4.	Boot donation details are captured in a form using the following required data fields: 
    - Make (Boot brand)
    - Category (Junior or Adult category to support the BootShop choices)
    - Customer (Junior or Adult for product card ID)
    - Size (Boot size)
    - Colour (Boot colour, supported by a boot image)
    - Studs (Screw in or moulded)
    - Quality (Brand New, Almost New & Used Boots)
    - Price (£5.00 for juniors & £10.00 for adults)
    - Image (clear picture of donated boots)
5. Click on 'Submit' button 
6. Confirmation message appears for the user to announce the donated boots have been added to the BootShop

##### Navigation Testing
###### •	Navbar tests
- CRUD Operations tested = **CREATE, READ, UPDATE & DELETE**
1.	Hover on 'Re-Boot' navbar brand for the cursor to change to a pointer design    
2.	Click on ‘Re-Boot’ navbar brand from anywhere within the website
3.	User will be routed back to home page
4.	`Home` selector provides the same functionality as the navbar brand. Both will return the user to the home page from anywhere within the Re-Boot app
5.  `About` selector provides a navbar dropdown function for the following:
    - `Re-Boot explained`- provides a detailed insight and purpose on the Re-Boot app
    - `Juniors` - for pricing and boot size conversion data
    - `Adults` - for pricing and boot size conversion data
    - `Boot Quality` - summary narrative on 3 different thresholds of permitted donated rugby boot quality
        - Click 'View FAQ's' for more information on accepted thresholds of donated boot quality    
6. `BootShop` selector provides a navbar dropdown function for the following:
    - 'Juniors` collection of donated rugby boot products
    - `Adults` collection of donated rugby boot products
7. 'Help' selector provides a navbar dropdown function for the following:
    - `FAQ's` series of questions and answers targeted to help users understanding of Re-Boot 
        - Click 'Get in touch' button for user to raise a question with Re-Boot, if not covered in FAQ's page
    - `Contact Us` form created to enable user to send message direct to Re-Boot. Other means of connecting with Re-Boot are also available
        - Click 'Submit Enquiry' for user to send email diret to Re-Boot   
8. `Search` user can enter a partial or whole product brand name. Results are sourced from current Bootshop stock  
9. `MyReBoot` logged in users are personally greeted. Dashboard design allows the user to donate unwnated rugby boots, create a blog post message and reset their password
10. `Logout` logged in users click on selector narrative to formally log out of Re-Boot
11. `Register` all users can click on selector narrative to commence the Re-Boot registration process
12. `Login` all users can click on selector narrative to commence the Re-Boot login process
13. 'Cart' icon for a shopping cart positioned to far right of navbar. A product counter appears to top-right of cart when user starts adding products to the cart. Confirmed product purchases are removed from the cart  

*Observation*: The presence of all navbar options clearly takes up considerable estate space. Therefore, the navbar does collapse in mobile view only with a hamburger icon on show. Full navbar menu appears when icon is clicked    

###### •	Homepage introduction 'Why Re-Boot?' tests
- CRUD Operations tested = **READ**
1.	Go to home page
2.	Reasons to be cheerful are x4 full responsive paragraphs
3.	Click on 'Learn More' button
4.	User is routed to `Re-Boot Explained` 

###### •	Homepage Quick Step Guide tests
- CRUD Operations tested = **READ**
1.	Go to home page
2.	x4 steps for user to follow
3.	Step 1 - Browse Stock. Links to both junior and adult boot products
4.	Step 2 - Register & Login. Link to registration page
5.	Step 3 - Donate. Function is accessed by logged in users via their MyReBoot page
6.	Step 4 - Purchase. Function is accessed by logged in users via the BootShop

###### •	Homepage Latest Arrivals tests
- CRUD Operations tested = **READ**
1.	Go to home page
2.	3 product cards on show that includes Boot image, quality status, boot make, size, colour, stud type and price
3.	Click on 'See More Juniors Boots' or 'See More Adults Boots' buttons to access the BootShop

###### •	Blog post tests
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Go to home page an sign in
2.	Click on 'MyReBoot' in the navbar
3.	Read MyReBoot dashboard and click 'Blog' button
4.	Create a new blog post by completing data fields:
    - Title
    - Author
    - Content (Blog detail)
    - Image. User can source from local machine (not mandatory)
    - Tag (meta)
    - Published date. Auto-populated at the time of creating the Blog post 
5. Click 'Save' button
6. Confirmed blog post that includes title, author, content, image, tag, published date and views
7. User has option to 'Edit Post' with abutton click or return 'Back to Blog' with a button click
8. 'Edit Post' allows the user to make adjustments to their orignal blog post. View number will increase by 1 once edit has been saved
9. 'Back to Blog' will route the user to the central blog forum where all blog posts are on show

###### •	Footer links tests - Social Media
- CRUD Operations tested = **READ**
1.	Go to footer section
2.	Click social media icons (LinkedIn & Facebook)
3.	All Users are passed through to website authors’ actual live pages

###### •	Footer links tests - Trading
- CRUD Operations tested = **READ**
1.	Go to footer section
2.	Click on 'For Juniors'
3.	User is routed to all junior products that appear in current BootShop stock
4.	Click on 'For Adults'
5.	User is routed to all adult products that appear in current BootShop stock

###### •	Footer links tests - Site Links
- CRUD Operations tested = **READ**
1.	Go to footer section
2.	Click on 'About'
3.	User is routed to 'Re-Boot Explained' that appears as a dropdown feature in the navbar
4.	Click on 'Contact'
5.	User is routed to 'Contact Us' that appears as a dropdown feature under 'Help'
6.	Click on 'Cookies'
7.	User is routed to a dedicated page on cookies and how they are used
8.	Click on 'FAQ's'
9.	User is routed to 'FAQ's' that appears as a dropdown feature under 'Help'
10. Click on 'Privacy Policy'
11.	User is routed to a dedicated page on site privacy and how Re-Boot serves to protect their registered members
12.	Click on 'Terms & Conditions'
13.	User is routed to a dedicated page on Re-Boots' rules for use of their website

### Code Validation

Code       | Url Link                    | App / Directory          | Filename                     | Outcome | Comments
-----------|-----------------------------|--------------------------|------------------------------|---------|---------
HTML5      |https://validator.w3.org     |Accounts                  |login.html                    |Pass     |Jinja templating language used = ok     
HTML5      |https://validator.w3.org     |Accounts                  |password_reset_complete.html  |Pass     |Jinja templating language used = ok        
HTML5      |https://validator.w3.org     |Accounts                  |password_reset_confirm.html   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Accounts                  |password_reset_done.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Accounts                  |password_reset_email.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Accounts                  |password_reset_form.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Accounts                  |profile.html                  |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Accounts                  |registration.html             |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Blog                      |blogpostform.html             |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Blog                      |blogposts.html                |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Blog                      |postdetail.html               |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Cart                      |cart.html                     |Pass     |p stray end tag reported,but all ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Checkout                  |checkout.html                 |Pass     |Jinja templating language used = ok  
HTML5      |https://validator.w3.org     |Home                      |adults.html                   |Pass     |Stray end tag reported,but all ok.Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |bootquality.html              |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |contact.html                  |Pass     |Legend attribute replaced by h3. Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |cookie.html                   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |explained.html                |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |faqs.html                     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |index.html                    |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |juniors.html                  |Pass     |Stray end tag reported,but all ok.Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |privacy.html                  |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Home                      |terms.html                    |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Products                  |create_product.html           |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Products                  |productdetail.html            |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Products                  |products.html                 |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Templates                 |base.html                     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Templates > Peripheral    |navbar.html                   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org     |Templates > Peripheral    |footer.html                   |Pass     |Jinja templating language used = ok

Code       | Url Link                    | App / Directory          | Filename                     | Outcome | Comments
-----------|-----------------------------|--------------------------|------------------------------|---------|---------
Python3    |http://pep8online.com        |Accounts                  |test_app.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |test_forms.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |backends.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |forms.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |urls_reset.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Accounts                  |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |test_app.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |test_forms.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |test_models.py                |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |forms.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Blog                      |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |contexts.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Cart                      |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |test_forms.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |test_models.py                |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |forms.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Checkout                  |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |contexts.py                   |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Home                      |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |test_forms.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |test_models.py                |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |test_views.py                 |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |admin.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |apps.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |forms.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |models.py                     |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |urls.py                       |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Products                  |views.py                      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Root Directory            |custom_storages.py            |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Root Directory            |env.py                        |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com        |Root Directory            |manage.py                     |Pass     |All convention errors corrected = ok

Code       | Url Link                    | App / Directory          | Filename                     | Outcome | Comments
-----------|-----------------------------|--------------------------|------------------------------|---------|---------
CSS3       |https://jigsaw.w3.org/       |Static                    |style.css                     |Pass     |W3C CSS Validator results - CSS level 3 + SVG - negative padding -1rem triggered a warning message = ok
Javascript |https://jshint.com/          |Static                    |stripe.js                     |Pass     |No errors found
Javascript |https://jshint.com/          |Checkout                  |checkout.html                 |Pass     |Code recognised by Stripe.com = ok    

## Responsiveness and Rendering
Chrome DevTools together with a selection of mobile, table and desktop devices were relied upon through the entire software development cycle. A key objective was to test both the rendering and responsiveness of the software application against multiple screen resolutions and web browser platforms. Any bugs identified were debugged in real time with special observations noted in a [testing matrix control document](https://github.com/Spagettileg/reboot-pbf/tree/master/tests).

The Re-Boot application has been tested by students from the Slack community, together with friends and family members. Feedback on what worked well and what did not was recorded and suitable corrections to the code were keyed.

In the final analysis, this application can be passed as fully responsive across all devices that participated in testing.

## Browser Compatability

The following browsers were used in testing the Re-Boot application. Internet Explorer was out of scope for testing due to obsolete capability

platform | version
---------|--------
Chrome   |80.0.3987.87
Edge     |44.18362.449.0
Firefox  |74.0.2
Safari   |12.4.5
Opera    |66.0.3515.72

## Known Bugs

1. SweetAlert2 continually generates a warning message in the browser console. Unable to find a fix, however, the bug is not affecting the performance of the Re-Boot website

`SweetAlert2: Unknown parameter "type"` 