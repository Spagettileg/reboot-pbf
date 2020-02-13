[![Build Status](https://travis-ci.com/Spagettileg/reboot-pbf.svg?branch=master)](https://travis-ci.com/Spagettileg/reboot-pbf)

# Re-Boot | Online exchange for new and used rugby boots 
###### Full Stack Frameworks with Django - Code Institute 

[Re-Boot] was designed, built and deployed by Paul Friel as his final project for the Code Institute Full Stack Web Development diploma. 

[Re-Boot] is a non-profit making product exchange portal that provides a secure hub for the recyling of good quality rugby boots. The website targets the rugby playing community through keeping the cost of participation to an inexpensive level.  

A marketplace is created by the registered customer through donating unwanted rugby boots. For juniors, foot growth is the main reason for changing their boots, whereas adults may look to change for improved performance or manage issue of wear & tear. Irrespective of age or gender, Re-Boot aims to serve a rugby playing community with low-cost and good quality replacement boots at a fraction of the retail price.     

Once registered, customers will enjoy secure access to their own 'MyReBoot' webpage where personal details can be created, read, updated and deleted. Furthermore, the logged in user can also view their transaction history for both donations and purchases, together with any applicable customer feedback relating to a specfic transaction.    

Furthermore, a reduced carbon footprint can be achieved through avoiding the purchase of brand new rugby boots and shift to product reuse to reduce unecessary landfill waste.


## Demo
A live demo can be found (placeholder)

## Navigate to detail
[UXD Considerations](#uxd-considerations) || [User](#user) | [Business](#business) | [Next Stage Generation](#next-stage-generation) | [Wireframes](#wireframes) | [User Stories](#user-stories) | [CSS Framework](#css-framework) | [Colour Palette](#colour-palette) | [Typography](#typography) | [Icon Graphics](#icon-graphics)  

[Information Architecture](#information-architecture) || [Application Framework](#application-framework) | [Database Selection](#database-selection) | [Data Models](#data-models)

[Technologies Applied](#technologies-applied) || [Databases](#databases) | [Languages](#languages) | [Libraries](#libraries) | [Tools](#tools) | [Hosting](#hosting)

[ReBoot Summary Functions](#reboot-summary-functions) ||

[Features](#features) || [Features Left to Implement](#features-left-to-implement)

[Testing](#testing) || [Introduction](#introduction) | [Systems Based Testing](#systems-based-testing) | [Manual Testing](#manual-testing) | [Code Validation](#code-validation) | [Responsiveness & Rendering](#responsiveness--rendering) 

[Browser Compatibility](#browser-compatibility) ||

[Deployment](#deployment) || [Deployment To Heroku](#deployment-to-heroku) | [Local Deployment](#local-deployment)

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
- All purchased rugby boots delivered to a pre-nominated safe delivery address

#### Business
- Only registered users can donate and purchase Re-Boot products to help deliver assurance on personal data security and trading
- Creation of a MyReBoot account is only for registered users to ensure bonafide credentials
- Provide a simple and intuitive site for the user to click, search, read, create, add, update & delete records. Access levels are determined through whether user has successfully registered 
- Use customer feedback to further improve the offerings of Re-Boot
- Monitor product demand to help generate positive marketing campaigns 
- Next stage generation is to move on from a personal recipe application to enterprise scale where professional kitchens and learning institutions leverage the power of code in the cloud to access quality recipes to create industry best practice and blue print models for recipe innovation.  

#### Next Stage Generation
- Increase product density through expanding scope of sports footwear genres
- Leverage footfall data to attract commercial online advertising, with resultaqnt revenues used to maintain and grow website
- Affiliate with professional sport organisations through embracing product recyle credentials
- Create social media channels to promote 'Re-Boot'

### Wireframes
My wireframe mock-up designs have been created in [Balsamiq](https://balsamiq.com/) to showcase the 'Re-Boot' website responsivenesson mobile, tablet and desktop devices.

•	[Home](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Home_v1.zip)

•	[About](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/About_v1.zip)

•	[BootRoom](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/BootRoom_v1.zip)

•	[Help](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Help_v1.zip)

•	[Search](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Search_v1.zip)

•	[Register & Login](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/RegisterandLogin_v1.zip)

•	[MyReBoot](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/MyReBoot_v1.zip)

•	[Cart](https://github.com/Spagettileg/reboot/blob/master/Plans/wireframes/Cart_v1.zip)


### User Stories
> I need an app that provides quick and intuitive access to understand how to donate & purchase either new or used rugby boots [READ]

> I want to detailed information on make, size, colour and stud type of a replacement rugby boot [READ]

> My personal information must be secure and password protected {CREATE, READ, UPDATE & DELETE]

> My donated rugby boot information must be kept in a secure environment and protected from unauthorised edit & or deletion [UPDATE & DELETE]

> I want to be informed if my donated rugby boots dont get purchased from 6 months from the original date of donation [READ & UPDATE] 

> Obsolete rugby boot donations can be removed from my profile by an authorised user [READ & DELETE]

> To have access to a blog function to understand availability of replacement rugby boots that may not be appearing on Re-Boot website [CREATE, READ, UPDATE & DELETE]

> I would like the opportunity to write a review / provide feedback of my user experience [CREATE, READ & UPDATE]

> I'd like to upload my rugby boot donation by adding make, size, colour, stud configuration and image too [CREATE & UPDATE]

> I would like the flexibility to donate and purchase rugby boots at different times. Replacement boots may not be available at the time of boot donation [CREATE, READ & UPDATE]

> Replacement boots - I'm willing to pay £5.00 for junior boots and £10.00 for adult boots [READ]

> Delivery costs of replacement rugby boots should be borne by the original boot donator [READ]  

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

### Icon Graphics
Font Awesome 5 icon graphics were used in conjunction with Bootstrap 4... (More info required)

TBC
TBC


## Information Architecture
### Application Framework
Django application framework was a prerequisite in the design of this project, according to the project brief.

### Database Selection
Django framework is fast, secure and scalable. Provides a dynamic CRUD (create, read, update and delete) interface, configured with admin models and generated via introspection. requiring SQL database 
 - SQLITE3 database was used for development of this project on my local machine  
 - PostgresSQL was used support the full production of the Re-Boot website. An enterprise-level, object-relational DBMS that uses procedural languages like Perl and Python, in addition to SQL-level code  

### Data Models

TBC...


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

•	Register & Login data entry requirements include username and password. Where appropriate, data entry governance exists in the form of required attributes meaning all requests for data must be completed prior to access the full Virtual Cookbook website   

•	All usernames and passwords will be unique to avoid unauthorised access to third party recipes

•	Logged in users will have access to their own Re-Boot webpage with full rights to create, edit and delete personal information  

### Feature 2 - Navbar brand logo 

•	Normal html convention rules followed by placing the navbar brand logo 'Re-Boot' in the navbar, at the top left corner. The User has unhindered access to this logo and when clicked, will always return the user to the homepage.  


### Features Left to Implement

## Testing

### Introduction


### Systems Based Testing 

### Manual Testing
##### Registration Testing

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


### Responsiveness & Rendering

## Browser Compatability

The following browsers were used in testing the Re-Boot application. Internet Explorer was out of scope for testing due to obsolete capability

platform | version
---------|--------
Chrome   |
Edge     |
Firefox  |
Safari   |
Opera    |

## Deployment

### Deployment to Heroku

#### AWS Cloud 9 IDE

#### Heroku

#### Local Deployment
##### Via GitHub

##### Via the CLI

## Credits
- Shoe sizes reported in both UK and Euro systems sourced from [Shoe sizing charts](https://www.shoesizingcharts.com/)  

### Content

### Media
- Rugby boot images were taken from [prodirectrugby](https://www.prodirectrugby.com/)

- Rugby background and banner images were taken from [pixabay](https://www/pixabay.com) and [Olga Guryanova](https://unsplash.com/photos/ft7vJxwl2RY), both royalty free stock image libraries

- Favicon image was created by myself

### Acknowledgements
