# Dev Tracker - Personal Developer Progress Tracker

A full-stack Django web application that helps developers track their learning, coding challenges, and daily progress across platforms like AlgoMap, LeetCode, and general programming study sessions.

## READ HERE
I started this project beacuse I wanted to get be able to see my progress all on one website while also get better at making full-stack applications. I didn't want it to be something that I won't use as soon as I make it, like a blog app for example. It doesn't interest me to spend so much time on developing to not even use it. I **will** be using this applicaiton when I finish it (you can too), and it is easily scalable so in the future I can add more skills and practice techniques as I keep getting better at software developing. This has really helped with speeding up the learning process of making real world applications and also practicing simple logic in Leetcode at the same time.

## Overview
**DevTracker** is a productivity and learning companion for developers.
It allows you to:
- Track AlgoMap / LeetCode problems you’ve completed
- Rate their difficulty
- Store notes and reflections
- Log daily learning sessions
- Document milestones (like new Django concepts learned)
- View your overall progress in a dashboard

This project demonstrates real-world Django developer skills:
- Models, Views and Templates
- User authentication
- CRUD operations
- Django Admin customisation
- Clean project architecture
- Optional REST API (Django REST Framework)
- Deployment on Render/Railway

## Features

### User Accounts
- Login, Register and Logout
- Secure authentication using Django's built in User model

### Problem Tracker
- Add problems you've solved (Algomap, LeetCode, Custom)
- Custom difficulty rating (Easy, Medium, Hard)
- Notes for explinations or thoughts
- Automatic date tracking
- List + Detail views
- Edit + Delete options

### Learning Milestones
Track progress as you learn:

- Django concepts
- Python techniques
- CS fundamentals
- Anything related to your dev journey

### Daily Sessions
- Log daily learning time
- Add notes for what your studied
- Track consistency and streaks

### Dashboard
- Total problem solved
- Difficulty distribution
- Daily study streak
- Recently completed milestones

### Tech Stack
- Python3
- Django
- SQLite/PostgreSQL
- HTML/CSS (Django Templates)
- Bootstrap and TailwindCSS 
- Django REST Framwork
- Render/Railway for deployment

### Project Structure
```bash
devtracker/
│
├── DevTracker/       
│   ├── __init__.py      
│   ├── asgi.py      
│   ├── settings.py        
│   ├── urls.py    
│   └── wsgi.py   
│
├── website/    
│   ├── migrations/
│       ├── 0001_initial.py
│       ├── 0002_initial.py
│       └── __init__.py
│   ├── templates/
│       ├── base.html   
│       ├── dashboard.html
│       ├── index.html
│       ├── login.html
│       ├── milestones.html
│       └── track.html
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
├── .gitignore
├── manage.py
└── README.md
```

### Getting Started
- Clone to Repo
```bash
git clone https://github.com/yourusername/dev-tracker.git
cd dev-tracker
```
- Create a virtual environment
```bash
pyhton -m venv venv
source venv/bin/activate # Mac/Linux
venv/Scripts/activate    # Windows
```
- Run the server
```bash
python manage.py runserver
```

### Planned Features
- REST API endpoint
- Progress charts
- Dark mode
- Problem tages
- Search + Filters
- User profile page

## Licence
MIT Licence

Built by Subhaan