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
| context_processors.py | ![screenshot](documentation/validation/python/python-val-shop-context.png) | Pass: No Errors |
| forms.py | ![screenshot](documentation/validation/python/python-val-shop-forms.png) | Pass: No Errors |
| models.py | ![screenshot](documentation/validation/python/python-val-shop-models.png) | Pass: No Errors |
| urls.py | ![screenshot](documentation/validation/python/python-val-shop-urls.png) | Pass: No Errors |
| views.py | ![screenshot](documentation/validation/python/python-val-shop-views.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/res-chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/res-firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/res-edge.png) | Works as expected |

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
| | Click on Shop link in navbar | Redirection to Shop page | Pass | |
| | Click on Wholesale link in navbar | Redirection to Wholesale page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Shop link in navbar | Redirection to Shop page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Sign Up link in navbar | Redirection to Sign Up page | Pass | |
| | Click on Log Out link in navbar | Log out and Redirection to Home page | Pass | |
| | Enter product in Search Bar | Redirects to Products in the Shop page | Pass | |
| | Click on Cart link in navbar | Redirects to Cart page | Pass | |
| | Click on Social links in Footer | Redirection to corresponding social page | Pass | |
| Home page | | | | |
| | Click on Sho Now button on hero image | Redirection to Shop page | Pass | |
| | Click on Show Me button | Redirection to Shop page | Pass | |
| | Click on product Shop Now button | Redirection to that products detail page | Pass | |
| | Click on Shop Wholesale button | Redirection to Wholesale page | Pass | |
| Shop | | | | |
| | Click on any products View Details button | Redirection to that products details page | Pass | |
| | Select filter preferences and click Apply Filters | Filters products based on search | Pass | |
| | Click on any products Image | Redirection to that products details page | Pass | |
| | Click on any products Add To Cart button | Adds product to cart and toast displays | Pass | |
| Product Details Details Page | | | | |
| | Click on quantity selector buttons | Increases or decreases quantity | Pass | |
| | Click on Add To Cart button | Adds product to cart and toast displays | Pass | |
| | Click on any products Add To Cart button | Adds product to cart and toast displays | Pass | |
| | Click on star rating box | Dropdown bow with star ratings appears | Pass | |
| | Enter text in review box and click Submit Review | Adds review to page and toast confirmation | Pass | |
| | Click Edit button on own review | Redirects to Edit Review page | Pass | |
| | Click Delete button on own review | Redirects to Delete Review page | Pass | |
| | Click Back To Shop button | Redirects to Shop page | Pass | |
| Edit Review Page | | | | |
| | Click on star rating box | Dropdown bow with star ratings appears | Pass | |
| | Enter text in review box and click Update Review | Updates review on page, redirects to product detail page and toast message | Pass | |
| | Click Cancel button | Redirects to Product Details page | Pass | |
| Delete Review Page | | | | |
| | Click Yes, Delete button | Removes review and redirect to Product Detail page | Pass | |
| | Click on Cancel button | Redirect to Product Detail page | Pass | |
| Wholesale Page | | | | |
| | Click on Contact Us button | Redirect to Contact page | Pass | |
| Contact Page | | | | |
| |  Enter name | Redirect to Contact Form | Pass | |
| |  Enter valid email address | Redirect to Contact Form | Pass | |
| | Enter message | Redirect to Contact Form | Pass | |
| | Click on Submit button | Redirect to Contact page and toast message | Pass | |
| | Click on Google Map | Navigates as it should | Pass | |
| Sign In Page | | | | |
| | Enter valid Email Address | Field will only accept registered users | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click on Sign In button | Redirects user to Home page with toast message | Pass |
| | Click on Forgot Password button | Redirects user to Password Reset page | Pass |
| Password Reset Page | | | | |
| | Enter valid Email Address | Field will only accept registered users | Pass | |
| | Click on Back to Login button | Redirects user to Sign In page | Pass |
| | Click on Reset My Password button | Redirects user to Password Reset Submitted page | Pass |
| Password Change Page | | | | |
| | Enter Password | 2 boxes and the passwords need to match | Pass | |
| | Click on Back to Login button | Redirects user to Sign In page | Pass |
| | Click on Change Password button | Redirects user to Password Reset Done page | Pass |
| Password Reset Done Page | | | | |
| | Click on Back To Login button | Redirects user to Sign In page | Pass |
| Register Page | | | | |
| | Enter valid Email Address | Field will only accept email format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Sign Up button | Redirects user to Verify Your Email page with toast message | Pass | |
| Confirm Email Address Page | | | | |
| | Click Confirm button | Redirects to Sign In page with toast message | Pass | |
| Log Out Page | | | | |
| | Click Yes, Log Me Out button | Logs out user, Redirects user to Home page | Pass |
| | Click Cancel button | Keeps user logged in, redirects to Home page | Pass |
| Profile Page | | | | |
| | Click on the Update Profile button | Redirects to Edit Profile page | Pass | |
| | Click on the Delete My Account button | Redirects to Delete Account Confirmation page | Pass | |
| | Click on the View button on an order | Redirects to Order Details page | Pass | |
| Edit Profile Page | | | | |
| | Enter user details | Field will only accept email format | Pass | |
| | Click on the Save Changes button | Redirects to Profile page | Pass | |
| | Click on the Cancel button | Redirects to Profile page | Pass | |
| Delete Account Confirmation Page | | | | |
| | Click on the Delete My Account button | Deletes account and redirects to Home page | Pass | |
| | Click on the Cancel button | Redirects to Profile page without deleting account | Pass | |
| Order Details Page | | | | |
| | Click on the Back To Profile button | Redirects to Profile page | Pass | |
| Cart Page | | | | |
| | (With product in added to cart) change number in quantity box and click Update button | Updates quantity | Pass | |
| | (With product in added to cart) click Remove button | Removes product from cart | Pass | |
| | Click on Proceed To Checkout button | Redirects to Checkout page | Pass | |
| Checkout Page | | | | |
| | Enter user details | Field will only accept email format | Pass | |
| | Click on Product Image | Redirects to Products details page | Pass | |
| | Click on the Adjust Cart button | Redirects to Cart page | Pass | |
| | Click on the Complete Order button | Redirects to Checkout Success page with toast message | Pass | |
| Checkout Success Page | | | | |
| | Click Continue Shopping button | Redirects to Shop page | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Give option to Login or Sign Up | Pass | |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user, I want to browse products by category so that I can easily find items of interest. | ![screenshot](documentation/userstories/stories-browse.png) |
| As a user,  I want to search for products using keywords so that I can quickly find specific items. | ![screenshot](documentation/userstories/stories-keywordsearch.png) |
| As a user, I want to view detailed product information so that I can make informed purchase decisions. | ![screenshot](documentation/userstories/stories-details.png) |
| As a user, I want to add products to my shopping cart so that I can review them before purchasing. | ![screenshot](documentation/userstories/stories-cart.png) |
| As a user, I want to register an account so that I can save my details for future purchases. | ![screenshot](documentation/userstories/stories-register.png) |
| As a user, I want to log in and log out securely so that my account remains private. | ![screenshot](documentation/userstories/stories-login.png) |
| As a user, I want to update my profile information so that I can keep my account details current. | ![screenshot](documentation/userstories/stories-editprofile.png) |
| As a user, I want to leave reviews on products so that I can share my feedback with others. | ![screenshot](documentation/userstories/stories-review.png) |
| As a user, I want a secure and streamlined checkout process so that I can complete my purchase with confidence. | ![screenshot](documentation/userstories/stories-checkout.png) |
| As a user, I want to receive an order confirmation email so that I have a record of my purchase. | ![screenshot](documentation/userstories/stories-orderemail.png) |
| As a user, I want to contact customer support directly through the website so that I can resolve any issues promptly. | ![screenshot](documentation/userstories/stories-contact.png) |
| As a user, I want to view my order history so that I can review past purchases. | ![screenshot](documentation/userstories/stories-orderhistory.png) |
| As an admin, I want to log in to the admin dashboard so that I can manage the site securely. | ![screenshot](documentation/userstories/stories-adminlogin.png) |
| As an admin, I want to perform CRUD operations on products so that I can manage the catalog effectively. | ![screenshot](documentation/userstories/stories-admincrud.png) |
| As an admin, I want to manage user accounts so that I can control access and maintain security. | ![screenshot](documentation/userstories/stories-adminuser.png) |
| As an admin, I want to manage orders so that I can oversee the entire order lifecycle. | ![screenshot](documentation/userstories/stories-adminorders.png) |
| As an admin, I want to manage inventory so that I can keep product stock up to date. | ![screenshot](documentation/userstories/stories-admininventories.png) |
| As an admin, I want to respond to customer inquiries so that issues are resolved quickly. | ![screenshot](documentation/userstories/stories-admincontact.png) |


