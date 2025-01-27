# Operating system

Create Ubuntu virtual machine as my host is a Windows 10 machine.  
Install Python and Pipenv on the linux vm for Python project configuration management.  
Install Firefox, Chrome and MSEdge.  

NOTE: Had significant problems with Firefox not running from pytest.
I thought it was me doing something wrong with the Pytest configuration, but after a lot of wasted time it turns out
that it's an Ubuntu 24.04 OS problem with the pytest/selenium webdriver not being able to invoke the "geckodriver" so,
for the moment, I have ignored Firefox and am using Chrome and Edge browsers.
I might be able to get Firefox working when I containerise all of this.

## Python Environment requires:

Python 3.12
Pipenv
After a little faffing around it seems you need to install pipenv in a container using the --system param:
pipenv install --system otherwise you have to create a user and setup the virtualenv in that which is counterproductive
since a container is (usually) a one user, one time thing anyway.


# Sweetshop Tests

### Page Links

Home Page:
`https://sweetshop.netlify.app`

Sweets Page:
`https://sweetshop.netlify.app/sweets`

Login Page:
`https://sweetshop.netlify.app/login`

Account Page:
`https://sweetshop.netlify.app/00efc23d-b605-4f31-b97b-6bb276de447e.html`

Basket Page:
`https://sweetshop.netlify.app/basket`

About Page:
`https://sweetshop.netlify.app/about`

### User registration and login

(use the greyed out, pre-populated credentials)

* Positive - assert leads to "Your Account" page

  * Access Login Page                             DONE
  * login with credentials - data::
    - "abcd@efg.hij" & "blah"
    - "xy@abc" & "password"
* Negative - assert stays on "Login" page

  * login with credentials - data::
    - "" & ""
    - "username" & ""
    - "" & "password"
    - "@efg.hij" & ""
    - "abcd@" & "password"
    - unicode??

- Product browsing and search functionality
  !!I can't see any search function
  ::Positive - assert user sees sweets listed on home page

* "Bon Bons"
* "Sherbert Straws"
  ::Positive - assert user can navigate to sweets list page from home page
* "Sweets" link
* "Browse Sweets" link
  ::Positive - assert user sees sweets listed on sweets list page
* "Sweets" link
* "Browse Sweets" link
  ::Negative - assert ???

- Shopping basket operations
  !!There are many possible actions/operations with regards to the basket feature - here are a few basic ones
  ::Positive - various assertions

* clicking add to basket for Bon Bons :asserion: increases basket by 1
* clicking add to basket for Fruit Salads & Drumsticks :asserion: adds 2 to the basket
* clicking add to basket for Fruit Salads & Drumsticks :asserion: and then going to basket shows Fruit Salads & Drumsticks
  ::Negative - assert ???

- Checkout process
  ::Positive - various assertions

::Negative - assert ???

- Order history veriﬁcation
  ::Positive - various assertions

::Negative - assert ???


# AirportGap Tests

