# EternalCityCrawls
Half/Full Day Tour of Rome developed on Django

## Table of contents
<!--ts-->

# UX

## User goals

The target audience of **Eternal Cities Crawls** is:
- Local People interested in unusual visit of their own city.
- First Time Visitors with little time available, interested to see the most important.
- Food Lovers interested to combine visits with local food.

User goals:
- Browse the tour Catalogues and order them by type and duration.
- Be able to see preview image of destination, price and details of the tour.
- Book a specific tour along with the number of participants, adding it to the cart page.
- Check on the personal profile page the booking they have in place
- Add Multiple tour to the Cart Page
- Log on the Personal Profile Page
- Checkout using card payment.
- Find information about the tour operators such as address phone number and its mission.
- Read Previous Customer's feedbacks.
- Receive information about the status of his/her payment.

## Design

### Color Scheme
Following color Palette has been adopted; the main background color used is Panache(`#F1FAEE`) or Conch(`#A8ADAC`) as an alternative; those two colours are dominating the application. Other Elements, such Button and Navbar are using Nordic (`#1D3537`) or a gradient of it with Jelly Bean(`#457B9D`). Amaranth(`#E63946`) has been used as an element of contrast, in the footer or for some button.

![Color Palette](static/img/ECC_palette.png)

## Wireframes

Wireframe mockups, created using [Balsamiq](https://balsamiq.com/), are available in diffent format:

 1. Laptop
    1. [Landing](wireframes/landing/LandingLaptop.pdf)
    1. [Seach](wireframes/search/SearchLaptop.pdf)
    1. [Tour](wireframes/tour/TourLaptop.pdf)
    1. [Checkout Main](wireframes/checkout/CheckoutMainLaptop.pdf)
    1. [Checkout Details](wireframes/checkout/CheckoutDetailsLaptop.pdf)
 1. Tablet
     1. [Landing](wireframes/landing/LandingTablet.pdf)
     1. [Search](wireframes/search/SearchTablet.pdf)
     1. [Tour](wireframes/tour/TourTablet.pdf)
     1. [Checkout Main](wireframes/checkout/CheckoutMainTablet.pdf)
     1. [Checkout Details](wireframes/checkout/CheckoutDetailsTablet.pdf)
 1. Mobile
     1. [Landing](wireframes/landing/LandingMobile.pdf)
     1. [Search](wireframes/search/SearchMobile.pdf)
     1. [Tour](wireframes/tour/TourMobile.pdf)
     1. [Checkout Main](wireframes/checkout/CheckoutMainMobile.pdf)
     1. [Checkout Details](wireframes/checkout/CheckoutDetailsMobile.pdf)


Modals not dependent on the device:

   1. [Log in](static/img/wireframes/login/login.pdf)
   1. [Register](static/img/wireframes/login/registration.pdf)

## Deployment

### Deploying to Heroku:

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```

* 2: <strong>Create</strong> a procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push these newly created files to your repository.
* 4: Create a new app for this project on the Heroku Dashboard.
* 5: Select your deployment method by clicking on the deployment method button and select GitHub.
* 6: On the dashboard, set the following config variables:

**Key**|**Value**
:-----:|:-----:


* 7: <strong>Click</strong> the deploy button on the heroku Dashboard.
* 8: Wait for the build to finish and click the view project link once it has!





