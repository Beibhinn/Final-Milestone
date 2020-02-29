# Final Milestone - Unicorn Attractor
[![Build Status](https://travis-ci.org/Beibhinn/Final-Milestone.svg?branch=master)](https://travis-ci.org/Beibhinn/Final-Milestone)

* [Unicorn Attractor](#unicorn-attractor)
  + [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
  + [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  + [Technologies Used](#technologies-used)
  + [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  + [Deployment](#deployment)
  + [Credits](#credits)
    - [Content](#content)
    - [Layout](#layout)
    - [Media](#media)
    - [Templates](#templates)
    - [Theme](#theme)
      




  
## Unicorn Attractor  
  
For my final milestone project for the Full-Stack software development course with Code Institute, I decided to follow the suggested brief, and created an issue management/ bug tracker website. 
  
From a user perspective, I have come across similar functionality on the web. Often while researching errors or issues for packages, I would find myself on a page detailing a ticket where someone experienced the same or a similar issue to me. This could be extremely useful at times, as by reading over the ticket and comments I would come across potential fixes. 
From the other side, I also appreciated that while working on a number of different tickets or issues at once, it is important to keep organised. For this reason, I wanted my project to also serve the developer well, by laying information out clearly. 

In this project I aimed to offer a positive experience and a useful tool to both staff and users.
  
My website can be found at the following URL: https://beibhinn-final-milestone.herokuapp.com/  
  
### UX  
  
#### User Stories  
- As a guest, I want to be able to browse existing bugs and features.
- As a guest, I want to be able to read through the detailed tickets for bugs and features, and the related comment threads.
- As a user, I want to be able to sign up for an account.
- As a user, I want to be able to sign in and out of my account, and access stored issues relevant to me.
- As a user, I want to be able to search for relevant bugs/ features.
- As a user, I want to be able to add a bug or feature that I haven't been able to find on the site yet.
- As a user, I want to be able to see the status of the bug/ feature as it progresses.
- As a user, I want to be able to comment on existing bugs/ features, to let others know of any suggestions, and to highlight if I also have the same problem.
- As a user, I want to be able to upvote bugs to indicate that I also have the same problem. (Only 1 vote per person per bug is expected).
- As a user, I want to be able to remove my upvote from a bug if I change my mind.
- As a user, I want to be able to choose a donation amount for a feature, then add it to my cart, in case I want to donate to multiple features. (This avoids the need for multiple payments).
- As a user I want to be able to edit my cart before proceeding to the payment screen.
- As a staff member, I want to easily be able to update the status of a bug/ feature, to keep our users as informed as possible.  
  
#### Wireframes  
The wireframes I created for this project can be viewed [here.](https://github.com/Beibhinn/Final-Milestone/blob/master/wireframes/wireframes.pdf)  
  
### Features  
  
#### Existing Features  
  
- **Registration/ Login**: Allows users to create an account and login with a unique username and password.   
- **Profile**: User gets their own profile page where they can view/change their profile picture as well view as bugs/ features they've added to the site, bugs they've upvoted, and features they donated to.
- **Navigation: header & footer**: The site name in the top left corner acts as a brand/logo which redirects users to the home page. Other navigation links are along the left side, directing the user to other relevant pages. Footer informs the user that the site is hosted by Heroku, and provides as link to where they can view the source code on Github.
- **Home Page**: Allows all users to view the current bugs and features on the site, as well as their status. From this page, the user can search for existing issues and redirect to the forms for adding a new bug or issue. The user can also upvote a bug if they are logged in, and can add a donation amount for a particular feature to their cart. By clicking on the link for a bug/ feature, the user is redirected to a detailed view of that issue. Staff members can drag a bug or a feature to a new status column to update its status quickly and easily.
- **Bugs/ Features**:  These pages allow the users to view only bugs or only features. Each ticket displays a coloured status so the user can easily recognise their current state. Each issue has a link to a page containing more details about that issue.
- **Bug/ Feature detail view**: Allows all users to view detailed information for a particular issue, including who added it, when it was added, its status, its full description, how many views it has, and how many votes/ donations. (Any attachment included as part of the ticket will also be visible here). It also allows signed in users to comment. Guests will not be given the option to sign in but will be able to read existing comments.  
- **Add bug/ feature**:  Allows signed in users to add a new bug or feature to the site.
- **Charts**: Visually displays the proportion of bugs/ features in each status relative to the total number of bugs/features.
- **About us**: Provides information about how the site works & how to use it.
- **Cart**: Pending donations for features are stored in the cart until the user is ready to proceed to checkout. User can edit the amount they want to donate per feature, as well as remove a feature from their basket altogether.  Total donation amount is also visible here. 
- **Checkout**: The user can enter their payment details and complete the transaction. Once this is complete, the features they donated to will be visible in the users account.   
      

  
#### Features Left to Implement  
  
 - **Assign issue**: A feature where the admin would be able to assign the task to a particular member of staff, to indicate that they are resposible for that ticket and are working on it. As there is only one developer on this team at the moment, not necessary to implement yet. 
 - **Sorting**: A feature to allow the user to sort by date added, views, votes or donations.    
 -  **Graphs**: A visual record of progress made over time on all bugs and features. Not necessary at this point as there are not sufficient issues to aggregate the data in a meaningful way.
 - **Delete function**: At this time, the admin can delete issues only through the the django admin site. In a later update, I plan to allow the user who created the issue to delete it before it is 'in progress', and allow staff to delete any issue during any status.
  
### Technologies Used  
   
 - **HTML5**: HTML5 was used to create the structure of the website  
 - [**CSS**:](https://sass-lang.com/documentation/syntax) CSS was used to style the website.  
 - [**JQuery**:](https://jquery.com) JQuery was used to simplify DOM manipulation.  
 - [**Font Awesome**:](https://fontawesome.com) Font Awesome was used to add icons to the site, such as the upvote and cart icons.  
 - [**Bootstrap 3.3**:](https://getbootstrap.com/docs/3.3/) As Bootstrap is designed with the Mobile First Approach in mind, this framework was used to help structure the website, ensuring that it would be compatible on mobile devices. 
 - [**Django 1.11.23**:](https://www.djangoproject.com/download/) Django was used as it is an easy-to-use and flexible RESTful framework. Its built-in templating engine allows for rapid prototyping and iterating of pages and endpoints.  
 - [**Python 3.7**:](https://www.python.org/) This is the latest, most stable version of Python, and was used to create the backend of the site.  
 - [**Whitenoise**:](http://whitenoise.evans.io/en/stable/) Whitenoise was used to allow us to serve our static files on Heroku.
 - [**Stripe**:](https://stripe.com/gb) Stripe was used to process of user payments securely. 
 - [**django-avatar**:](https://django-avatar.readthedocs.io/en/latest/) Django-avatar was used to facilitate the addition of an avatar to user profiles.
 - [**django-comments-xtd**:](https://django-comments-xtd.readthedocs.io/en/latest/) This was used to add the comment funcationality to bug and features.. 
      
### Testing  
  
#### Manual Testing  
  
 - *Navbar* :  
    - Click on each of the links within the menu (including the logo), and verify that each one is functioning correctly, and that they take the user to the correct page.  
    - While not logged in, click 'add a bug' and verify you are directed to the login page rather than the form to add a new bug.
    - While not logged in, click 'add a feature' and verify you are directed to the login page rather than the form to add a new feature.
    - Under account access, verify the options given are 'login' or 'register' while not logged in, and 'profile' and 'logout' when logged in.
  
 - *Home page/ Dashboard* :  
    - Click a title link of a bug & feature to verify you are redirected to a page displaying the issue's full details.  Navigate back to dashboard & check the views count has increased by 1.
    - Click the upvote icon for a bug and ensure the icon toggles to a filled-in version & upvote counter increases.
    - Toggle the upvote icon again, ensure the icon reverts back to as it was to begin with and the counter decreases.
    - Enter a donation amount for a feature and add to cart. Ensure a badge appears on the cart in the nav and click to confirm that the feature and amount have been added. Click 'view cart' and verify you are redirected to the cart page.
    - While logged in as staff/ admin, drag an issue from the 'to do' column to another. Click its title to view the issue details and verify it now says 'Started on:' and indicates a date, as well as the date of creation. 
    - Drag an issue to the 'done' column and click to view its details. Verify the date of completion is also now showing.
    -   Type a search term in the search bar and submit, ensuring that you are redirected to a page with the results. 
  
 - *Register page* :  
    - Fill out the form using a name that is already in use. Verify an error is shown and an account is not created.
    - Fill out the form using an email that is not valid. Verify an error is shown and an account is not created.
    - Fill out the form where the 'password' and 'password confirmation' inputs don't match. Verify an error is shown and an account is not created.
    - Click 'Log in here' button to ensure you get redirected to the login page instead.
    - Fill out the form with valid details. Confirm an account is created and you are logged in.  
  
 - *Login Page* :  
    - Enter a username that hasn't been registered, verify an error is shown and the user is not logged in.
    - Enter a correct username and an incorrect password. Verify an error is shown and the user is not logged in.
    - Click the 'register now' link and ensure you are redirected to the register page.
    - Click 'Forgot my password' and verify you are redicted to a new page. Enter your email and submit. Check you've been redirected to a page confirming a password reset email has been sent. Verify links redirect to the expected places.
    - Enter a correct username and associated password. Ensure user is logged in successfully.
     
 - *View bugs* :  
    - Click a title link of a bug & feature to verify you are redirected to a page displaying the issue's full details.  Navigate back to dashboard & check the views count has increased by 1.
    - Click the upvote icon for a bug and ensure the icon toggles to a filled-in version & upvote counter increases.
    - Toggle the upvote icon again, ensure the icon reverts back to as it was to begin with and the counter decreases.
 
 - *Bug/ Feature detail* :  
    - Verify the details are all displaying, including that the number of comments matches how many comments are visible. 
    - Verify that only when logged in as the user who created the issue or staff, an edit button appears in the top right which brings the user to a form to edit.
    - Toggle the upvote button for the bug and verify the icon and counter change. For a feature, add a donation amount to the cart and verify it shows up in the cart in the nav.
    - Verify that when not logged in, the user cannot post a comment and is prompted to sign in and register.
    - Verify that when signed in, a user can post a comment and have it appear in the thread.
  
 - *View features* :  
    - Click a title link of a feature& feature to verify you are redirected to a page displaying the issue's full details.  Navigate back to dashboard & check the views count has increased by 1.
    - Add a donation amount to the cart and verify it shows up in the cart in the nav.
  
 - *Account view* :  
    - Verify your custom profile picture or the default avatar is visible. Click the link underneath and verify you are directed to a page where you can upload and choose your image.
    - Ensure the first tab shows only issues added by you. Toggle upvotes and add donations as in previous testing.
    - Ensure the second tab displays only bugs you've upvoted, and that if you remove your vote and refresh the page, that bug will no longer be visible here. 
    - Ensure the last tab shows features you have donated to, as well as how much you've already donated.
  
 - *Add bug form* :  
    - Try to submit the empty form and verify that the required fields are indicated  
    - Fill out the form with valid details. Go back to the bugs page or dashboard and verify the new bug is now showing, with a 'created' status.
  
 - *Edit bug form* :  
    - While logged in as the creator of a bug or as staff, go to the 'edit bug' page and verify the existing information automatically populated into the form.  
    - Make whatever changes you wish to your bug, then submit. Go back to the bugs page or dashboard and verify that it is showing the updated information.  
    - Attempt to edit a bug that was not created by you by visiting the appropriate URL (/bugs/edit/{{ bug id}} ) and verify you cannot access this page.

 - *Add feature form* :  
    - Try to submit the empty form and verify that the required fields are indicated  
    - Fill out the form with valid details. Go back to the features page or dashboard and verify the new feature is now showing, with a 'created' status and no donations yet.
  
 - *Edit feature form* :  
    - While logged in as the creator of a feature or as staff, go to the 'edit feature' page and verify the existing information automatically populated into the form.  
    - Make whatever changes you wish to your feature, then submit. Go back to the features page or dashboard and verify that it is showing the updated information.  
    - Attempt to edit a feature that was not created by you by visiting the appropriate URL (/features/edit/{{ feature id}} ) and verify you cannot access this page.
  
 - *Search* :  
    - Type a search term (eg. 'link') into the search bar and submit. Verify you're redirected to a search results page which shows the results, if any. If no results, user should be prompted to add a bug/ feature
    - Do usual testing of all links, toggling upvotes and adding donation to cart.

 - *Cart* :  
    - Verify all features you added to the cart appear.
    -  Amend a donation by typing in the new amount and clicking the 'amend' button. Ensure 'Current donation value in cart' changes to reflect the new donation amount.
    - Remove a donation from your cart by clicking the 'delete' button. Ensure it no longer appears in the cart.
    - Click 'donate' and verify you are redirected to the checkout page 

 - *Checkout* :  
    - Verify all features you want to donate to are appearing
    - Check the total donation amount to be sure it matches the total of all the feature donations.
    - Enter the testing card number for stripe `4242424242424242` , any 3 digits for the security code and any future date for the expiry.
    - Verify you are redirected to the features page and get a success message indicating your donation was successful. 

 - *Charts* :  
    - Verify a chart is shown for both bugs and features, which is colour coded according to the colour of the status it is currently in. (Shown on the status banner and gutter of each issue).
    - When hovered over, ensure the number of bugs/ features in that status is shown.
  
####  Automated Testing  
  
While manual testing was done on every feature possible, I also wrote some tests in order to automate the process, and ensure everything was working as it should, to the best of my ability. Unit testing can be found in the following locations:
 - Search 
	 - [tests](https://github.com/Beibhinn/Final-Milestone/blob/master/search/tests.py)
- Features
	- [tests](https://github.com/Beibhinn/Final-Milestone/blob/master/features/tests.py)
	- [forms](https://github.com/Beibhinn/Final-Milestone/blob/master/features/test_forms.py)
	- [models](https://github.com/Beibhinn/Final-Milestone/blob/master/features/test_models.py)
	- [views](https://github.com/Beibhinn/Final-Milestone/blob/master/features/test_views.py)
- Checkout
	- [tests](https://github.com/Beibhinn/Final-Milestone/blob/master/checkout/tests.py)
	- [models](https://github.com/Beibhinn/Final-Milestone/blob/master/checkout/test_models.py)
	- [views](https://github.com/Beibhinn/Final-Milestone/blob/master/checkout/test_views.py)
- Cart
	- [tests](https://github.com/Beibhinn/Final-Milestone/blob/master/cart/tests.py)
	- [views](https://github.com/Beibhinn/Final-Milestone/blob/master/cart/test_views.py)
- Bugs 
	- [tests](https://github.com/Beibhinn/Final-Milestone/blob/master/bugs/tests.py)
	- [forms](https://github.com/Beibhinn/Final-Milestone/blob/master/bugs/test_forms.py)
	- [models](https://github.com/Beibhinn/Final-Milestone/blob/master/bugs/test_models.py)
	- [views](https://github.com/Beibhinn/Final-Milestone/blob/master/bugs/test_views.py)

 To run the tests simply perform `python manage.py test`. These tests focus on the behaviours/ possible actions of the users as they interact with the website, and the expected outcomes of these interactions. The tests verify that all pages and templates are rendered as expected, and also tests CRUD functionality for the database.   

This project is responsive, adjusting and resizing dependant on screen size. This was tested using devices with various screen sizes, as well as the ‘responsive design mode’ tool in firefox and chrome.
  
  
### Deployment  
  
The source code can be viewed on [GitHub](https://github.com/Beibhinn/Final-Milestone).  A live demo has been deployed to [Heroku](https://beibhinn-final-milestone.herokuapp.com/).  
  
In order to deploy to Heroku, a Procfile has to first be created to allow Heroku to identify the type of application being handled. The required modules need to be exported to a requirements.txt file so that all dependencies could be automatically installed by the host. A Heroku remote was added to the git repository so that the project could be deployed to Heroku via `git push`.  
  
The app relies on the following environment variables, which can be set for Heroku via the web console. If deploying locally, setting these depends on the operating system used.  
  

|||
| --- | --- |
| AWS_ACCESS_KEY_ID| `<your_id_goes_here>` |  
| AWS_SECRET_ACCESS_KEY | `<your_access_key_goes_here>`  |  
| DATABASE_URL | `<your_database_url_key_goes_here>` |  
| DISABLE_COLLECTSTATIC | `1` |  
| SECRET_KEY | `<your_secret_key_goes_here>` |  
| STRIPE_PUBLISHABLE | `<your_stripe_publishable_key_goes_here>` |  
| STRIPE_SECRET | `<your_stripe_secret_key_goes_here>` |  
| EMAIL_USER | `<your_email_address_goes_here>` |  
| EMAIL_PASSWORD | `<your_email_password_goes_here>` |  
  
  
To deploy locally:  
- Clone repository, open terminal in repository folder  
- `pip install -r requirements.txt`  
- `python app.py`  
- In settings.py, uncomment `import env` 
- Set the environment variables. Ie. set IP to `127.0.0.1` and the others as normal
- In base.html, go to the `toggleUpvote` function in the scripts and change the url from `https://` to `http://`. You can't run this with https in localhost
- Open `http://localhost:<PORT>`  
  
### Credits  
  
#### Layout

I took inspiration for my dashboard layout and functionality from the following sites:
- [Asana](https://asana.com/)
- [Backlog](https://backlog.com/)
- [Basecamp](https://basecamp.com/)
- [Bugzilla](https://bugzilla.mozilla.org/home)
- [Jira](https://www.atlassian.com/software/jira)
- [nTask](https://www.ntaskmanager.com/product/issue-management-software/)
- [Trello](https://trello.com/)
  
#### Media  

- [Logo/ Favicon](https://img.icons8.com/plasticine/100/000000/unicorn.png)
- [Default user avatar](https://community.spotify.com/t5/media/gallerypage/image-id/75447i3FF8FE0DEA7D5BCD)
- [Guest avatar](https://cdn0.iconfinder.com/data/icons/unigrid-flat-human-vol-2/90/011_101_anonymous_anonym_hacker_vendetta_user_human_avatar-512.png)

#### Templates
To expedite development time, I made use of code previously used as part of the Code Institute's Full Stack Development course, for the ecommerce project. This was the code relating to user and account authentication and the source repository can be found [here.](https://github.com/Code-Institute-Solutions/proposed_django_authentication)

#### Theme
I used a Bootswatch theme for this project. [SB Admin 2](https://startbootstrap.com/template-overviews/sb-admin-2/) is an open source admin dashboard theme for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/). You can find the GitHub repository [here.](https://github.com/BlackrockDigital/startbootstrap-sb-admin-2)
