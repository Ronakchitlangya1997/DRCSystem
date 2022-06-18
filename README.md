# Django Project Template

The clean, fast and right way to start a new Django `1.10.1` powered website.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

    $ virtualenv project-env
    $ source project-env/bin/activate

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/Ronakchitlangya1997/DRCSystem.git
    $ cd DRCSystem
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver