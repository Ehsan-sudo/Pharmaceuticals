# Pharmaceuticals
A python django web app for pharmaceutical business in Afghanistan


# Requirements:
`sudo apt install python3`  
`sudo apt install python3-pip`  
`sudo pip install django`  
`sudo apt install mysql-server`  
`sudo apt install mysqlclient`  
`sudo apt install libmysqlclient-dev`


# Configurations:
After you have installed all the requirements, it's time to run the project. To do this, follow the steps below:  
  
### Database configuration:
create a database called **pharma** in your mysql server. then set the database configurations in the **/Pharmacueticals/pharmaceuticals/pharmaceuticals/settings.py** as below: 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pharma',
        'USER': 'ehsan',
        'PASSWORD': 'ehsan123'
    }
}
```
where pharma, ehsan, ehsan123 are the name of the database, username for my mysql server, and password for the user respectively.

### Creating tables inside database
After configuring the **settings.py** file, migrate all the database migrations by running the below command inside terminal while you are in the **/Pharmacueticals/pharmaceuticals/** directory:  
$`python3 manage.py migrate`  
  
this will create all the tables and relationships in your mysql server.

# Running the web application:  
after the configurations are done, now you can run the django development server using the command below. you need to be at the at **/Pharmacueticals/pharmaceuticals/** directory:  
$`python3 manage.py runserver`

after the server has started successfully, you can open any browser in your computer and go to **127.0.0.1:8000/register**.

:)
