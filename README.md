# DevTrack.io - Personal Developer Progress Tracker

A full-stack Django web application that helps developers track their learning, coding challenges, and daily progress across platforms like AlgoMap and LeetCode.

## Why I made this project

I started this project because I wanted to see my progress all in one place while also getting better at building full-stack applications. I didn't want to build something I wouldn't use — like a blog app. I will be using this application myself, and it is easily scalable so I can add more features as I keep improving as a developer. This project has really helped speed up my learning of real-world Django development while also practicing problem solving on LeetCode at the same time. If you're looking at the code and wondering why there are so many comments, it's because I was learning the Django framework as I built it.

## Overview

**DevTrack.io** is a productivity and learning companion for developers. It allows you to:
- Track AlgoMap / LeetCode problems you've completed
- Rate their difficulty (Easy, Medium, Hard)
- Store notes and reflections on each problem
- Log learning milestones
- View your overall progress on a personal dashboard

## Features

### User Accounts
- Login, Sign Up and Logout
- Secure authentication using Django's built-in User model
- Personal data — each user only sees their own problems and milestones

### Problem Tracker
- Add problems you've solved (LeetCode, AlgoMap, Custom)
- Custom difficulty rating (Easy, Medium, Hard)
- Notes for explanations or thoughts
- Automatic date tracking

### Learning Milestones
- Log milestones as you progress through topics
- Add a description and date achieved
- View all your milestones in one place

### Dashboard
- Total problems solved
- Difficulty breakdown (Easy / Medium / Hard)
- Recently solved problems table

## Tech Stack
- Python 3
- Django
- SQLite
- HTML/CSS (Django Templates)
- Bootstrap
- Docker

## Running with Docker
```bash
git clone https://github.com/yourusername/devtrack.git
cd devtrack
docker-compose up --build
```
Then go to http://localhost:8000

## Running Locally
```bash
git clone https://github.com/yourusername/devtrack.git
cd devtrack
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then go to http://127.0.0.1:8000

## Project Structure
```bash
DevTracker/
│
├── DevTracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── website/
│   ├── migrations/
│   ├── templates/
│   │   ├── account/
│   │   │   └── dashboard.html
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── logged_out.html
│   │   │   └── signup.html
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── milestones.html
│   │   └── track.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

## Planned Features
- PostgreSQL migration
- Django REST Framework API endpoints
- Progress charts
- Dark mode
- Problem tags
- Search and filters
- User profile page

## Licence
MIT Licence

Built by Subhaan