## Bugs

- Messages not being sent from contact form to the admin panel.

    - Updated the views.py file to contain: from .models import ContactMessage. As it was missing.

- Navbar toggle menu button not working.

    - Bootstrap 4 uses data-toggle="collapse" instead of data-bs-toggle="collapse". Changed and worked.

- Cart quantity was adding quantities together rather than updating them as a whole number.

    - To fix this I had to replace the form action in cart.html to update_cart rather than add_to_cart.

- Cart total briefly displays too many decimal places when the cart is updating.

    - To fix this I had to update the return in the context_processors.py cart_total to inclue '2', this makes sure when loading, the total always displays to 2 decimal places.

- Product orders not showing on Django admin page.

    - Error was showing no sku was set on the product model, added this line:  sku = models.CharField(max_length=32, blank=True, null=True) and made migrated the changes to fix the problem.

- Footer appearing in the toast.

    ![screenshot](documentation/bugs/toast-footer.png)

    - To fix this I had to relocate the toast code in base.html beneath the footer as the footer was inheriting code from the toast.

- Cart total (under the cart icon) was showing too many decimal places, even though all of the views were correct.

    ![screenshot](documentation/bugs/cart-total-error.png)

    - To fix this, I had to import: from django.http import JsonResponse as it was not there.

- Footer not at the bottom of the page on pages that only have a little bit of content.

    ![screenshot](documentation/bugs/footer-not-fixed.png)

    - To fix this I had to add a class to the body tag in base.html, this wrapped everything is a flexbox container, which I then styled in style.css and ensured a height of 100%.

- Navbar breaking in the wrong place due to bootstrap styling.

    ![screenshot](documentation/bugs/navbartoggleissue.png)

    - Add custom breakpoint at 896px.
 

## Unfixed Bugs

There are no remaining bugs that I am aware of.