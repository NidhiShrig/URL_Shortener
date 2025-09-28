# Django URL Shortener

A simple web application built with Django that allows users to shorten long URLs into easy-to-share short links. Users can enter any valid URL, and the system generates a unique short code that redirects to the original URL. The app also tracks the number of times each short URL is accessed.  

This project demonstrates core Django concepts including models, views, templates, forms, URL routing, and CRUD operations.

## Features

- Shorten long URLs to concise, unique links
- Redirect short URLs to original URLs
- Track the number of clicks for each URL
- Admin panel to manage URLs
- Responsive interface using Bootstrap

## Project Structure

url_shortener_project/
│
├── manage.py
├── db.sqlite3
│
├── url_shortener_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── shortener/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── migrations/
│ │ ├── init.py
│ │ └── ...
│ └── templates/
│ └── home.html

## Installation

1. **Clone the repository**  
```bash
git clone <repository-url>
cd URL_Shortener


2.Create a virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate 

3. Install dependencies
pip install django

4.Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional, for admin panel)
python manage.py createsuperuser

6.Run the development server
python manage.py runserver

7. Access the app
Home page: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/

8.Usage
- Enter a long URL in the form on the home page.
- Click Shorten URL.
- The generated short URL will appear; clicking it will redirect to the original URL.
- Admin can manage all short URLs and view click counts.

9.Technologies Used
Python 3
Django Web Framework
SQLite (Database)
Bootstrap 5 (Frontend Styling)