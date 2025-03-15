import os
import subprocess
import sys
import shutil
import time

# Function to check if we are in a virtual environment
def check_venv():
    # Check if Python is installed
    python_executable = shutil.which("python") or shutil.which("python3")
    if not python_executable:
        print("Error: Python is not installed or not found in the system PATH.")
        sys.exit(1)

    # Check if the current Python executable is in a virtual environment
    if sys.prefix == sys.base_prefix:
        print("Not in a virtual environment. Creating one...")
        try:
            # Create a virtual environment
            subprocess.check_call([python_executable, "-m", "venv", "venv"])
            # Determine the activation script based on the platform
            activate_script = "venv/bin/activate" if sys.platform != "win32" else "venv\\Scripts\\activate"
            print(f"Virtual environment created. Run 'source {activate_script}' to activate it and rerun the script.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            sys.exit(1)
        sys.exit(1)
    else:
        print("Already in a virtual environment.")


# Function to install dependencies and generate requirements.txt
def install_dependencies():
    print("Installing Django and Django Unfold...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "django", "django-unfold"])
    pip_freeze_req = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode('utf-8')
    print (pip_freeze_req)
    with open("requirements.txt", "w") as file:
        file.write(f"{pip_freeze_req}")

# Function to create Django project and app
def create_project_and_app():
    project_name = input("\nEnter the Django project name: ")
    app_name = input("Enter the name of the first app: ")

    print(f"Creating Django project: {project_name}...")
    subprocess.check_call([sys.executable, "-m", "django", "startproject", project_name])

    print(f"Creating Django app: {app_name}...")
    os.chdir(project_name)
    subprocess.check_call([sys.executable, "manage.py", "startapp", app_name])

    # Add the app to INSTALLED_APPS in settings.py
    settings_path = os.path.join(project_name, 'settings.py')

    print(f"Looking for settings.py at: {settings_path}")
    
    # Check if settings.py exists
    if not os.path.exists(settings_path):
        raise FileNotFoundError(f"Could not find settings.py at {settings_path}. Please check the project structure.")

    with open(settings_path, 'r') as file:
        lines = file.readlines()

    # Find the line where INSTALLED_APPS ends
    for i, line in enumerate(lines):
        if 'INSTALLED_APPS' in line:
            # Look for the closing bracket of INSTALLED_APPS
            while ']' not in lines[i]:
                i += 1
            # Insert the new app before the closing bracket
            lines.insert(i, f"    '{app_name}',\n")
            break

    # Write the updated content back to settings.py
    with open(settings_path, 'w') as file:
        file.writelines(lines)

    print(f"Added '{app_name}' to INSTALLED_APPS in settings.py.")

 # Create models.py content
    models_content = """
from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    """

    # Write models.py
    models_path = os.path.join(app_name, 'models.py')
    with open(models_path, 'w') as file:
        file.write(models_content)

    print(f"Created models.py in {app_name}.")

    # Create admin.py content
    admin_content = """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import TestModel

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


@admin.register(TestModel)
class TestModelAdmin(ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
    """

    # Write admin.py
    admin_path = os.path.join(app_name, 'admin.py')
    with open(admin_path, 'w') as file:
        file.write(admin_content)

    print(f"Created admin.py in {app_name}.")

    # Configure Django Unfold as the first item in INSTALLED_APPS
    print("Configuring Django Unfold...")
    settings_path = os.path.join(project_name, "settings.py")
    with open(settings_path, "r") as file:
        lines = file.readlines()
    with open(settings_path, "w") as file:
        for line in lines:
            if line.startswith("INSTALLED_APPS = ["):
                file.write("INSTALLED_APPS = [\n    'unfold',\n")
            else:
                file.write(line)

    # Add Unfold settings
    with open(settings_path, "a") as file:
        file.write("\n\n# Django Unfold Settings\n")
        file.write("UNFOLD = {\n")
        file.write(f"    'SITE_HEADER': '{project_name} Dashboard',\n")
        file.write(f"    'SITE_TITLE': '{project_name} Dashboard',\n")
        file.write("    'SITE_ICON': None,\n")
        file.write("}\n")

    # Create templates folder and index.html
    print("Creating templates folder and index.html...")
    templates_path = os.path.join(app_name, "templates", app_name)
    os.makedirs(templates_path, exist_ok=True)
    index_html_path = os.path.join(templates_path, "index.html")
    index_html_content = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Setup Complete!</title>
</head>
<body>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap');

    *{
        margin: 0;
        padding: 0;
    }
    body{
        font-family: "Work Sans";
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #19865C;
    }
    nav{
        width: 99vw;
        display: flex;
        flex-direction: row-reverse;
        padding: 20px;
        background-color: #6DDCBD;
        margin-bottom: 20px;
    }
    nav li a{
        padding: 10px 30px;
        color: #19865C;
        text-decoration: none;
        background-color: #FFFFFF;
        border-radius: 10px;
        font-weight: bold;
    }
    nav li a:hover{
        color: #FFFFFF;
        background-color: #6DDCBD;
        border: 1px solid #FFFFFF;
        transition: .3s;
    }
    h1{
        font-weight: bold;
        font-size: 40px;
        text-align: center;
    }
    li{
        list-style: none;
        font-size: 20px;
    }

    </style>
    <nav>
        <li><a href="/admin">Admin</a></li>
    </nav>
    <h1>Custom Setup complete!</h1>
    <ul>
        <li>✓✓ App configured</li>
        <li>✓✓ App basics created</li>
        <li>✓✓ App defaults updated</li>
        <li>✓✓ Admin superuser created</li>
        <li>✓✓ Admin page styled and updated</li>
    </ul>
</body>
</html>

"""

    with open(index_html_path, "w") as file:
        file.write(index_html_content)
        # file.write("<html lang='en'>\n")
        # file.write("<head>\n")
        # file.write("    <meta charset='UTF-8'>\n")
        # file.write("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        # file.write("    <title>Index Page</title>\n")
        # file.write("</head>\n")
        # file.write("<body>\n")
        # file.write("    <h1>Default Index Page by Conto</h1>\n")
        # file.write("</body>\n")
        # file.write("</html>\n")

    # Update views.py to render the index.html template
    print("Updating views.py to render the index.html template...")
    app_views_path = os.path.join(app_name, "views.py")
    with open(app_views_path, "w") as file:
        file.write("from django.shortcuts import render\n\n")
        file.write("def index(request):\n")
        file.write(f"    return render(request, '{app_name}/index.html')\n")

    # Create urls.py in the app with a default path to index view
    print("Creating urls.py in the app...")
    app_urls_path = os.path.join(app_name, "urls.py")
    with open(app_urls_path, "w") as file:
        file.write("from django.urls import path\n")
        file.write("from . import views\n\n")
        file.write("urlpatterns = [\n")
        file.write("    path('', views.index, name='index'),\n")
        file.write("]\n")

    # Include the app's urls.py in the project's urls.py
    print("Including app's urls in the project...")
    project_urls_path = os.path.join(project_name, "urls.py")
    with open(project_urls_path, "r") as file:
        lines = file.readlines()
    with open(project_urls_path, "w") as file:
        for line in lines:
            if line.startswith("from django.urls import path"):
                file.write("from django.urls import path, include\n")
            elif line.startswith("urlpatterns = ["):
                file.write(line)
                # file.write(f"    path('admin/', admin.site.urls),\n")  # Ensure admin URLs are included
                file.write(f"    path('', include('{app_name}.urls')),\n")
            else:
                file.write(line)

    os.chdir("..")

# Function to create superuser
def create_superuser(project_name):
    create_superuser_choice = input("Do you want to create a superuser? (yes/no): ").lower()
    if create_superuser_choice == "yes" or "y":
        print("Making migrations...")
        os.chdir(project_name)
        
        # Run makemigrations
        subprocess.check_call([sys.executable, "manage.py", "makemigrations"])
        
        # Run migrate
        print("Applying migrations...")
        subprocess.check_call([sys.executable, "manage.py", "migrate"])
        
        # Create superuser
        print("Creating superuser...")
        subprocess.check_call([sys.executable, "manage.py", "createsuperuser"], stdin=sys.stdin)
        
        # Return to the parent directory
        os.chdir("..")
    else:
        print("Great,")
        time.sleep(1)
        print("Great, exiting now...")
        time.sleep(2)


# Main function
def main():
    check_venv()
    install_dependencies()
    create_project_and_app()
    project_name = input("Enter the Django project name again (for superuser creation): ")
    create_superuser(project_name)
    print("Django project setup is complete!")

if __name__ == "__main__":
    main()