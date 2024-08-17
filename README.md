
# The Kids Kids Books Reviews Review

## Introduction

 The Kids Kids Books Reviews Review project is focused on safeguarding vulnerable individuals, especially children, from the threat of radicalization, akin to how other forms of harm are addressed in safeguarding efforts. The project aims to foster a safe community by providing tools to help monitor, review, and analyze content that may influence young minds.

##   Project Overview
In today's world, protecting communities from radicalization is just as critical as any other form of safeguarding. This project aims to provide a platform that not only reviews children's Kids Books Reviews but also monitors the content for any potentially harmful or radicalizing material.

This project is designed to help parents, educators, and community members identify books that are safe, educational, and free from radicalizing content, while also offering an interface to flag or report questionable material.

![Responsive Mockup](documentation/screenshots/Screenshot1.responsive.webp)

[Link to the live site](https://book-shelf-e3665f129252.herokuapp.com/)

## Index – Table of Contents
* [User Experience (UX)](#ser-experience-ux) 
* [Agile](#agile)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Database plan
## Data structure in Lucichart

![Datastructure Mockup](documentation/screenshots/Screenshot2_datamodel.webp)

- After project purpose decided, lucichart is used to implement and plan the database structure.
- The above diagram is serving as an guide to indicate the field types and relationships between data stored in database.

## Data models

- User model
 - -  Django pre-defined class-based model. Username and password implemented to login.
- Book model
 - - | title | CharField | | pages | integerField | | author | CharField | | description | TextField | | created_on | DateTimeField | | approval | BooleanField | | category | ForeignKey | | updated_on | DateTimeField | | image | CloudinaryField || user | ForeignKey |
- Review model
 - - | book | ForeignKey | | user | ForeignKey | | content | TextField | | created_on | DateTimeField | | approval | BooleanField |
- Category model
 - -  | book | ForeignKey | | name | CharField |

[Back to Top](#top)


# user-experience-ux

## Overview

The UX design focuses on creating an engaging and welcoming environment. After signup and logging in, the site user would be able to add a new book they would like to share with other users and add a review to any books. They can search book by book name key words, book author key words or book 4 categories(Fiction,Non_fiction,Science_fiction and Children'S&Teenage).

## Site User
Once the project is set up, you can start using the platform to review books and monitor content. Here’s how you can get started:

- Sign Up / Login: Create an account or log in if you already have one.
- Browse Books: Navigate through the list of books available on the platform.
- Review a Book: Click on a book and leave a review or rating based on its content.
- Flag Content: If you notice any questionable content, use the flagging feature to report it.
Access Resources: Visit the resources section for educational materials and guides.


## Purposes for the site
 This project is designed to help parents, educators, and community members identify books that are safe, educational, and free from radicalizing content, while also offering an interface to flag or report questionable material.



## Wireframes created in Balsamic
- Home Page for mobile screen
  - ![Datastructure Mockup](documentation/wireframes/wireframe_homepage_mobilescreen.webp)

- Home Page for pad/laptop screen
  - ![Datastructure Mockup](documentation/wireframes/wireframe_homepage_padlaptopscreen.webp)

- About Page
  - ![Datastructure Mockup](documentation/wireframes/wireframe_aboutpage.webp)

- Book detail page for logged in user
  - ![Datastructure Mockup](documentation/wireframes/wireframe_bookdetail_loggedin.webp)

- Add a book page for logged in user
  - ![Datastructure Mockup](documentation/wireframes/wireframe_addbook_loggedin.webp)

### Colour schemes
The colour schemes generated from [cooler](https://coolors.co/c9daea-03f7eb-00b295-191516-ab2346) as below:
![Colourscheme Mockup](documentation/colour-palette/color_scheme.webp)

### Font
[Googlefont](https://fonts.google.com/) of Lato used.

[Back to Top](#top)


# agile

## Agile development

In the development life-cycle of Kids Books Review, Agile methodology was used to ensure iterative and efficient progress throughout the project development. Central to this approach was the utilization of a Kanban board hosted on GitHub Projects. You can view the project board as: [KANBAN Board](https://github.com/users/NeeruRathour/projects/6).

 -![Kanban Mockup](documentation/screenshots/Kanban_board.webp)

### Kanban overview
The Kanban board served as a visual representation of the project's progress and allowed for effective task management. It consisted of the following sections:

- Todo: This section contained all the tasks and user stories that were yet to be prioritized for implementation.
- In Progress: Work in progress was tracked here, indicating tasks actively being worked on.
- Done: Tasks that were completed successfully were moved to this column.

### User Stories Integration
User stories played a pivotal role in shaping the development process, ensuring that features were aligned with user needs. These user stories were mapped onto the Kanban board, guiding the prioritization and implementation of tasks.

### Task Management
In addition to tracking user stories, the Kanban board served as a comprehensive task list. Tasks utilized as breaking down user stories into smaller, actionable units, ensuring clear and manageable objectives for development. This specific approach facilitated efficient progress tracking.

By leveraging Agile principles and utilizing the Kanban board effectively, the development of Kids Books Review remained focused, adaptable, and responsive to evolving requirements, resulting in a more robust and user-centric Django application.

## User Stories Overview
### List of User Stories




- [#1 View comments/reviews ](https://github.com/NeeruRathour/kids-books-review/issues/3)
- [#2 Account registration ](https://github.com/NeeruRathour/kids-books-review/issues/4)
- [#3 Post a review on book ](https://github.com/NeeruRathour/kids-books-review/issues/5)
- [#4 Modify or delete reviews of a book ](https://github.com/NeeruRathour/kids-books-review/issues/6)
- [#5 View list of books ](https://github.com/NeeruRathour/kids-books-review/issues/1)
- [#6 click on book for details ](https://github.com/NeeruRathour/kids-books-review/issues/2)


### MOSCOW Details
- MO (Book CRUD | Review CRUD | Account registration | )
- S ( Approve book reviews | Approve book | About page | Search book)
- CO (View paginated books | Templates styling | )
- W (Log in via social media account | Profile page)

[Back to Top](#top)

# Features

-  Book Reviews: Users can review and rate children's Kids Books Reviews based on their content, educational value, and overall impact on young readers.
-   Content Monitoring: The platform offers automated tools to scan and analyze text for any signs of radicalization or harmful ideologies.
-   Community Flagging: Members of the community can flag content that they find concerning, which will then be reviewed by moderators.
-   Educational Resources: Provides resources and guides for parents and educators on how to discuss sensitive topics with children.


## Features implemented

- Full CRUD on review of a Kids Books Review: the logged-in site user can create, read, edit and delete their review on a Kids Books Review
- Full CRUD on a Kids Books Review: the logged-in site user can create,read,edit and delete their Kids Books Review
- Search a Kids Books Review via key words in Kids Books Review title or Kids Books Review author or 4 categories(Fiction,Non_fiction,Science_fiction and Children's&Teenage Kids Books Reviews)
- The site admin maintain the submitted Kids Books Reviews and reviews of specific Kids Books Reviews.

- ![Kids Books Review Mockup](documentation/screenshots/Kids Books Review_add.webp)
- ![Kids Books Review_rud Mockup](documentation/screenshots/Kids Books Review_rud.webp)
- ![review_crud](documentation/screenshots/reviews_crud.webp)
- ![search](documentation/screenshots/search.webp)

### Navbar and Footer:
- Unified Navbar and footer on every page
- Navbar's changes as signing in status,logged in user can see add a Kids Books Review tab
- Footer includes social links and github links

### Index page:
- The homepage provides the list of Kids Books Reviews
- It can be accessed without signing in

### About Us page:
- About page includes a short brief instruction on the Kids Kids Books Reviews Review site
- It can be accessed without signing in

### Responsiveness
- There's a hamburger navbar on mobile size screen

## Future features
- Log in via social account
    - At the home page, the site user can select the logging in approach via social medai account.
    - The user can select via faceKids Books Review, twitter, or instgram account to log in and log in successfully with approriate incredientials.
- Profile page
    - Given a logged-in site user, view the summary list of Kids Books Reviews and reviews user submitted in a seperate page.
    - Given a logged-in site user, view the status of the Kids Books Reviews and reviews user submitted.
    - Given a logged-in site user, user can check and update their name and password.

[Back to Top](#top)

# Testing 

## Validation
### HTML
[W3 HTML Validator](https://validator.w3.org/) to check the HTML
screenshot

### CSS
[W3 CSS Validator](https://jigsaw.w3.org/css-validator/) to check the CSS
screenshot

### Python
[CI Python Linter](https://pep8ci.herokuapp.com/) to check python scripts
screenshot

## Manual test
### Home page
Test Result

### About page
Test Result

### Footer/NAVBar
Test Result

### Login/logout/registration page
Test Result

### Review CRUD
Test Result

### Kids Books Review CRUD
Test Result

### Search a Kids Books Review
Test Result

[Back to Top](#top)

# technologies-used
The technologies implemented in this application included HTML5, CSS, Bootstrap, Javascript , Python , PostgreSQL , Heroku and Django.

- Python used as the back-end programming language.

- Git used for version control.

- GitHub used for secure online code storage.

- Gitpod used as a cloud-based IDE for development.

- Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.

- PostgreSQL used as the ratioanl database.

- Lucidchart - for database ER diagrams.

- Heroku used for hosting the deployed full stack site.

- Cloudinary used for online static file storage.

- Balsamiq utilized for design and prototyping(wireframes).

- Google,Stack Overflow and ChatGPT utilized for general research or solving a bug, information gathering, and various online tools.

[Back to Top](#top)

# Deployment

## Deployment Guide
### Deployment Steps:
- Creating the Heroku App account
- In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Create a unique name for your project.
- Select the closest region in this case is EURO Region
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

### Setting Up Environment Variables
- Add Heroku to the ALLOWED_HOSTS list.
- Configure static files and templates directories in settings.py.
- Migrate the models to the new database connection in the terminal.
- Create env.py in the top level of the Django app.
- Import os in env.py.
- Set up necessary environment variables in env.py, including the secret key and database URL.
- Update settings.py to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".

### Creating Procfile and Pushing Changes
- Create a Procfile in the top level directory.
- Add the command to run the project in the Procfile.
- Add, commit, and push the changes to GitHub.

### Heroku Deployment
- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Make sure to resolve any deployment errors by adjusting the code as necessary.

### Forking the Repository
Forking the GitHub Repository allows you to create a copy of the original repository without affecting it. Steps are as below:

- Log in to GitHub or create an account.
- Visit the repository link.
- Click on "Fork" at the top of the repository.

### Creating a Clone of the Repository
Creating a clone enables you to make a local copy of the repository. Steps are as below:

- Navigate to the Kids Kids Books Reviews Review repository.
- Click on the <>Code button.
- Select the "HTTPS" option under the "Local" tab and copy the URL.
- Open your terminal and change the directory to your desired location.
- Use git clone followed by the copied repository URL.

[Back to Top](#top)

# Credits
## Images 
- Background image and Kids Books Review featured images for the mock content were taken from free stock photos on [Pexels](https://www.pexels.com/)
- Image format conversion done via [freeconvernt](https://www.freeconvert.com/png-to-webp)
 

## Code
- Code Institute course content for providing the knowledge and guidance to build the project
- GitHub user katiejanecoughlan and Gordon-Meade for sharing a best practice README structure
- Course Facilitator Alexander and David Calikes continued support and guidelines.
- Tutor Kevin, Spencers and Martin's subject matter sessions and coding sessions.
- Fellow cohort peers support and knowledge sharing during the course learning journey.

[Back to Top](#top)
