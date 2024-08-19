
# The Kids Kids Books Reviews Review

## Introduction

 Welcome to KidsBooks Reviews, the ultimate platform for discovering and sharing the joy of children's literature. Our mission is to foster a vibrant, inclusive community where parents, teachers, and young readers can find, review, and discuss books that inspire and educate. We are dedicated to curating a diverse collection of children's literature, making it easier to choose books that resonate with kids of all ages and backgrounds.

##   Project Overview
KidsBooks Reviews is designed to provide a comprehensive and user-friendly environment for reviewing and rating children's books. After signing up and logging in, users can interact with the platform by adding their own reviews, modifying their ratings, and managing their content. Our goal is to help users find quality literature and engage with the book community through honest and insightful reviews.

[Link to the live site](https://kids-books-review-3b6dc6d9b4c6.herokuapp.com/)

[Link to responsive design](https://ui.dev/amiresponsive?url=https://kids-books-review-3b6dc6d9b4c6.herokuapp.com/)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Agile](#agile)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

- After project purpose decided, lucichart is used to implement and plan the database structure.

### Data Models

- **User model**
  - Django pre-defined class-based model. Username and password implemented to login.

- **Review model**
  - | `book`       | ForeignKey  |
  - | `user`       | ForeignKey  |
  - | `content`    | TextField   |
  - | `created_on` | DateTimeField |
  - | `approval`   | BooleanField |

- **Ratings model**
  - | `book`       | ForeignKey  |
  - | `name`       | CharField   |


# user-experience-ux

## Overview

KidsBooks Reviews is a platform designed to help parents, teachers, and young readers discover and share the joy of children's literature. Our focus is on creating a vibrant, user-driven community where you can review and rate books, providing valuable insights for other users. After signing up and logging in, users can engage with featured books by adding their own reviews and ratings.

## Site User

Once you have set up your account, you can start using the platform to review books and manage your content. Here’s how you can get started:

- **Sign Up / Login:** Create an account or log in if you already have one.
- **Review a Book:** Select a book to leave a review or rating based on its content and your experience.
- **Manage Your Reviews:** Edit or delete your own reviews and modify your ratings as needed.
- **Explore Content:** Browse and search for books by title, author, or category to find the perfect read.

## Purposes for the Site
KidsBooks Reviews aims to provide a reliable resource for discovering high-quality children’s literature. Our project supports parents, educators, and community members in finding books that are both educational and engaging, ensuring that each child finds stories that resonate with them.

           
### Colour schemes
The colour schemes generated from [cooler](https://coolors.co/c9daea-03f7eb-00b295-191516-ab2346) 

### Font
[Googlefont](https://fonts.google.com/) of Lato used.


# agile

## Agile development

In the development life-cycle of Kids Books Review, Agile methodology was used to ensure iterative and efficient progress throughout the project development. Central to this approach was the utilization of a Kanban board hosted on GitHub Projects. You can view the project board as: [KANBAN Board](https://github.com/users/NeeruRathour/projects/6).


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


# Features

- **Book Reviews:** Users can submit and view reviews and ratings for children's books. Ratings are averaged to reflect the book’s overall reception.
- **Review Management:** Users can create, read, edit, and delete their own reviews. They can also modify their ratings for previously reviewed books.
- **Content Moderation:** The platform includes tools for monitoring and managing submitted content to ensure quality and relevance.


## Features Implemented

- **Full CRUD Operations on Reviews:** Logged-in users can create, read, edit, and delete their own reviews and ratings.
- **Admin Controls:** Site administrators can maintain and oversee submitted book reviews and entries.

## Getting Started

1. **Sign Up / Login:** Register for an account or log in to access full features.
2. **Browse Books:** Explore our collection and select books to review.
3. **Submit Reviews:** Add your reviews and ratings for books you’ve read.
4. **Manage Content:** Edit or remove your reviews and ratings as needed.

### Navbar and Footer:
- Unified Navbar and footer on every page
- Navbar's changes as signing in status,logged in user can see add a Kids Books Review tab
- Footer includes copyrights and about us links. 

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
- Search Functionality
    - Given a logged-in site user, user can find books by keywords in the title, author, or by category (Fiction, Non-Fiction, Science Fiction, Children's & Teenage Books).

# Testing 

## Validation
### HTML
[W3 HTML Validator](https://validator.w3.org/) 

### CSS
[W3 CSS Validator](https://jigsaw.w3.org/css-validator/) 

### Python
[CI Python Linter](https://pep8ci.herokuapp.com/) 


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
