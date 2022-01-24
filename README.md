# Milestone Project 4 - Très Cars

## Project

The purpose of this site is to allow a user to browse and purchase a vehicle and browse and purchase accessories.

# Showcase

A deployed link to the site can be found on Heroku [here](https://tres-cars.herokuapp.com/)

![Preivew](static/images/responsive.png)
# UX

## User Stories

|Sotry ID|As A/An|I want to be able to|So That I can|
|-----|-----|-----|----|
| Viewing and Navigation|
|1| Shopper | View all vehicles for sale | Find an appropriate vehicle |
|2| Shopper | View Details of a specific vehicle | View all relevant information related to that vehicle|
|3| Shopper | Calculate true cost of a vehicle | Have a full understanding of the cost |
|4| Shopper | View accessories for a vehicle | Choose what I would like to add to my vehicle |
| Filtering / Searching |
|5| Shopper | Search by a vehicle Make / Model | Find the available stock of a certain vehicle |
|6| Shopper | Filter the vehicles by attributes | Identify vehicles matching my wants |
|7| Shopper | Sort the available vehicles by an attribute | See the vehicles in an order of e.g price |
|8| Shopper | See the number of available vehicles | See how many options are available |
| Checkout / Purchasing |
|9| Shopper | Easily see the products to be purchased | Ensure correct product / vehicle is being purchased |
|10| Shopper | Adjust quantity of products to be purchased | See the total cost and add more of an item if needed |
|11| Shopper | Enter Payment Info | Checkout with problem |
|12| Shopper | Secure Checkout | Feel safe that details are secure |
| Registration |
|13| Site User | Easily Register for an account	| Have a personal account with recommendation for parts / servicing |
|14| Site User | Login / Logout	| Access personal account information |
|15| Site User | Recover password | Recover access to account |
|16| Site User | Email Confirmation	| Verify that account creation was successful |
|17| Site User | Personalised User Page	| View Order history, my vehicle, set service schedule |
| Administration |
|18| Site Admin | Add vehicles to the site | Update the site with new vehicle stock |
|19| Site Admin | Add products / accessories to the site | Update site with new accessories |
|20| Site Admin | Update Vehicle / Product Details on the site | Update the details of a specific vehicle |


## Strategy

### User Needs

A user needs to be able to easily see what the website offers. This will be done via the landing page of the site.
Each aspect of the page will be displayed easily for a used. all information will be easily accesible.

A user needs to be able to purchase a vehilce or accessories with ease and in as fewer steps as possible.

### Technical Capabilities

It is possible to create this site efficiently using the bootstrap and Django frameworks as well as the HTML/CSS/Javascript/Python and heroku for deployment and postgres of a database. The DVLA API will also be used for getting extra information on vehicles added to the database.
### Business Vision

Offer a wide variety of vehicles, from older vehicles to brand new ones and pices from affordably to luxury. THe site will also offer accessories for specific of all vehicles
## Scope

The site will quickly show what it's purpose is for a user. From the home page users will be ale to enact a somple vehicle search with a mode detail search to follow.

Informaiton about the site can be found lower down on the home page, along with contact informaitn and a location. The site will be easy to navigate and 
The site will include an about section detailing what the site does and what a user can gain from it. It will be easy to enact a search and read the results. All information will be clearly laid out and easy to understand at a glance

## Structure

- The site will be detailed but simply laid out, cover 20 pages in total with pages generated when clicked on.
- navigation will give quick access to the main features of the site
- Site pages 
    - Home, Returns, Login, Logout, Vehicle Search, Vehicle Details, Accessory Select, accessory search, accesssory detail
    - Bag, Vehicle Checkout, Checkout, Checkout success, Profile, Management Home, Add Vehicle, Update Vehicle
    - Add Accessory, Update Accessory, contact Page
- A user will be able to quickly search for a vehicel fomr the home page, or run a more detail search from the vehicle search page. They will be able to select a type of accesory via the accessoeis link in the nav bar.
- Users can create a profil where purchases and account details can be stored
- An admin panel will be accesiable by admin users to allow for Adding/Updating Vehicles & accessories
## Skeleton

### Wireframes

- [Mobile >576px](static/wireframes/sm.png)
- [Tablet ≥768px](static/wireframes/md.png)
- [Desktop ≥1400px](static/wireframes/lg.png)

### Databse Schema

- [Schema](static/wireframes/database_schema.png)


## Surface

The site will be set over multiple pages. Users will be able to search for a purchase accessories / vehicles
## Visual Design
### Home

- The page will contiane a quick simple search for a vehicle
- An introduction and information panes wil lbe displayed futher down the page.

### Returns Page

- A simple page displaying the terms and conditions of sales and returns

### Contact Page

- A form to submit to the company.
- If the link to the page comes from a vehicle detail / accessory detail page, the informaiton onf the itme is included.
### Vehicle Search Page

- Linked to via the quick search and more options on the home page or via the New Search button in the header
- Without a search, contains all the vehicles on the site, with a search, displayed the matching vehicles.
- Able to filter vehicels by pre-defined search parameters.
- Sort the returned vehicles

### Vehicle Detail Page

- shows all the details and images of the selected vehicle
- able to see live data from DVLA api on the MOT,TAX and Co2 status
- Able to go to contact page taking the vehicle info
- Able to click to reserve the vehicle
- if an admin, vehicles can be updated/deleted
### Vehicle Reserve Page

- Can only take 1 vehicle at a time
- Enter user data, or prefilled if user logged in with saved data
- Enter payment details and reserve vehicle
- Confirmation mail sent to customer
- Info email sent to company

### Accessories Page

- Shows the categories of accessories available
- Clicking one filters the accessories by the category
- Search box available to search by term

### Accessories Search Page

- displays all accessories available for the category
- Accessoeis can be sorted
- Search box available to search by term
- if an admin, accessories can be updated / deleted
### Accessory Detail Page

- Displays the image and data available for the accessory
- Add to bag link for added teh accessory to bag
- "+ / -" buttons for changing quantity required
- if an admin, accessories can be updated / deleted
- Able to go to contact page taking the accessory info
### Bag Page

- Displays all the accessories currently in the bag
- Link to more accessoeis
- Link to the secure checkout page
### Acessories Checkout Page

- Enter user data, or prefilled if user logged in with saved data
- Enter payment details and complete order
- Confirmation mail sent to customer
- Info email sent to company


## Admin Pages
### Management Home

- Displayed the links to Add A vehicle or accessory

### Add vehicle

- Allows a vehicle to be added
- Allows text information
- Allows multi image upload with requirment to select a main image

### Update a vehicle

- Accessed via vehicles search page or vehicle page
- Allows text information to be edited
- Allows images to be removed
- Allows a new main image to be selected
- Allows more images to be added

### Add an acessory
- Allows an accessory to be added
- Allows text information
- Allows single image upload
## Features

### Existing Features

### Features to be implemented

- Service Reminders
- MOT Reminders
## Technoogies used

- HTML
- CSS
- Javascript (Jquery & Vanilla)
- Bootstrap (Styling Framework)
- DVLA API (getting Vehicle Info)
- Django (Framework)
- Heroku (Deployment)
- Postgres (Database)
- AWS S3 Bucket (Storage)

# Testing
## Planning

## Running Tests

- Testing the HTML code was tested by generating a page and copying the HTML/url into the [W3C](https://validator.w3.org/) HTML Validator
- Testing the CSS was tested with the [W3C](https://jigsaw.w3.org/css-validator/validator) validator
- Tesing Javascript was tested with [Beautify Tools](https://beautifytools.com/javascript-validator.php)
- Testing Python was tested with [Python Tester](https://extendsclass.com/python-tester.html)

### HTML5 
#### User

- index.html
    - Removed unused attributes on select and a elements
    - Passed
- returns.html
    - Passed
- vehicles.html
    - removed unused attributes from select elements
    - Passed
- vehicle_detial.html
    - Passed
- reserve_vehicle_checkout.html
    - Own Code Passes
    - Stripe auto populated elements have issues
- checkout_success.html
    - Passed
- accessories.html
    - Removed unused attributes
    - Passed
- accessories_search.html
    - Removed unused attributes
    - added action to search form to conform
    - Passed
- accessories_detail.html
    - Removed usused heading
    - changed the way js adds disabled attribute
    - Passed
- bag.html
    - too many table row to headers. Corrected
    - Passed
- checkout.html
    - Own Code Passes
    - Stripe auto populated elements have issues
- profile.html
    - Passed

#### Admin

- home.html
    - correct a patagraph in a span
    - Passed
- add_vehicle.html
    - removed placeholder from select elements
    - Passed
- add_accessories.html
    -

### CSS3 

- base.css
    - Error with a colour spelt wrong. Corrected
- vehicles.css
    - Passed, No Errors
- profile.css
    - Passed, No Errors
- management.css
    - Passed, No Errors
- checkout.css
    - Passed, No Errors
- accessories.css
    - Passed, No Errors

### Javascript

- vehicles.js
    - Missing semicolons. Corrected
- vehicle_detail.js
    - Missing semicolons. Corrected
- home-script.js
    - variable not defined. Added let
- profile.js
    - Missing semicolons. Corrected
- add_accessory.js
    - Missing semicolons. Corrected
- add_vehicle.js
    - Missing semicolons & unused code. corrected
- update_vehicle.js
    - Missing semicolons. Corrected
- stripe.js
    - No errors
- bag.js
    - unused code removed
- accessories.js
    - Missing semicolons. Corrected
- accessory_detail.js
    - Missing semicolons. Corrected

### Python
## tres_cars (project)

- settings.py
    - Pass
- urls.py
    - Pass
## Vehicles

- admin.py
    - Pass
- models.py
    - Pass
- views.py
    - Pass
- urls.py
    - Pass

## profiles

- forms.py
    - Pass
- models.py
    - Pass
- views.py
    - Pass
- urls.py
    - Pass

## management

- forms.py
    - Pass
- models.py
    - Pass
- urls.py
    - Pass
- views.py
    - Pass
- widgets.py
    - Pass

## home

- urls.py
    - Pass
- views.py
    - Pass

## checkout

- admin.py
    - Pass
- forms.py
    - Pass
- models.py
    - Pass
- signals.py
    - Pass
- urls.py
    - Pass
- views.py
    - Pass
- webhook_handler.py
    - Pass
- webhooks.py
    - Pass

## bag

- contexts.py
    - Pass
- urls.py
    - Pass
- views.py
    - Pass

## accessories

- admin.py
    - Pass
- models.py
    - Pass
- urls.py
    - Pass
- views.py
    - Pass

### Lighthouse Results
#### Admin Pages


## Testing Results


### Bugs that occured

## Bugs/Changes During Development

## Deployment

# Credits

## This project is for educational purposes only

### Created by Codie Stephens-Evans