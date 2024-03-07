# Golfers Dream

![Am I responsive screenshot](documentation/images/am_i_responsive.png)

## Introduction

[Golfers Dream](https://golfers-dream-2d6e1b933be7.herokuapp.com/) is a website for a Golf Resort.

They offer hotel, restaurant, relaxation and most importantly Golf!

The idea is that people want to come here and thoroughly relax, with their favorite hobby attached.

You make one booking, and most things are included.

## Table of Contents

- [Golfers Dream](#golfers-dream)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Personas](#user-personas)
  - [User Stories](#user-stories)
  - [User Goals](#user-goals)
  - [Website Owner Goals](#website-owner-goals)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Colors](#colors)
  - [Screenshots of Finished Website](#screenshots-of-finished-website)
  - [Deployment](#deployment)

## User Personas

- A person whos favorite hobby is golf, wants an all inclusive golf vacation.
- A group of friends that play golf together, wants to get away on an all inclusive trip.
- A family wants bonding time over their hobby, with extra pampering on the side.

## User Stories

The user stories outlined in my [GitHub Project](https://github.com/users/hogbergmarkus/projects/14/views/1) is what drove my development of features.

I created epics with a following user story. Then created acceptance critera and tasks for each user story.

To implement agile methodology I utilized GitHub Projects, along with priority labels, and mapped them to a Milestone.

The user storys in my GitHub project are as follows:

- As a user I can easily navigate from the home page since it is not cluttered so that I can get to what I want fast.
- As a Site User I can create an account so that I can sign in.
- As a Site User I can make a booking with the resort so that I have a reservation.
- As a Site User I can go to my profile page so that I can see my bookings.
- As a Site User I can edit and delete my bookings so that I can adjust my bookings if I change my mind.
- As a Site Admin I can view contact requests from the contact form so that I can respond to the request.
- As a Site Admin I can create, read, update and delete user bookings so that I can manage the bookings.
- As a Site User I can view images and read about the resort so that I can decide if it is for me.

## User Goals

New user:

- I am able to find my way accross the website without hassle.
- I can read enough about the resort to understand what it is about.
- Sign up process is easy.
- I can contact the resort without registering for an account.

Returning user:

- Sign in is easy.
- My bookings are viewable, and I can manage them.
- I can contact the resort if I need to.

## Website Owner Goals

The purpose of this site is to attract golfers that want some extra luxury.

The interface is simple but striking. You should be attracted to the beautiful image of the golf course on the home page,

followed by the lyxury shown on the "what we offer" tab. That is if you don't immediately press the "Book Now" button.

The website should work on any device, mobile, tablet or desktop.

## Design

### Wireframes

You will find the link to my wireframes here: [WireFrames](https://github.com/hogbergmarkus/golfers-dream/tree/main/documentation/wireframes).

Alternatively go to my [GitHub repository](https://github.com/hogbergmarkus/golfers-dream) and look in the documentation folder.

### Fonts

I applied Roboto-Serif to the entire body, but overrid it for paragraphs with Roboto for better readability.

Roboto-Serif has that luxury feel that I was trying to achieve with the website,

while Roboto is less stylish, but easier to read.

### Colors

I used color extremely sparingly, only a slight shade to the navbar and footer.

I wanted the images to pop, and no distraction on the form pages except for the buttons.

## Screenshots of Finished Website

This is the landing page, beautiful in its simplicity.

![Homepage](documentation/images/home_screenshot.png)

On the tab "What we offer" potential custumers are further drawn in.

![What we offer](documentation/images/about_screenshot.png)

The contact page offers a contact form for everyone, signed in or not.

![Contact](documentation/images/contact_screenshot.png)

The booking page requires users to be signed in.

![Booking not signed in](documentation/images/booking_not_signed_in_screenshot.png)

If signed in, the booking page instead shows you a booking form.

![Booking signed in](documentation/images/booking_signed_in_screenshot.png)

Your Profile page is accessible after sign in. This is how it look without any bookings.

![Profile with no bookings](documentation/images/profile_no_bookings.png)

With some bookings it looks like this.

![Profile with bookings](documentation/images/profile_screenshot.png)

## Deployment

The project was deployed to Heroku as the steps below details.

- I set up a postgreSQL server at [elephantsql](https://customer.elephantsql.com/).
- Made sure to adjust the settings file accordingly, to utilize that database.
- Made sure to have my SECRET_KEY and DATABASE_URL in the env.py file.
- And the env.py file added to .gitignore.
- I installed gunicorn version 20.1.
- Add gunicorn to requirements.txt.
- Install whitenoise version 5.3.
- Add whitenoise to requirements.txt.
- Add whitenoise to middleware settings file.
- Also in the settings file create a path for whitenoise to collect static files.
- Create a Procfile, and declare it is a web process followed by the command to execute the project.
- Add a runtime.txt file to root directory, and add a supported python version as close as possible to my own.
- Run the command collectstatic, to collect static files.
- Set Debug to False in the settings file.
- Add Heroku to allowed hosts in the settings file (.herokuapp).
- Push the code to GitHub.
- Create a new app on [Heroku](https://id.heroku.com/login).
- On the settings tab of my app I clicked "Reveal Config Vars" and add DATABASE_URL and SECRET_KEY.
- DATABASE_URL got the value of my postgresql database url.
- SECRET_KEY got a very long and complicated value that I'm not going to tell you about!
- Then I went back to the deploy tab of my app, and clicked connect to GitHub.
- I then searched for my repository and connected it to the app.
- Click Deploy branch.

Here is a link to my Deployed project: [Golfers Dream](https://golfers-dream-2d6e1b933be7.herokuapp.com/)
