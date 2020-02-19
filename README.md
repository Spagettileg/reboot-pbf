[![Build Status](https://travis-ci.com/Spagettileg/reboot-pbf.svg?branch=master)](https://travis-ci.com/Spagettileg/reboot-pbf)

# Re-Boot | Online exchange for new and used rugby boots 
###### Full Stack Frameworks with Django - Code Institute 

[Re-Boot](https://reboot-pbf.herokuapp.com/) was designed, built and deployed by Paul Friel as his final project for the Code Institute Full Stack Web Development diploma. 

Re-Boot is a non-profit making product exchange portal that provides a secure hub for the recyling of good quality rugby boots. The website targets the rugby playing community through keeping the cost of participation to an inexpensive level.  

A marketplace is created by the registered customer through donating unwanted rugby boots. For juniors, foot growth is the main reason for changing their boots, whereas adults may look to change for improved performance or manage issue of wear & tear. Irrespective of age or gender, Re-Boot aims to serve a rugby playing community with low-cost and good quality replacement boots at a fraction of the retail price.     

Once registered, customers will enjoy secure access to their own 'MyReBoot' webpage where the logged in user can donate unwanted rugby boots, create a blog post and reset their Re-Boot password.     

Furthermore, a reduced carbon footprint can be achieved through avoiding the purchase of brand new rugby boots and shift to product reuse to reduce unecessary landfill waste.


## Demo
A live demo of [Re-Boot](https://reboot-pbf.herokuapp.com/) can be found.

## Navigate to detail
[UXD Considerations](#uxd-considerations) || [User](#user) | [Business](#business) | [Next Stage Generation](#next-stage-generation) | [Wireframes](#wireframes) | [User Stories](#user-stories) | [CSS Framework](#css-framework) | [Colour Palette](#colour-palette) | [Typography](#typography) | [Icon Graphics](#icon-graphics)  

[Information Architecture](#information-architecture) || [Application Framework](#application-framework) | [Database Selection](#database-selection) | [Data Models](#data-models)

[Technologies Applied](#technologies-applied) || [Databases](#databases) | [Languages](#languages) | [Libraries](#libraries) | [Tools](#tools) | [Hosting](#hosting)

[ReBoot Summary Functions](#reboot-summary-functions) 

[Features](#features) || [Features Left to Implement](#features-left-to-implement)

[Tests](#tests)

[Deployment](#deployment) || [Local Deployment](#local-deployment) | [Deployment To Heroku](#deployment-to-heroku)

[Credits](#credits) || [Content](#content) | [Media](#media) | [Acknowledgements](#acknowledgements)

## UXD Considerations
### User & Business Objectives

#### User
- The registered customer belongs to a community of rugby enthusiasts
- Value for money product offerings made available
- Access to well known brands to support anyy concerns upon product quality
- Fulfil a moral obligation to not throw away good quality products and seek to recycle
- Start a blog conversation upon availability of rugby boots not yet appearing on Re-Boot website, etc
- Happy to browse current stock, without obligation to purchase
- Assured that personal details are secure from unauthorised access

#### Business
- Only registered users can donate and purchase Re-Boot products to help deliver assurance on personal data security and trading
- Creation of a MyReBoot account is only for registered users to ensure bonafide credentials
- Provide a simple and intuitive site for the user to click, search, read, create, add, update & delete own data. Access levels are determind through whether user has successfully registered 
- Use customer feedback to further improve the offerings of Re-Boot
- Monitor product demand to help generate positive marketing campaigns 

#### Next Stage Generation
- Increase product density through expanding scope of sports footwear genres
- Leverage footfall data to attract commercial online advertising, with resultaqnt revenues used to maintain and grow website
- Affiliate with professional sport organisations through embracing product recyle credentials
- Create social media channels to promote 'Re-Boot'

### Wireframes
My wireframe mock-up designs have been created in [Balsamiq](https://balsamiq.com/) to showcase the 'Re-Boot' website responsivenesson mobile, tablet and desktop devices.

•	[Home](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Home_v1.zip)

•	[About](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/About_v1.zip)

•	[BootRoom](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/BootShop_v1.zip)

•	[Help](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Help_v1.zip)

•	[Search](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Search_v1.zip)

•	[Register & Login](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/RegisterandLogin_v1.zip)

•	[MyReBoot](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/MyReBoot_v1.zip)

•	[Cart](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Cart_v1.zip)


### User Stories
> I need an app that provides quick and intuitive access to understand how to donate & purchase either new or used rugby boots [READ]

> I want detailed information on make, size, colour and stud type of a replacement rugby boot [READ]

> My personal information must be secure and password protected {CREATE, READ & UPDATE]

> My donated rugby boot information must be kept in a secure environment and protected from unauthorised edit & or deletion [UPDATE & DELETE]

> Obsolete rugby boot donations can be removed from my profile by an authorised user [READ & DELETE]

> To have access to a blog function to understand availability of replacement rugby boots that may not be appearing on Re-Boot website [CREATE, READ & UPDATE]

> I would like the opportunity to write a review / provide feedback of my user experience [CREATE, READ & UPDATE]

> I'd like to upload my rugby boot donation by adding make, size, colour, stud configuration and image too [CREATE, READ & UPDATE]

> I would like the flexibility to donate and purchase rugby boots at different times. Replacement boots may not be available at the time of boot donation [CREATE, READ & UPDATE]

> I want to be able to delete unwanted rugby boot products from my shopping cart [DELETE]

> Replacement boots - I'm willing to pay £5.00 for junior boots and £10.00 for adult boots [READ]


### CSS Framework
Bootstrap 4 was the chosen framework for styling my project. I used the bootstrap grid extensively to support responsiveness on mobile, tablet and desktop devices.  

### Colour Palette
Colours used in this project were sourced through consultation with my mentor [Simen Daehlin](simen.dehlin@gmail.com). Essentially, the colours are seeking to capture key attrbutes of rugby through energy, assertiveness and co-ordination.

Colour                       | Hex Code
-----------------------------|----------
Rich Black                   | #001514
White                        | #FFFFFF
Vivid Tangelo (Orange)       | #F26826
Blue Sapphire (Dark Green)   | #135A68
Space Cadet (Dark Blue)      | #21295C

### Typography
Open Sans & Sans Serif fonts were used throughout this project. H1 header was used in the home page to help qualify 'Why Re-Boot?'to the user. Thereafter, H2 & H3 was used for sub-heading narrative. 

Font-weight of 400 & 700 was used to help draw attention to the user for both branding and instruction too.

[Re-Boot](https://github.com/Spagettileg/reboot-pbf/tree/master/plans/art) brand was self-built through use of MS Powerpoint tools.

### Icon Graphics
Font Awesome 5 icon graphics were used in conjunction with Bootstrap 4, primarily to support information page headers

- latest arrivals & boot quality = `fas fa-shoe-prints`
- faq's = `fas fa-comments`
- contact us - `far fa-inbox`
- privacy policy - `fas fa-lock`
- terms & conditions - `fas fa-exclamation-triangle`
- donate rugby boots - `far fa-handshake`
- blog post - `far fa-envelope`


## Information Architecture
### Application Framework
Django application framework was a prerequisite in the design of this project, according to the project brief.

### Database Selection
Django framework is fast, secure and scalable. Provides a dynamic CRUD (create, read, update and delete) interface, configured with admin models and generated via introspection. requiring SQL database 
 - SQLITE3 database was used for development of this project on my local machine  
 - PostgresSQL was used support the full production of the Re-Boot website. An enterprise-level, object-relational DBMS that uses procedural languages like Perl and Python, in addition to SQL-level code  

### Data Models

#### User
A User model used to support this project is the default standard provided by `django.contrib.auth.models`

#### Blog app model
Name            | DB Key              | Field Type    | Validation
----------------|---------------------|---------------|---------------------------------------------
Title           | post.title          | CharField     | max_length=200
Author          | post.author         | CharField     | max_length=75, null=True
Content         | post.content        | TextField     |
Created Date    | post.created_date   | DateTimeField | auto_now_add=True
Published Date  | post.published_date | DateTimeField | blank=True, null=True, default=timezone.now
Views           | post.views          | IntegerField  | default=0
Tag             | post.tag            | CharField     | max_length=30, blank=True, null=True
Image           | post.image          | ImageField    | upload_to="images", blank=True, null=True

- Blog post creation occurs within MyReBoot, once user has logged in  
- Blog images are stored in the `media` directory 

#### Checkout app model
Within the checkout app, `Order` and `OrderLineItem` models hold the data needed for users to create and pay for their orders.

##### Order model
Name              | DB Key          | Field Type    | Validation
------------------|-----------------|---------------|---------------------------------------------
Full name         | full_name       | CharField     | max_length=50, blank=False
Phone number      | phone_number    | CharField     | max_length=20, blank=False
Country           | country         | Charfield     | max_length=40, blank=False
Postcode          | postcode        | CharField     | max_length=20, blank=True
Town or City      | town_or_city    | CharField     | max_length=40, blank=False
Street address 1  | street_address1 | CharField     | max_length=40, blank=False
Street address 2  | street_address2 | CharField     | max_length=40, blank=False
County            | county          | CharField     | max_length=40, blank=False
Date              | date            | DateTimeField |             

- An `Order` model instance is created before any `OrderLineItems`. `OrderLineItems` rely on the `Order` model for a `ForeignKey`.

##### OrderLineItem model
Name     | DB Key   | Field Type                 | Validation
---------|----------|----------------------------|---------------------------------------------
Order    | order    | ForeignKey to Order        | Order, null=False, on_delete=models.CASCADE
Product  | product  | ForeignKey to Product      | Product, null=False, on_delete=models.CASCADE
Quantity | quantity | PositiveSmallIntegerField  | 

- An OrderLineItem instance is created for each unique product in the users cart, linking a users existing Order, product and quantity the user elects to purchase

#### Products app model
Name      | DB Key           | Field Type    | Validation
----------|------------------|---------------|---------------------------------------------
Make      | product.make     | CharField     | max_length=254
Category  | product.category | CharField     | max_length=254, choices=category_choices
Customer  | product.customer | CharField     | max_length=50, choices=category_choices, null=True
Size      | product.size     | IntegerField  | 
Colour    | product.colour   | CharField     | max_length=50
Studs     | product.studs    | CharField     | max_length=50
Quality   | product.quality  | CharField     | max_length=50, null=True
Price     | product.price    | DecimalField  | max_digits=6, decimal_places=2
Image     | product.image    | ImageField    | upload_to='images', blank=True, null=True

- `Category choices` are defined within the `Product` model

## Technologies Applied
### Databases
•	[SQLITE3](https://www.sqlite.org/index.html) provided by Django for a developemnt database
•	[PostgresSQL](https://www.postgresql.org/) provided by Heroku for a production database

### Languages
•	[HTML5](https://html.spec.whatwg.org/multipage/) used as the markup language

•	[CSS3](https://www.w3.org/Style/CSS/) used to style the HTML

•	[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) used mostly for DOM manipulation

•	[Python3](https://www.python.org/) used to run the backend application


### Libraries
•	[Font Awesome](https://fontawesome.com/) v5.11.2 to provide the icon set for Re-Boot website

•	[Google Fonts](https://fonts.google.com/) provided the fonts used throughout the project

•	[jQuery](https://jquery.com/) is used to manipulate the DOM, for example buttons, and showing / hiding elements

•	[Bootstrap4](https://www.bootstrapcdn.com/) v4.4.1 to enable ease of website responsiveness and simplify coding structure


### Tools
•	[AWS Cloud9](https://aws.amazon.com/cloud9/) a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser.

•	[AWS S3 Bucket](https://aws.amazon.com/) provides for secure cloud based repository in storage of website images

•	[Balsamiq](https://balsamiq.com/) is a small graphical tool to sketch out user interfaces, for websites and web / desktop / mobile applications and used to visualise my project through mock-up design.

•	[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) enables the creation, configuration and management of AWS S3

•	[Coverage](https://coverage.readthedocs.io/en/v4.5.x/) for python unittests code coverage measurement

•	[Django](https://www.djangoproject.com/) high-level Python Web framework that encourages rapid development and clean, pragmatic design

•	[Django-Heroku](https://pypi.org/project/django-heroku/) enabling improved deployment of django projects on heroku

•	[Django-Storages](https://django-storages.readthedocs.io/en/latest/) custom storage backending with Django to work with AWS S3 and Boto3

•	[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

•	[GitHub](https://github.com/) is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

•	[Gunicorn](https://pypi.org/project/gunicorn/) enables deployment of the Django project to heroku via UNXI WSGI HTTP Server

•	[Pillow](https://pillow.readthedocs.io/en/stable/) a python imaging library enabling image files to store in database

•	[PIP](https://pip.pypa.io/en/stable/installing/) enabling installation of tools and packages required for this project to function correctly

•	[psycopg2](https://pypi.org/project/psycopg2/) a PostgreSQL production database adapter for Python

•	[Stripe](https://stripe.com/gb) payment platform to validate debit and credit card payments securely

•	[Travis](https://travis-ci.com/) for continuous integration via GitHub and autonomous testing of project code  

•	[Whitenoise](http://whitenoise.evans.io/en/stable/) allowing the web app to serve its own static files


### Hosting
•	[Heroku](https://heroku.com) is used to host the deployed application - 're-boot'

## ReBoot Summary Functions

## Features
### Feature 1 - Registration & Authentication 

•	User has a mandatory requirement to complete the registration & authentication form when clicking on the sites url address 

•	Register & Login data entry requirements include username and password. Where appropriate, data entry governance exists in the form of required attributes meaning all requests for data must be completed prior to access the full Re-Boot website   

•	All usernames and passwords will be unique to avoid unauthorised access to third party boot donations

•	Logged in users will have access to their own Re-Boot webpage with full access rights to donate boots, create a blog post and reset a password  

•	Logout is activated through clicking the 'Logout' narrative positioned in the navbar. The user will then return to Re-Boot homepage

### Feature 2 - Navbar brand logo 

•	Normal html convention rules followed by placing the navbar brand logo 'Re-Boot' in the navbar, at the top left corner. The User has unhindered access to this logo and when clicked, will always return the user to the homepage.  

### Feature 3 - Overview of Re-Boot

•	An elevation statement has been created to promote Re-Boot to the User to set out its purpose, value generators, responsive to user stories and reference to key features

### Feature 4 - Quick Step Guide

•	A read only view created to show the user how best to navigate through Re-Boot via 4 steps    

•	From browse stock > register / login > donate unwanted boots > purchase replacement boots 

### Feature 5 - Latest Arrivals 

•	All users can view latest boot arrivals to whet the users appetite and potentially increase Re-Boot membership numbers   

•	All boots on show are donated by existing Re-Boot members and subject to a self-governing quality classification. New Boots, Almost New and Used Boots 

•	Only registered users can trade in donation and purchase of Re-Boot products

### Feature 6 - Re-Boot explained

•	A detailed insight created to promote Re-Boot to the User to set out its purpose, value generators, responsive to user stories and reference to key features  

### Feature 7 - 'About' > Juniors

•	Pricing set at £5.00 per pair of replacement rugby boots.    

•	Boot size conversion table, including UK & Euro sizing from UK/Euro 8/25 to UK/Euro 2.5/35 inclusive  

### Feature 8 - 'About' > Adults

•	Pricing set at £10.00 per pair of replacement rugby boots.    

•	Boot size conversion table, including UK & Euro sizing from UK/Euro 3/36 to UK/Euro 15/49 inclusive  

### Feature 9 - Boot Quality 

•	Clear and definitive guidelines on donated rugby boot tolerance

    -   New Boots: Original box included
    -   Almost New: Super condition
    -   Used Boots: Worn in, avoiding blisters

•	More detailed information on required quality standards can be viewed in FAQ's page

### Feature 10 - 'BootShop' > Juniors

•	A repository of donated junior rugby boots available for purchase by a registerd user 

•	Each product card includes a juniors name tag, full colour product image, boot make, boot size, price and a 'read more' button to access further product information

### Feature 11 - 'BootShop' > Adults 

•	A repository of donated adult rugby boots available for purchase by a registerd user 

•	Each product card includes a adults name tag, full colour product image, boot make, boot size, price and a 'read more' button to access further product information

### Feature 12 - Favourite recipe tickbox 

•	Logged in user to navigate to either 'Edit Recipe' or 'Add Recipe' page to mark their given recipe as a favourite. A simple tickbox has been created to record the User actions in both the application and cloud database too. Tick for favourite and untick for non-favourite   

•	Summary favourite count statistics can be viewed in the navbar by both logged in and non-logged in users. The cursor has been set to default as the data is only intended for read only purposes   

### Feature 13 - 'Help' > FAQ's 

•	Any user has access to full page of Re-Boot FAQ's

•	FAQ Purpose is to help user navigate through Re-Boot website and to offer support with the process of donating and purchasing rugby boots  

•	If a question cannot be answered in FAQ page, then the user is invited to click a 'get in touch' button. The user is then presented with a contact form. Once completed the form will be sent directly to Re-Boot email address.     

### Feature 14 - 'Help' > Contact us 

•	All users can complete a contact form to alert Re-Boot of any question, concern, note of appreciation, etc  

•	The user is required to complete their full name, email address, brief subject narrative and a detailed comment setting out their query 

•	Find Re-Boot information is also made availabe to the user. Including Re-Boots' address, telephone number, email, business hours, collections data and company vat number 

•	The user is invited to click a 'submit enquiry' button. The form will be sent directly to Re-Boot email address

### Feature 15 - Search 

•	User is requested to key in either a partial or complete rugby boot brand name to initiate a search within the current BootShop   

•	Search function is available for all users. Logged in users will get to proceed to purchase searched products, if required  

•	Leaving the search field blank will result in all available BootShop products being shown to the user

### Feature 16 - MyReBoot page

•	Logged in users are allocated their own portal space to donate rugby boots, create ther own blog message and reset their password  

•	All donated rugby boots added by the logged in user will appear in BootShop portal space and can then be viewed by other registered users  

•	New blog posts will appear in a consolidated blog forum to allow other registered users to read and respond  

•	Password resets are initiated by the registered user. The user will be asked for their email address, where upon a response email is submitted to the user with a link to enable their password to be securely changed       

### Feature 17 - Shopping Cart

•	Logged in users have full access to the BootShop to browse collection of rugby boots for sale  

•	The product detail page includes an 'add to cart' button. Once clicked, the selected product will then appear in the shoping cart. A visible counter will then increment +1 for each product added to the cart 

•	Cart items can be deleted by the user, in the event the user no longer wishes to proceed with a purchase. The user will simply enter a zero value in the input box and click 'delete'. The cart counter will reduce -1, but not less than zero

•	If the user wishes to proceed with their purchase, then a 'checkout' button will be clicked by the user

•	The checkout process requires the logged in user to enter the following information:

    -   Full name
    -   Phone number
    -   Country
    -   Postcode
    -   Town or City
    -   Street Address 1
    -   Street Address 2
    -   County
    
    Followed by payment information:
    
    -   Credit card number
    -   Security code (CVV)
    -   Month (Card Expiry)
    -   Year (Year Expiry)

•	Once user is happy with their data entry, all required fields are completed and validated, then the user can click 'Submit Payment' button 

•	Payment process is managed via Stripe vendor

### Feature 18 - Footer 

•	Provides a social media link to LinkedIn and a link to my Facebook page. Fonts (icons) secured from bootstrap 4 / font awesome 5. The links are wired to the website designers’ respective social media sites    

•	Trading links that enables the user to access either juniors or adults Bootshop. Only logged in users can proceed to donate and purchase Re-Boot products 

•	Site links enable the user to access the following:

    -   'About': Re-Boot explained
    -   'Contact': Send a message to Re-Boot
    -   'Cookies': Information on defintion and usage
    -   'FAQ's': Questions and answers for all users
    -   'Privacy Policy': Re-Boots' position on customer data protection
    -   'Terms & Conditions': Rules that apply to both User and Re-Boot

### Features Left to Implement

- Alternate sporting footwear to be included for a future release
- Add 'for sale' and 'sold' signs on each rugby boot product to help user understand product availability
- Deleted cart items to be reversed by the user, in the event human error was responsible for the original product deletion 
- A dedicated favourite products page that allows the user to import favourite product records into MyReBoot
- Additional sporting categories that relate to Re-Boot customers. The list is will be quite extensive and could be developed by creating a new 'key value' field, per record held in postgresQSL database. For example;
    - `category': "male"`
    - `category': "female"`
    - `category': "professional"`
    - `category': "amateur"`

## Tests
Test analysis and reporting can be viewed in a separate [TESTS.md]() file.

## Deployment

### Local Deployment
This project can be run on your own IDE through following the guidance notes below:

Ensure you have the following tools:
* An IDE such as [AWS Cloud9](https://console.aws.amazon.com/cloud9/home/product), for example. There are others in the marketplace
 
* [PIP](https://pip.pypa.io/en/stable/installing/), [Python 3](https://www.python.org/downloads/) & [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) should be installed on your machine

* [Stripe](https://dashboard.stripe.com/login), [AWS S3](https://s3.console.aws.amazon.com/) and [emailjs](https://www.emailjs.com/) offer free services and are essential in ensuring hinder free access to your website, plus enablement of payments, storage and email services 

Your advised to click the links above for guidance on installation and retrieval of the necessary environment variables.

##### Instructions
1. Save a copy of your GitHub repository located at https://github.com/Spagettileg/reboot-pbf by clicking the "download zip" button at the top of the page, then extract the zip file to your chosen local folder. Alternatively, you can clone the repository with the following command, if you have Git installed on your system

```
git clone https://github.com/Spagettileg/reboot-pbf
```

2. From your preferred IDE, open a new terminal session in the unzip folder or cd to the correct location

3. A virtual environment is recommended for the Python interpreter. Enter the following command:

```
python3 -m .venv venv
```
>NOTE: The `python` part of this command and the ones in other steps below assumes you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`

4. Activate the .venv with the command:
``` 
.venv\Scripts\activate 
```
This command may differ depending on your operating system. Suggest you refer to [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further guidance.

5. If needed, consider upgrading pip locally with
```
pip3 install --upgrade pip
```
6. Install all required modules / packages with the command
```
pip3 -r requirements.txt
```
7. If using AWS Cloud9, create a new file called `env.py` in your IDE root directory. Add the following environment variables, knowing that the sensitive data will not be visible to any other user

```
import os

os.environ.setdefault("SECRET_KEY",'enter key details here')

os.environ.setdefault("AWSC9_HOST",'enter key details here')

os.environ.setdefault("DATABASE_URL",'enter key details here')

os.environ.setdefault("STRIPE_PUBLISHABLE",'enter key details here')

os.environ.setdefault("STRIPE_SECRET",'enter key details here')

os.environ.setdefault("AWS_ACCESS_KEY_ID",'enter key details here')

os.environ.setdefault("AWS_SECRET_ACCESS_KEY",'enter key details here')

os.environ.setdefault("EMAIL_USER",'enter email details here')

os.environ.setdefault("EMAIL_PASS",'enter key details here')
                      
```

8. If using AWS Cloud9, locate the settings.py file and add your environment variables as below. 
```
import os

import dj_database_url

if os.path.exists('env.py'):
    import env

"DATABASE_URL" in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [os.getenv('AWSC9_HOST', 'reboot-pbf.herokuapp.com')]

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')

STRIPE_SECRET = os.getenv('STRIPE_SECRET')

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
```

`AWS C9 HOST` should be the local address for the site when running within your own IDE.

A developemnt environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting `DEBUG` to `True` only when working in development and not on the deployed site.

9. Migrate the admin panel models to create your database template with the terminal commands

`python3 manage.py makemigrations`

`python manage.py migrate` to ensure all tables have been updated into your database  

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:

`python3 manage.py createsuperuser`

11. The app can now be run locally with the following command:

`python3 manage.py runserver $IP:$PORT`

12. App should be running. Now use the local link provided and add /admin to the end of the url address. Login with your superuser account and create instances of new product within the new database.

13. Once instances of new products exist in your database, your local developemnt website will run as expected.

### Deployment to Heroku
The site has been formally deployed to [Heroku](https://reboot-pbf.herokuapp.com/) and the latest version of my application can be found here. The following steps were taken in order to deploy:

Apply the following steps to deploy Re-Boot app to herokus:

1. Create a `requirements.txt` file using the terminal command pip freeze > requirements.txt

2. Create a `Procfile` via the ubuntu bash terminal command `echo web: python3 app.py > Procfile`

3. Key `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub repository

4. Create a new app on the [Heroku](https://dashboard.heroku.com/apps) website by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

5. Your heroku dashboard will then invite you to click on "Deploy" > "Deployment method" and select GitHub

6. Check and confirm the heroku app is linked to the correct GitHub repository

7. Return to your heroku dashboard. Click on "Settings" > "Reveal Config Vars"

8. Complete the following config vars:

Key                      | Value
-------------------------|--------
`AWS_ACCESS_KEY_ID`      | "Enter secret key"
`AWS_SECRET_ACCESS_KEY`  | "Enter secret key"
`DATABASE_URL`           | "postgreSQL database url address"
`DISABLE_COLLECTSTATIC`  | `1`
`SECRET_KEY`             | "Enter secret key"
`STRIPE_PUBLISHABLE`     | "Enter secret key"
`STRIPE_SECRET`          | "Enter secret key"

9. From the command line of your local IDE:

    - Enter the heroku postgres shell
    - Migrate the database models
    - Create your superuser account in your new database
    
Expert guidance on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

10. Return to your heroku dashboard. Click "Deploy". Scroll down to "Manual Deploy". Select the master branch then click "Deploy Branch"

11. Once the build is complete, click the "View app" button provided

12. From the link provided, append `/admin` to the end of the url address. Login with your superuser account and create instances of new products within the new database

13. Where instances of the new products exist in your database, your heroku production site will run as expected

## Credits
- Shoe sizes reported in both UK and Euro systems sourced from [Shoe sizing charts](https://www.shoesizingcharts.com/)  

### Content

### Media
- Rugby boot images were taken from [prodirectrugby](https://www.prodirectrugby.com/)

- Rugby background and banner images were taken from [pixabay](https://www/pixabay.com) and [Olga Guryanova](https://unsplash.com/photos/ft7vJxwl2RY), both royalty free stock image libraries

- [Favicon](https://github.com/Spagettileg/reboot-pbf/tree/master/plans/art) image was created by myself

- Images for Browse, Donate, Purchase, Feedback and Empty Shopping Cart [pixabay](https://www/pixabay.com)

- User register image [flickr.com](www.flickr.com/photos )

- Junior and adult rugby images [clipart](https://www.clipartof.com/gallery/clipart/rugby.html)

### Acknowledgements

**Simen Daehlin** (Current Mentor) - For clear guidance on opportunities to improve website design using improved normal HTML & CSS conventions. Simpler coding practice makes for better output. 
**Theo Despoudis** (Previous Mentor) - For his guidance in previous milestone projects and helping understand the finer detail of Javascript & Python coding 

Slack Community and the following experts to keep me honest and focused.

**Stephen Moody** - Tutor,
**Michael Park** - Tutor &
**Samantha Dartnell** - Tutor 

*This is for educational use.* 