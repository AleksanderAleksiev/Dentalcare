# Dentalcare

 Web application assisting dental heath

 Actually, this is only the server side of the application which handles the API requests and storing the data in a database. It can be paired with various UI applications, but I have chosen React. Here is the link for the other repository.

# What is Dentalcare?

Dentalcare is a web application that assists both dentists and their clients in their everyday tasks, making it easier for them to set up dentist's appointments around every other chore of their own.

Being a dentist is quite stressful, as I know from my aunt. Not only she has to make appoinments with her patients, but sometimes she has to take time to order some moldings from other specialists, or some medicines and machine parts from long-distance providers.

As for the normal people, we all know that no one enjoys a dentist visit, but it is essential for our dental health so we should do it regularly and also plan it beforehand, as it might take several hours of our day.

# Who can use Dentalcare?

As it might already be clear, this web application can be used both by dentists and their clients. Upon registration a user can select its role and based on it, there will be different permissions. The main feature is scheduling tasks and appointments.

# Technologies Used

For this part of the application I have used the well known **Django** web framework for **Python** which also have integrated **SQLite** database.

# Starting The Project

The first requirement is having [**Python**](https://www.python.org/) version 3 or above installed on your machine. You should also have a package manager like [pip](https://pypi.org/project/pip/).

In order to start the project you must be inside the root directory of the project, if you are not sure this is the one with the ```manage.py``` file in it.
I would recommend using a virtual environment for the project, as this is an isolated environment , which allows you to have project-specific dependencies and packages in it, separate from the system’s Python environment and other projects. This ensures that the project’s dependencies are controlled and not affected by other packages or updates in the system.

Run this command inside the root directory to create your virtual environment(venv):

```
python -m venv venv_name
```
where ```venv_name``` will be the name of the environment.

Activate the venv by typing:
```
venv_name\scripts\activate
```
(this is for Windows only)

Once you are in the virtual environment run the next command, in order to install all the required packages and dependencies:
```
pip install -r requirements.txt
```

After these steps you are good to go. Type in 
```
python manage.py runserver
```
Now ther server is up and running on ```http://127.0.0.1:8000/``` and you can access it from any frontend application.

