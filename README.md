# Mathree System

Mathree System is a Django-based web application designed to manage Matatu Owner Businesses. The system allows matatu owners to manage their fleets, schedule routes, track vehicle maintenance, handle financial management, manage drivers, and improve customer service. It includes functionalities for both admins (owners) and users (drivers/touts), allowing them to interact with their respective dashboards.

## Features

- **Fleet Management**: Manage vehicle data, including registration, maintenance tracking, and vehicle health.
- **Scheduling**: Create and manage schedules for vehicles, assign drivers and touts, and handle route planning.
- **Financial Management**: Automate fare collection, track expenses, and generate revenue reports.
- **Driver Management**: Monitor driver performance, assign shifts, and ensure compliance with regulations.
- **Customer Service**: Gather passenger feedback and improve service quality.
- **Admin Dashboard**: Admin users (owners) have full control over the system, including the ability to view, edit, and manage all aspects of the business.

## Technologies Used

- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **Authentication**: Django's built-in authentication system
- **Deployment**: N/A (still under development)

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/Kennedy-pentester/Project-matatu.git
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations to set up the database

```bash
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser. This user will have access to the Django admin panel.

### 6. Run the server

```bash
python manage.py runserver
```

Now, you can visit the application at `http://127.0.0.1:8000/` in your browser.

## Project Setup Details

- **Database**: This project uses SQLite3 for local development. The main database file is `db.sqlite3`
- **User Roles**:
  - **Admin (Owner)**: Has full access to all sections, including fleet, scheduling, financials, and user management.
  - **Driver**: Can view assigned vehicles and schedules.
  - **Tout**: Can manage customer-related tasks and feedback.

## Usage

1. **Login**:

   - admins can login to the system using their credentials and will be directed to `Django admin` page
   - Drivers and touts will also be directed to respective pages too
   - Owners will be directed to `admin_dashboard` page (different with admins) where they can see activities

2. **Logout**: Users can log out from any page, and they will be redirected to the login page.
