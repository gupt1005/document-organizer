# Document Organizer

A Django-based web application for organizing and managing digital documents. The project demonstrates full-stack web development using Python and Django, with a focus on backend architecture, database management, and a clean web interface.

## Features

* Organize and manage digital documents
* Store document information using a relational database
* Create, view, update, and delete document records
* Dynamic web pages using Django templates
* Backend routing and request handling with Django
* Persistent data storage using SQLite

## Technologies

* **Python** — Backend programming
* **Django** — Web application framework
* **SQLite** — Database
* **HTML/CSS** — Frontend
* **Git** — Version control

## Project Structure

```text
Document_Organizer/
│
├── myproject/
│   ├── manage.py
│   │
│   ├── myproject/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── <app_name>/
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
│
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Document_Organizer
```

### 2. Create a virtual environment

Create a Python virtual environment for the project:

```bash
python3 -m venv chore_scheduler_env
```

### 3. Activate the virtual environment

On macOS/Linux:

```bash
source chore_scheduler_env/bin/activate
```

On Windows:

```bash
chore_scheduler_env\Scripts\activate
```

Once activated, your terminal should show the environment name:

```text
(chore_scheduler_env)
```

### 4. Install dependencies

If a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

Otherwise, install Django directly:

```bash
pip install django
```

### 5. Run database migrations

From the directory containing `manage.py`:

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Press `Control + C` to stop the development server.

## Django Commands

Some useful commands for development:

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Create an administrator account

```bash
python manage.py createsuperuser
```

### Run tests

```bash
python manage.py test
```

## Development Environment

The project uses a Python virtual environment to isolate its dependencies from the system Python installation. This allows the project to maintain its own Python packages and versions without affecting other projects on the computer.

## Future Improvements

Potential future additions include:

* User authentication and accounts
* Document search and filtering
* Document categories and tags
* Improved document upload functionality
* File previews
* More advanced document metadata management
* Additional automated tests
* Improved frontend styling and responsiveness

## Purpose

This project was developed to gain practical experience building a full-stack web application and to strengthen my understanding of backend development, databases, web frameworks, and software engineering practices.
