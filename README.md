# R.A.D - Really Addictive Decaf

![screenshot](documentation/mockup.png)

R.A.D is a fully functioning web application for an ecommerce decaf coffee website. The site provides users with information about coffee blends from around the world, an option to buy the coffee, allows users to easily create personal accounts and profiles to view current and previous orders, a contact section and a reviews section. The site also enables administrators to post new products to the site, as well as view and respond to customer enquiries.

## UX

The design philosophy was to create a stand-out design, with colours and design elements themed around extra-terrestrials/space.The coffee market is saturated so having a theme and colour scheme that is bold - and a niche focussing on decaf, would be the USP.

### Colour Scheme


The color scheme uses a bold pink, dark blue, white and turquoise to complement the custom packaging.


![screenshot](documentation/colour-palette.png)


## User Stories

All user stories can be found in a linked GitHub project [here](https://github.com/users/adamshaw90/projects/8)


## Features

## Existing Features

### Site Pages

- **Homepage**

    - The main homepage for the site. Hero image is large and striking. Welcome message to let users know what the site is. Call to action button to invite users to enter and explore the site. It also has information about the site with a section informing users of the variety of coffee available, with a link to the shop, a section of 'fan favourites' with links to individual products and a wholesale section with a button link to the wholesale page.

![screenshot](documentation/features/site-pages/Homepage1.png)
![screenshot](documentation/features/site-pages/Homepage2.png)
![screenshot](documentation/features/site-pages/Homepage3.png)
![screenshot](documentation/features/site-pages/Homepage4.png)


- **Shop Page**
    - Shop page. A page for users to browse the products on the site. Features include filters to narrow down the users preferences, and clickable products to go to the products detail page, also an option on each product to add straight to the cart without viewing the details page. Product deatils have a review and rating section that can be added to by signed-in users, that also have an edit and delete function.

![screenshot](documentation/features/site-pages/Shoppage.png)
![screenshot](documentation/features/site-pages/Detailspage1.png)
![screenshot](documentation/features/site-pages/Detailspage2.png)
![screenshot](documentation/features/site-pages/Detailspage3.png)
![screenshot](documentation/features/site-pages/Editreviewpage.png)
![screenshot](documentation/features/site-pages/Deletereviewpage.png)


- **Cart and Checkout Pages**
    - Cart page. Displays any products that the user has currenlty added to their shopping cart. Has the option to increase or decrease the quantity of each product in the cart, aswell as an option to remove the product completely.
    - Checkout Page. Displays the order summary so the user can double check what they are purchasing along with a payment details form for the name, address, phone number, email address and secure Stripe card payment form.

![screenshot](documentation/features/site-pages/Cartpage.png)
![screenshot](documentation/features/site-pages/checkoutpage1.png)
![screenshot](documentation/features/site-pages/checkoutpage2.png)


- **Wholesale Page**
    - Wholesale page. Gives users information on bulk buying and special pricing for business owners. Has a link to the contact page.

![screenshot](documentation/features/site-pages/Wholesalepage1.png)
![screenshot](documentation/features/site-pages/Wholesalepage2.png)


- **About Page**

    - About page. Gives users information on the business and their ethics. Dislays some images of the coffee production process.

![screenshot](documentation/features/site-pages/Aboutpage.png)


- **Contact Page**

    - Contact Page. Users can see contact information for R.A.D, including 
    a contact email address and location information. An embedded Google Maps widget allows users to see the business's exact location. There is also a form that can be filled out by users.

![screenshot](documentation/features/site-pages/Contactpage1.png)
![screenshot](documentation/features/site-pages/Contactpage2.png)


- **Register Page**

    - Register Page. Displays a form that new users of the site can fill in and make an account. The form is short, simple, and clean to encourage users to use it.

![screenshot](documentation/features/site-pages/Registerpage.png)


- **Sign-in Page**

    - Sign-in Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in to their account. A Forgot Password link takes users to another page where they can recover their password.

![screenshot](documentation/features/site-pages/Signinpage.png)
![screenshot](documentation/features/site-pages/Changepasswordpage.png)
![screenshot](documentation/features/site-pages/Passwordlinksentpage.png)
![screenshot](documentation/features/site-pages/Passwordresetpage.png)
![screenshot](documentation/features/site-pages/Passwordchangedpage.png)


- **Profile Page**

    - Profile page. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an edit form that users can use to update their profile information. It also displays any current and previous orders they have with a link to view the details. There is an option to delete the user profile also.

![screenshot](documentation/features/site-pages/Profilepage.png)
![screenshot](documentation/features/site-pages/Orderdetailpage.png)
![screenshot](documentation/features/site-pages/Editprofilepage.png)
![screenshot](documentation/features/site-pages/Deleteprofilepage.png)


- **Logout Page**

    - Logout Page. A simple page confirming that the user has logged out of their account. Displays a log in again button in case the user wishes to log back in.

![screenshot](documentation/features/site-pages/Logoutpage.png)


- **Custom Error Page**

    - Custom error handler page. This displays a simple error page that lets the user know that there has been an error loading the url with a button to take them back to the home-page of the site.

![screenshot](documentation/features/site-pages/404page.png)


### User Features

- **User Registration**

    - Users can register for an account using a front-end form. This creates a user object in the database and automatically secures the user's sensitive information.

![screenshot](documentation/features/user/Registerpage.png)

- **User Login**

    - Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.

![screenshot](documentation/features/user/Signinpage.png)

- **User Logout**

    - Users who are logged in can easily log out in order to stop access to their account-based information and functionality.

![screenshot](documentation/features/user/Logoutpage.png)


- **Login Dependant Navbar Links**

    - Users who are logged in see new links in the navbar. 'Sign Up' and 'Login' links are replaced with 'Profile' and 'Logout' links. This provides the user with visual feedback upon logging in, as well as removing links that they will not need.

![screenshot](documentation/features/user/navlinkbefore.png)
![screenshot](documentation/features/user/navlinkafter.png)


- **User Profile Creation**

    - User profiles are automatically created upon user registration. This assigns each user a profile which they can use to see/update their user information.

![screenshot](documentation/features/user/Profilepage.png)

- **User Profile Update**

    - Users can update their profile information using a front-end form located on their user profile page. This allows users to update profile information or correct possible mistakes made at registration.

![screenshot](documentation/features/user/Editprofilepage.png)

- **Adding Items to Cart**

    - Users can use the button on a product card in the shop page, or on the product details page to add the product to the cart - they will get a 'toast' pop up confirming the action, as well as showing a preview of the shopping cart.

![screenshot](documentation/features/user/Shoppage.png)
![screenshot](documentation/features/user/Toastcart.png)

    This will then show in the cart page when the user navigates there.

![screenshot](documentation/features/user/Cartpage.png)


- **User Order History**

    - Users can view their pending and previous orders from the profile page, with a button to view a particular orders details.

![screenshot](documentation/features/user/Profilepage.png)
![screenshot](documentation/features/user/Orderdetailpage.png)


### Future Features

- Additional option selectors on the product page.
    - Size/weight selector.
    - Type (bean or ground) selector.
- Advanced itinerary actions for admins.
    - Front end product creation.
    - Front end edit and delete functions.
    - Front end customer message view and response.
- Additional models for the site.
    - Subscription model.
    - Barista class booking model.

## Wireframes

- Balsamiq was used to create the wireframes.

Home page:

![home-wire](documentation/wireframes/wirehome1.png)
![home-wire](documentation/wireframes/wirehome2.png)
![home-wire](documentation/wireframes/wirehome3.png)
![home-wire](documentation/wireframes/wirehome4.png)

Shop page:

![home-wire](documentation/wireframes/wireshop.png)

Wholesale page:

![home-wire](documentation/wireframes/wirewholesale.png)
![home-wire](documentation/wireframes/wirewholesale2.png)

About page:

![about-wire](documentation/wireframes/wireabout.png)
![home-wire](documentation/wireframes/wireabout2.png)


Contact page:

![contact-wire](documentation/wireframes/wirecontact.png)

Login page:

![contact-wire](documentation/wireframes/wirelogin.png)


Profile page:

![contact-wire](documentation/wireframes/wireprofile.png)


## Tools & Technologies Used


- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [VSCode](https://code.visualstudio.com/) used as a local IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [CodeInstitute Database](https://dbs.ci-dbs.net/) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed site.
- [Cloudinary](https://cloudinary.com) used for online static file storage. and image converting.
- [Gunicorn](https://gunicorn.org/) used for WSGI server.
- [sycopg2](https://pypi.org/project/psycopg2/) used as a PostgreSQL database adapter.
- [AmIResponsive](https://ui.dev/amiresponsive) used as a mock-up maker.
- [Canva](https://www.canva.com/) used for image creation and AI image design.
- [Frame0](https://frame0.app/) used for wireframes.

## Database Design

While planning this project, I drew up some Entity Relationship Diagrams to help me to visualise the database models and their relationships. 

- User
![screenshot](documentation/user-erd.png)

- Product
![screenshot](documentation/product-erd.png)

- Order
![screenshot](documentation/order-erd.png)

- OrderItem
![screenshot](documentation/orderitem-erd.png)

- Cart
![screenshot](documentation/cart-erd.png)

- CartItem
![screenshot](documentation/cartitem-erd.png)

- Review
![screenshot](documentation/review-erd.png)

- ContactForm
![screenshot](documentation/contact-erd.png)


## Agile Development Process

### GitHub Projects & Issues
GitHub projects served as an Agile tool for this project.
It isn't a specialized tool, but it can be used the same way.

Through it, user stories, issues, and tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/userstories.png)


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://rad-47d779d14a28.herokuapp.com/).


### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python manage.py makemigrations`
- Migrate the data to the database: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Load fixtures (if applicable): `python manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/adamshaw90/RAD)
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/adamshaw90/RAD.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/adamshaw90/RAD)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/adamshaw90/RAD)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

The local version, created on Gitpod, does not have the functionality to send confirmation emails. This is due to the fact that Gitpod blocks the necessary email port required to carry out this operation. Gitpod blocks this port by default due to concerns about email spam and it cannot be changed.

## Credits

### Media


| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pixabay](https://pixabay.com/photos/tea-bag-dried-aroma-tee-5034097/) | 404 page | image | error page image |
| [Pixabay](https://pixabay.com/photos/coffee-coffee-sack-bags-659129/) | homepage | image | wholesale image |
| [Pixabay](https://pixabay.com/photos/coffee-machine-coffee-machine-3848316/) | wholesale page | image | image 1 |
| [Pixabay](https://pixabay.com/photos/coffee-beans-sack-burlap-colombia-1154356/) | wholesale page | image | image 2 |
| [Pixabay](https://pixabay.com/photos/vietnam-farm-vietnam-coffee-farm-5412741/) | about page | image | image 1 |
| [Pixabay](https://pixabay.com/photos/plant-bush-branch-grain-maturation-7599090/) | about page | image | image 2 |
| [Pixabay](https://pixabay.com/photos/coffee-beans-seed-caffeine-cafe-3392159/) | about page | image | image 3 |
| [Pixabay](https://pixabay.com/photos/coffee-beans-seed-caffeine-cafe-3392159/) | about page | image | image 3 |
| [canva](https://www.canva.com/) | home page | image | AI hero image |
| [canva](https://www.canva.com/) | home page | image | custom ufo/coffee beans image |
| [canva](https://www.canva.com/) | favicon | image | custom coffee bean image |

### Code

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [CodeInstitute](https://learn.codeinstitute.net/ci_program/diwad_v2_6) | checkout app | template code for the checkout and payment system | custom styles added |
| [CodeInstitute](https://learn.codeinstitute.net/ci_program/diwad_v2_6) | all pages | template code for the pop-up toasts | custom messages added |


### Acknowledgements

- I would like to thank my Code Institute cohort facilitator, Lewis Dillon for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and fellow students for the moral support.
- I would like to thank my wife Ottilie for putting up with my countless hours sat on my laptop whilst visiting various countries on a travelling vacation.

### Additional Information

- My env.py file was accidently pushed, which would have exposed secret keys. This was rectified and the keys were changed.