# Matatu Owner Business Management System

## Overview

The Matatu Owner Business Management System is a comprehensive software solution designed to streamline and optimize the operations of matatu businesses. It facilitates efficient fleet management, including scheduling, route planning, and vehicle maintenance tracking. The system also supports financial management with automated fare collection, expense tracking, and revenue reporting, along with driver management and customer service features.

## Features

- **Fleet Management**: Schedule management, route planning, vehicle maintenance tracking.
- **Financial Management**: Automated fare collection, expense tracking, revenue reporting.
- **Driver Management**: Performance monitoring, shift assignment, compliance tracking.
- **Customer Service**: Passenger feedback management, service quality assurance.

## Installation

### Prerequisites

- Python 3.12+
- Django 5.1.7
- Virtual Environment (recommended)

### Setup

1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd Project-matatu
   ```
2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Run the Server**
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the system at `http://localhost:8000/`
- Login or register as needed
- Use the dashboard to manage matatu operations

## Project Structure

```
Project-matatu/
│── matatu/        # Django project folder
│   ├── core/      # Main application
│   ├── templates/ # HTML templates
│   ├── static/    # Static files (CSS, JS, images)
│   ├── manage.py  # Django management script
│── requirements.txt  # Project dependencies
│── README.md      # Documentation
│── .gitignore     # Git ignore rules
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a Pull Request
