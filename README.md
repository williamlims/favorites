# favorites
Functionality of Favorite Products for Customers. Applications will be able to send HTTP requests to manage customers and their favorite products.

# Requirements
* Python 
* Git
* Postgres (with database name "favorites" created and running)

# Steps for installation
1. After Git Clone, run the file start.sh
2. Execute the command "source env/bin/activate"
3. Adjust the database connection settings in /favorites/settings.py, in the DATABASES item
4. Execute the commands: "python manage.py makemigrations" and then "python manage.py migrate"
5. Execute the command "python manage.py createsuperuser" and set up a USER for tests
6. Run: "python manage.py runserver"

# Functionality
Django REST framework offers an interface to test the API
* To view customer data, it is possible by accessing: http://127.0.0.1:8000/api/customers/
* To view the data for a specific customer, it is possible by accessing: http://127.0.0.1:8000/api/customers/<id>/

* It is possible to view customer data, but to update (PUT), create (POST) and remove (DELETE), authentication and authorization are required.

* For authentication, access: http://127.0.0.1:8000/api-auth/login/

* To see the list of products, access: http://127.0.0.1:8000/api/favorites/
* To see a specific product, access: http://127.0.0.1:8000/api/favorites/<id>/

* Favorite products are not saved if the corresponding product id does not exist.
