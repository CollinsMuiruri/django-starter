# 🚀 Django Project Setup Script

This Python script automates the setup of a Django project, including the creation of a virtual environment, installation of dependencies, and configuration of a Django app with Django Unfold for a stylish admin interface. Below is a detailed explanation of what the script does:

## 📋 Table of Contents
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Usage](#-usage)
- [Dependencies](#-dependencies)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Features

- **Virtual Environment Setup**: Automatically checks if a virtual environment is active and creates one if not.
- **Dependency Installation**: Installs Django and Django Unfold, and generates a `requirements.txt` file.
- **Project and App Creation**: Creates a Django project and app, and configures the app in the project's `settings.py`.
- **Admin Interface Styling**: Configures Django Unfold for a modern admin interface.
- **Superuser Creation**: Optionally creates a superuser for the Django admin.
- **Templates and Views**: Sets up a basic template and view for the app.

## 🛠 How It Works

### 1. **Virtual Environment Check**
   - The script checks if a virtual environment is active.
   - If not, it creates a new virtual environment named `venv`.

### 2. **Dependency Installation**
   - Installs Django and Django Unfold using `pip`.
   - Generates a `requirements.txt` file with the installed dependencies.

### 3. **Project and App Creation**
   - Prompts the user for a project name and app name.
   - Creates the Django project and app.
   - Adds the app to `INSTALLED_APPS` in `settings.py`.

### 4. **Admin Interface Styling**
   - Configures Django Unfold as the first item in `INSTALLED_APPS`.
   - Adds Unfold settings to `settings.py`.

### 5. **Templates and Views**
   - Creates a `templates` folder and an `index.html` file.
   - Updates `views.py` to render the `index.html` template.
   - Configures URL routing for the app.

### 6. **Superuser Creation**
   - Optionally creates a superuser for the Django admin interface.

## 🚀 Usage

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:CollinsMuiruri/django-starter.git
   cd django-setup-script
   ```

2. **Run the Script**:
    ```bash
    python setup_django.py
    ```

3. **Follow the Prompts**:
    - Activate the Virtual Environment:

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    
    - Enter the project name and app name when prompted.

    - Choose whether to create a superuser.

4. **Run the Django Development Server**:
    ```bash
    cd your_project_name
    python manage.py runserver
    ```

5.  **Access the Admin Interface**:
Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.

## 📦 Dependencies
Python 3.x

Django

Django Unfold

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.