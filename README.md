# Project Matatu

This is a web application built using Django for managing matatu (public transport) bookings. The app allows users to view available bookings, manage their dashboard, and interact with matatu services.

## Features

- **Dashboard**: View an overview of your bookings and matatu status.
- **Bookings**: Make and manage bookings for matatus.
- **Index Page**: A simple homepage to navigate through the app.

## Setup Instructions

Follow the steps below to set up and run the app locally.

### Prerequisites

Before you begin, ensure that you have the following installed on your system:

- Python 3.12 or higher
- Virtual environment tool (`venv`)
- Git (for version control)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/project-matatu.git
cd project-matatu
```

### 2. Set up a virtual environment

Create a virtual environment using `venv`:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On macOS/Linux**:

```bash
source venv/bin/activate
```

- **On Windows**:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application

Once all dependencies are installed, run the Django development server:

```bash
python manage.py runserver
```

This will start the server on `http://localhost:8000`.

### 5. Access the app

Open your browser and go to `http://localhost:8000` to interact with the application.

## Django Admin

You can also access the Django admin dashboard by going to `http://localhost:8000/admin/`. Use the superuser credentials to log in.

### 6. Create a superuser

To create a superuser (admin), run the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password for the superuser.

### 7. Database

The app uses an SQLite database by default. The database will be automatically created when you run the server.

To apply any database migrations, run:

```bash
python manage.py migrate
```

## Running Tests

To run the app's tests, use the following command:

```bash
python manage.py test
```

## Contributing

Feel free to fork this project and submit pull requests. Please make sure to follow the existing code structure and guidelines.
