## CollegeProject

A project that involves developing a feedback website for college. The project digitalize the feedbacks given by the students for their teachers. There are few drawbacks in traditional system like

- The teachers are able to find out the identity of students who has given them feedback. Hence, leads to unfair consequences.
- The evaluation score has to be fed into the database manually which takes a lot of time and require manpower.
- At times, it is difficult to understand the handwriting of some students, which leads to an ambiguity in suggestions given by such students.

The project tackles all these problems efficiently and focuses on building a fair feedback system.

The website is build up using Django framework with `Python 3.6.5` and `Django 2.0.7`
***
## Pre-requisite

Before running the project, you need to create a virtual environment so that it doesn't affect your other projects under development.

To create a  virutal environment follow these steps:

    $ cd ~
    $ pip install pipenv
    $ git clone https://github.com/GeekyFreelancers/CollegeProject
    $ cd CollegeProject
    $ pipenv install python==3.6.5
    $ pipenv shell

This will create and activate a virtual environment with Python version as specified. Now you need to install the `Django 2.0.7`(current version)

    $ pip install django==2.0.7
***
## Run the Project

First you need to populate the database as:

    $ python manage.py migrate

Then you need to run the server as:

    $ python manage.py runserver

Make sure you are in the CollegeProject directory. Go to the localhost and the project would work.
***

## References

- To know more about Django, refer https://www.djangoproject.com/
- To know more about Python, refer https://www.python.org/doc/