# Tasks
Tasks helps you registering and managing your to-do list with just a few clicks.
Showing which task is currently pending or completed.


<img width="1897" height="856" alt="image" src="https://github.com/user-attachments/assets/565406ad-76d0-4abb-958a-4b091f7ee019" />



# Features
Tasks allows you to create, edit and delete tasks at any moment, helping you managing all your dayly-basis activities 

# Technology
Python,
HTML
and Django Framework.

# How to use/run

If you want to use Tasks access the link below: 

https://tasks-a345.onrender.com/

Then, click on "Don't have an account? Click here." and fill out the form to get your account created.
-- You don't need to use a real email address to have access to it. --

But, if you want to run Tasks locally follow the steps below.
(You need Python already installed in your system.)

1. Download this repo to your computer and open the folder using some editor as VSCode or PyCharm.
2. In the terminal, run the command 'pip install -r requirements.txt'. This action will install all tools needed.
3. Go to 'tasks_project' folder, find the file 'settings.py' and look for the section 'DATABASES'. Replace all section with the code below

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

4. In terminal run 'python -m makemigrations', and then 'python -m migrate'. This two lines will create a db.sqlite3 file locally.
5. Run the command 'python ./manage.py runserver'.
6. In your favorite browser type the address 'http://127.0.0.1:8000'
-- Tasks login page will be showed for you. --
