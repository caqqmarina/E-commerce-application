Assignment 1:

Explain how you implemented the checklist above step-by-step (not just following the tutorial).

1. create a new django project (using django-admin startproject ecommerce)
2. create an application with the name shop in the project (using python manage.py startproject shop)
3. perform routing in the project so that the application
4. create a model in the application shop with the name Product (inside it are the name price description and i also added a custom model named slime quality)
5. create a function in views.py to return to an HTML template that displays the name of the application and my class and name
6. create routing in urls.py for the application main to map the function created in views.py
7. perform deployment to PWS for the application that has been created so that it can be accessed by others
8. create readme file

Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

diagram (bismillah)
https://drive.google.com/drive/folders/1f0XB4-UiS6rTEVDKlGMpc5juFq0RFWp6?usp=drive_link

1. Client Request:
The client (user) sends a request to a Django application via a web browser, typically an HTTP GET or POST request.

2. urls.py (URL Dispatcher):
This file defines the routes (URLs) for your Django application. When the request comes in, Django looks at urls.py to find which view should handle the request. Each URL pattern is associated with a view function.

3. views.py (Request Handler):
The view function defined in views.py receives the request. It can retrieve data from models, process the request, and prepare the response. Depending on the logic, the view function interacts with models.py to fetch or manipulate data.

4. models.py (Database Interaction):
If the view requires data from a database, it communicates with the models defined in models.py. The model represents the structure of your database and the logic to retrieve or manipulate data.

5. HTML Template (Rendering the Response):
Once the view has the necessary data, it passes this data to an HTML template (located in the templates directory).
The template generates the HTML response, which is returned to the client.

6. Client Response:
The generated HTML is sent back to the client as the HTTP response.

Explain the use of git in software development!

Git is a crucial tool in software development for managing and tracking code changes. It allows multiple developers to collaborate seamlessly, helping to prevent conflicts when working on the same project. Git also provides a history of modifications, so developers can review past changes and easily revert to previous versions if needed. Overall, it helps maintain organization and control in complex projects.

In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

Django is often chosen for beginners because it’s a comprehensive, all-in-one framework. It simplifies web development by providing tools for handling databases, security, and templates out of the box. This allows learners to focus on building features without worrying about the underlying infrastructure. Its clear structure encourages good coding practices, making it an ideal starting point for learning web development.

Why is the Django model called an ORM?

Django’s model is called an ORM (Object-Relational Mapping) because it automatically translates Python code into database queries. Instead of writing complex SQL, developers can interact with the database using simple Python objects. This abstraction makes database management easier and more intuitive, allowing developers to focus on the logic rather than the details of database queries.

Assignment 2:

1. Explain why we need data delivery in implementing a platform.

Data delivery is crucial because it allows platforms to exchange information between servers and clients or between multiple systems. Without data delivery, user interaction (such as submitting forms or retrieving information) would not be possible. Platforms need to support efficient data delivery to ensure seamless interaction, enable services such as APIs, and facilitate scalability.

2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

JSON is generally more lightweight and easier to read and write compared to XML, its easier on the eyes. Meanwhile, XML can be hard to read and very verbose, it also requires more parsing. Additionally for JSON it integrates well for API's and Javascript, making it more popular than XML.


3. Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.

The is_valid() method checks if the information someone entered into a form is correct and follows the rules you've set (like making sure a field isn't empty or that an email address is properly formatted). If everything looks good, it returns True; otherwise, it returns False. This is important because you don't want to save incomplete or incorrect data to your database.

4. Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?

The csrf_token protects your forms from Cross-Site Request Forgery (CSRF) attacks, where a user is tricked into unknowingly submitting a form on your site. Without it, an attacker could create fake forms that submit requests using a logged-in user's credentials, like changing their password or making purchases.

5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

- Created a form for adding Product objects using django’s ModelForm.
- Built views to handle different data formats (XML and JSON) for all products and by specific IDs.
- Implemented URL routing for pws to connect views with the web application’s interface.
- Structured the form with CSRF protection to avoid vulnerabilities.
- Ensured validation using the is_valid() method to prevent invalid data from being submitted.
