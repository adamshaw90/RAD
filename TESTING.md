# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| 404 | ![screenshot](documentation/validation/html/html-val-404.png) | Pass: No Errors |
| Home/Base | ![screenshot](documentation/validation/html/html-val-base.png) | Pass: No Errors, 1 Warning : HTML is compliant, external JS script warning. Inherited throughout site. |
| Shop | ![screenshot](documentation/validation/html/html-val-shop.png) | Pass: No Errors |
| Wholesale | ![screenshot](documentation/validation/html/html-val-wholesale.png) | Pass: No Errors |
| About | ![screenshot](documentation/validation/html/html-val-about.png) | Pass: No Errors |
| Contact | ![screenshot](documentation/validation/html/html-val-contact.png) | Pass: No Errors |
| Profile | ![screenshot](documentation/validation/html/html-val-profile.png) | Pass: No Errors |
| Register | ![screenshot](documentation/validation/html/html-val-register.png) | Pass: No Errors |
| Login | ![screenshot](documentation/validation/html/html-val-login.png) | Pass: No Errors |
| Product Details | ![screenshot](documentation/validation/html/html-val-productdetail.png) | Pass: No Errors |
| Edit Review | ![screenshot](documentation/validation/html/html-val-reviewedit.png) | Pass: No Errors |
| Delete Review | ![screenshot](documentation/validation/html/html-val-reviewdelete.png) | Pass: No Errors |
| Edit Profile | ![screenshot](documentation/validation/html/html-val-profileedit.png) | Pass: No Errors |
| Delete Profile | ![screenshot](documentation/validation/html/html-val-profiledelete.png) | Pass: No Errors |
| Order Details | ![screenshot](documentation/validation/html/html-val-orderdetails.png) | Pass: No Errors |
| Logout | ![screenshot](documentation/validation/html/html-val-logout.png) | Pass: No Errors |
| Cart | ![screenshot](documentation/validation/html/html-val-cart.png) | Pass: No Errors |
| Checkout | ![screenshot](documentation/validation/html/html-val-checkout.png) | Pass: No Errors |
| Checkout Success | ![screenshot](documentation/validation/html/html-val-checkoutsuccess.png) | Pass: No Errors |
| Email confirm | ![screenshot](documentation/validation/html/html-val-emailconfirm.png) | Pass: No Errors |
| Password Change | ![screenshot](documentation/validation/html/html-val-password1.png) | Pass: No Errors |
| Password Reset Done | ![screenshot](documentation/validation/html/html-val-password2.png) | Pass: No Errors |
| Password Reset From Key Done | ![screenshot](documentation/validation/html/html-val-password3.png) | Pass: No Errors |
| Password Reset From Key | ![screenshot](documentation/validation/html/html-val-password4.png) | Pass: No Errors |
| Password Reset | ![screenshot](documentation/validation/html/) | Pass: No Errors |
| Verification Sent | ![screenshot](documentation/validation/html/html-val-emailconfirmclick.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![screenshot](documentation/validation/css/css-val-style.png) | Pass: No Errors |
| checkout.css | ![screenshot](documentation/validation/css/css-val-checkout.png) | Pass: No Errors |
| order_details.css | ![screenshot](documentation/validation/css/css-val-order.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation//validation/javascript/js-val-stripe.png) | Pass: No Errors |
| cart.js | ![screenshot](documentation//validation/javascript/js-val-cart.png) | Pass: No Errors |
| quantity.js | ![screenshot](documentation//validation/javascript/js-val-quantity.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For rad App
| File | Screenshot | Notes |
| --- | --- | --- |
| settings.py | ![screenshot](documentation/validation/python/python-val-rad-settings.png) | AUTH_PASSWORD_VALIDATORS lines too long (django code) |
| urls.py | ![screenshot](documentation/validation/python/python-val-rad-urls.png) | Pass: No Errors |

#### Validation For Checkout App
| File | Screenshot | Notes |
| --- | --- | --- |
| init.py | ![screenshot](documentation/validation/python/python-val-checkout-init.png) | Pass: No Errors |
| admin.py | ![screenshot](documentation/validation/python/python-val-checkout-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](documentation/validation/python/python-val-checkout-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](documentation/validation/python/python-val-checkout-forms.png) | Pass: No Errors |
| models.py | ![screenshot](documentation/validation/python/python-val-checkout-models.png) | Pass: No Errors |
| signals.py | ![screenshot](documentation/validation/python/python-val-checkout-signals.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/python-val-checkout-urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/python-val-checkout-views.png) | Pass: No Errors |
| webhook_handler.py | ![screenshot](documentation/validation/python/python-val-checkout-whh.png) | Pass: No Errors |
| webhooks.py | ![screenshot](documentation/validation/python/python-val-checkout-wh.png) | Pass: No Errors |

#### Validation For Accounts App
| File | Screenshot | Notes |
| --- | --- | --- |
| forms.py | ![screenshot](documentation/validation/python/python-val-acc-forms.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/python-val-acc-urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/python-val-acc-views.png) | Pass: No Errors |

#### Validation For Core App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](documentation/validation/python/python-val-core-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](documentation/validation/python/python-val-core-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](documentation/validation/python/python-val-core-forms.png) | Pass: No Errors |
| models.py | ![screenshot](documentation/validation/python/python-val-core-models.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/python-val-core-urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/python-val-core-views.png) | Pass: No Errors |

#### Validation For Shop App
| File | Screenshot | Notes |
| --- | --- | --- |
| cart_tags.py | ![screenshot](documentation/validation/python/python-val-shop-carttags.png) | Pass: No Errors |
| shop_tags.py | ![screenshot](documentation/validation/python/python-val-shop-shoptags.png) | Pass: No Errors |
| admin.py | ![screenshot](documentation/validation/python/python-val-shop-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](documentation/validation/python/python-val-shop-apps.png) | Pass: No Errors |
| context_processors.py | ![screenshot](documentation/validation/python/) | Pass: No Errors |
| forms.py | ![screenshot](documentation/validation/python/python-val-shop-forms.png) | Pass: No Errors |
| models.py | ![screenshot](documentation/validation/python/python-val-shop-models.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/python-val-shop-urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/python-val-shop-views.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser_chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser_firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser_edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/desktop.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

### RAD Templates - Mobile Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| 404 | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Home | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Shop | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Wholesale | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| About | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Contact | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Profile | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Register | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Login | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Product Details | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Edit Review | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Delete Review | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Edit Profile | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Delete Profile | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Order Details | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Logout | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Cart | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Checkout | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Checkout Success | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Base | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Account Base | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Email confirm | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Password Change | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Password Reset Done | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Password Reset From Key Done | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Password Reset From Key | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Password Reset | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Verification Sent | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Verified Email Required | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Toast Error | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Toast Info | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Toast Success | mobile | ![screenshot](documentation/lighthouse/mobile) |  |
| Toast Warning | mobile | ![screenshot](documentation/lighthouse/mobile) |  |

### RAD Templates - Desktop Testing
| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| 404 | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Home | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Shop | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Wholesale | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| About | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Contact | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Profile | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Register | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Login | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Product Details | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Edit Review | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Delete Review | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Edit Profile | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Delete Profile | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Order Details | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Logout | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Cart | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Checkout | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Checkout Success | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Base | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Account Base | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Email confirm | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Password Change | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Password Reset Done | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Password Reset From Key Done | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Password Reset From Key | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Password Reset | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Verification Sent | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Verified Email Required | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Toast Error | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Toast Info | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Toast Success | desktop | ![screenshot](documentation/lighthouse/desktop) |  |
| Toast Warning | desktop | ![screenshot](documentation/lighthouse/desktop) |  |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Itineraries link in navbar | Redirection to Itineraries page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Sign Up link in navbar | Redirection to Sign Up page | Pass | |
| | Click on Log Out link in navbar | Log out and Redirection to Home page | Pass | |
| | Click on Social links in Footer | Redirection to corresponding social page | Pass | |
| Home page | | | | |
| | Click on Explore Itineraries button on hero image | Redirection to Itineraries page | Pass | |
| | Click on Featured Itineraries View Details button | Redirection to that itinerary's details page | Pass | |
| Itineraries page | | | | |
| | Click on any itinerary's View Details button | Redirection to that itinerary's details page | Pass | |
| Itinerary Details Page | | | | |
| | Click on Book Now button | Redirect to booking confirmation page | Pass | |
| | Click on back button | Redirect to reservation list page | Pass | |
| Booking Confirmation Page | | | | |
| | Click on Confirm Booking button | Redirect to Profile confirmation page | Pass | |
| | Click on Cancel button | Redirect to itinerary page | Pass | |
| Contact Page | | | | |
| |  Enter name | Redirect to Contact Form | Pass | |
| |  Enter valid email address | Redirect to Contact Form | Pass | |
| | Enter message | Redirect to Contact Form | Pass | |
| | Click on Submit button | Redirect to Contact page | Pass | |
| | Click on Google Map | Navigates as it should | Pass | |
| Login Page | | | | |
| | Enter valid Username | Field will only accept registered users | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click on Log In button | Redirects user to Home Page | Pass |
| | Click on Sign Up button | Redirects user to Sign Up Page | Pass |
| Sign Up Page | | | | |
| | Enter valid Username | Field will only accept username format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Register button | Redirects user to home page | Pass | |
| Log Out Page | | | | |
| | Click Logout button | Logs out user, Redirects user to Home page | Pass |
| | Click Cancel button | Keeps user logged in, redirects to Home page | Pass |
| Profile Page | | | | |
| | Click on the Edit Profile button | Redirects to Edit Profile page | Pass | |
| | Click on the Delete Account button | Redirects to Delete Account Confirmation page | Pass | |
| | Click on the Cancel booking button | Redirects to Delete Booking Confirmation page | Pass | |
| Edit Profile Page | | | | |
| | Enter user details | Field will only accept email format | Pass | |
| | Click on the Save Changes button | Redirects to Profile page | Pass | |
| | Click on the Cancel button | Redirects to Profile page | Pass | |
| Delete Account Confirmation Page | | | | |
| | Click on the Delete My Account button | Deletes account and redirects to Home page | Pass | |
| | Click on the Cancel button | Redirects to Profile page without deleting account | Pass | |
| Delete Booking Confirmation Page | | | | |
| | Click on the Yes, Cancel button | Deletes booking and redirects to Profile page | Pass | |
| | Click on the No, Go Back button | Keeps booking and redirects to Profile page | Pass | |
| | Click on the Cancel booking button | Redirects to Delete Booking Confirmation page | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Give option to Login or Sign Up | Pass | |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I want to log into my account so that I can access my saved trips and profile settings. | ![screenshot](documentation/features/site-pages/profilewithbooking.png) |
|As a user I want to recover my account if I forget my password, so that I can regain access without creating a new account. | ![screenshot](documentation/features/site-pages/contactpage.png) |
| As a user I want to sign up for an account so that I can access the website's features. | ![screenshot](documentation/features/site-pages/signup.png) |
| As a user I want to log out of my account so that my session is securely ended. | ![screenshot](documentation/features/site-pages/logout.png) |
| As a user I want to book a trip from the itinerary page so that I can reserve my spot. | ![screenshot](documentation/features/site-pages/itin2.png) |
| As a user I want to update my account information so that I can keep my details accurate. | ![screenshot](documentation/features/site-pages/editprofile.png) |
| As an admin I want to create, update, or delete itineraries, so that I can keep the trip offerings up-to-date. | ![screenshot](documentation/features/site-pages/itinadmin.png) |
| As an admin I want to view and manage user bookings so that I can handle any issues or changes efficiently. | ![screenshot](documentation/features/site-pages/bookingadmin.png) |


## Bugs

- Navbar items wouldn't align on right.

    - To fix this, I had to remove css for header display:flex for them to align to the right.

- Raw html showing on homepage cards.

    ![screenshot](documentation/bugs/rawhtmlbug.png)

    - To fix this, I had to add 'safe' to base home.html

- Card buttons not staying at the bottom.

    ![screenshot](documentation/bugs/buttonsbug.png)

    - To fix this, I wrapped the card contents in a separate div and added css to the button : margin-top: auto;

- Logo not showing.

    ![screenshot](documentation/bugs/logobug.png)

    - To fix this, I had to resize the logo image as the file size was too large.

- Footer not staying fixed to the bottom of the page on soame pages.

    ![screenshot](documentation/bugs/footerbug.png)

    - To fix this I had to set the .homepage height to 100vh.

- Extra zeros being displayed on prices.

    - To fix this, I had to add a float format so new code is: <p><strong>Price:</strong> £{{ itinerary.price|floatformat:"0" }}pp</p> anywhere there was a price.

- Too many itineraries showing in the features section.

    - To fix this, I had to add 'slice' to {% for itinerary in itineraries|slice:":6" %} in the home.html file so that it will now only display 6.

## Unfixed Bugs

There are no remaining bugs that I am aware of.