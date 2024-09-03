
# The Anime Radio Website

This repository contains the source code for The Anime Radio website, developed using Django. The site is designed to serve as a central hub for anime enthusiasts, providing information, updates, and community interaction centered around anime. It features a complete anime recommendation engine based on a SQL Lite database. User Authentication and Registration. Polling and voting Apps and Much More. 

## Repository Structure

The repository is organized as follows:

- **Django Project Files**:
  - `manage.py`: Django's command-line utility for administrative tasks.
  - `settings.py`: Configuration settings for the Django project, including installed apps, middleware, and templates.
  - `urls.py`: URL routing for the website, directing traffic to the appropriate views.
  - `wsgi.py` and `asgi.py`: Entry points for WSGI/ASGI-compatible web servers to serve your project.
  
- **Main App**:
  - `home/`: Contains the main application that handles the home page and other static pages like the About and Contact sections.
    - `models.py`: Defines the data models for the application.
    - `views.py`: Contains the logic for rendering the website's pages.
    - `urls.py`: URL configurations specific to this app.
    - `templates/`: HTML templates that define the structure of the website.
    - `static/`: Static files such as CSS, JavaScript, and images used in the app.
    
- **Templates**:
  - `base.html`: The base template that includes the common layout for all pages.
  - `home.html`: The template for the home page.
  - `about.html`: The template for the About page.
  - `contact.html`: The template for the Contact page.
  
- **Static Files**:
  - `css/`: Contains custom stylesheets.
  - `js/`: Contains custom JavaScript files.
  - `images/`: Includes images used throughout the website.

## Features

- **Django Framework**: The website is built using Django, a powerful Python web framework that promotes rapid development and clean, pragmatic design.
- **Static Pages**: The site includes several static pages such as Home, About, and Contact, offering a structured and informative experience for visitors.
- **Responsive Design**: The website is fully responsive, ensuring it looks good on all devices, from desktops to smartphones.
- **Extendable Architecture**: Built with Django, the project is easily extendable. New features and applications can be integrated smoothly.

