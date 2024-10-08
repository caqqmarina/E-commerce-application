# Assignment 2

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

# Assignment 3

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

Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
https://drive.google.com/drive/folders/1XM6ZVE7FzbINOaqk8aYaWosNkBmm2B6A?usp=sharing

# Assignment 4 

 1. What is the difference between HttpResponseRedirect() and redirect()?

 HttpResponseRedirect(): a low-level method that simply returns an HTTP 302 redirect to a specific URL
 redirect(): a high-level Django utility that automatically handles various types of inputs. It can take a view name, a URL path, or even an object and resolve it to the appropriate URL.

 2. Explain how the MoodEntry model is linked with User!
 MoodEntry can be linked with the ForeignKey relationship, which means that the MoodEntry model has a field user which is a foreign key to the User model. Each user can have multiple mood entries, but each MoodEntry is linked to exactly one User.

 3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these   two concepts.

 Authentication:
 This is the process of verifying a user's identity (i.e., checking if the user is who they claim to be). In Django, authentication happens when a user provides valid credentials (such as a username and password) via the login form. Django checks the credentials against the database, and if they are valid, the user is authenticated.

 Authorization:

 This is the process of determining if a user has permission to access a resource or perform an action (e.g., accessing a specific view, editing data). In Django, after a user is authenticated, the system checks whether the user has the necessary permissions to perform an action.

 5. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

 Django uses sessions to remember logged-in users. When a user logs in, Django creates a session on the server side and assigns it a unique session ID. This session ID is stored in a cookie on the user’s browser. On each subsequent request, the user’s browser sends this session cookie back to the server. Django retrieves the session data based on the session ID stored in the cookie, which includes information like the user’s ID.

 Other uses of cookies:

 Storing preferences: Cookies can be used to store user preferences (e.g., language settings, theme selection).
 Tracking: Cookies can be used for tracking user behavior, such as the items viewed in an e-commerce store.
 Shopping cart: Cookies can be used to maintain a shopping cart for users who haven’t logged in.

 Are all cookies safe to use?

 Not all cookies are safe: Some cookies, especially third-party tracking cookies, can be used to collect user data without their consent, raising privacy concerns.

 6. Explain how did you implement the checklist step-by-step (apart from following the tutorial).

1. Implemented user authentication using Django’s UserCreationForm for registration and AuthenticationForm for login.

2. Customized the login_user view to handle form submissions and log users in upon successful authentication.

3. Added necessary URL paths to urls.py.

4. Created the Product model with fields like name, price, description, and slime_quality.

5. Linked the Product to the User model using a ForeignKey, ensuring each product is associated with a specific user.

6. Developed a view to display products for the logged-in user only.

7. Created a view for adding new product entries, ensuring the logged-in user is automatically associated with the product.

8. Customized main.html to display user-specific products by filtering based on request.user.

9. Added templates for login, registration, and product creation.

10. Performed migrations using makemigrations and migrate to update the database schema.

11. Created two test user accounts and added three products for each to verify that users only see their own data.

# Assignment 5

# Questions

 A. CSS Selector Priority Order
The priority of CSS selectors is determined by specificity. The order is:
1. Inline styles (highest priority)
2. IDs (`#id`)
3. Classes, attributes, and pseudo-classes (`.class`, `:hover`)
4. Element selectors (`div`, `h1`, etc.)
5. Universal selector (`*`) (lowest priority)

The more specific a selector is, the higher its priority.

 B. Importance of Responsive Design
Responsive design is crucial because it ensures a seamless user experience across various devices. For example:
- Applications with responsive design: Twitter, Amazon
- Applications without responsive design: Older versions of eBay, many static websites

These applications may appear broken or difficult to navigate on different screen sizes.

 C. Differences Between Margin, Border, and Padding
- Margin: Space outside an element, creating distance from other elements. Implemented using `margin` property.
- Border: A line surrounding the element. Defined with the `border` property, specifying width, style, and color.
- Padding: Space inside the element, between the content and the border. Adjusted using the `padding` property.

Example:

```css

.box {
  margin: 20px; 
  border: 2px solid black; 
  padding: 10px;
}
```

 D. Concepts of Flexbox and Grid Layout
- Flexbox: A one-dimensional layout model that arranges items along a single axis (row or column). Ideal for aligning items within a container.
  - Example: Centering elements within a navbar.

- Grid Layout: A two-dimensional layout system allowing items to be arranged into rows and columns. Useful for creating complex layouts.
  - Example: Designing a product card layout.

 E. Step-by-Step Implementation of the Checklist
1. Functions for Product Management: Added additional code in views.py and html formattings for product deletion and editing.
2. Design Customization: Leveraged Tailwind CSS to enhance the aesthetics of the login, register, and product pages.
3. Product List: Implemented conditional rendering for empty states and styled product cards for fun look
4. Navbar: Implemented a Navbar (which isnt being used much right now) for future functionality

# Assignment 6

# Questions

 A. Explain the benefits of using JavaScript in developing web applications!

JavaScript allows us to make web pages dynamic and interactive without needing to reload the entire page. It improves user experience by handling tasks like real-time updates, form validation, or interactive elements directly in the browser. This makes apps faster, reduces server load, and keeps the user engaged with instant feedback.

 B. Explain why we need to use await when we call fetch()! What would happen if we don't use await?

When we use fetch(), it returns a promise that may take some time to resolve. By using await, we pause the code execution until the data is fetched, which ensures that we handle the data correctly before moving on. Without await, the code might try to use the fetched data before it’s ready, which could result in errors or undefined values.

 C. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

Django has built-in CSRF protection to prevent malicious form submissions. AJAX requests also need to pass the CSRF token, but it can sometimes complicate things. csrf_exempt allows you to bypass CSRF protection on certain views to simplify AJAX POST requests. 

 D. On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

Front-end sanitization can easily be bypassed because users can manipulate the browser or send requests manually. That’s why back-end sanitization is critical—it ensures that no harmful data makes its way into the server or database, even if the front-end controls are tampered with.

 E. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

1. AJAX GET: Modified data card to fetch entries belonging to the logged-in user using fetch(). Updated the UI without reloading.

2. AJAX POST: Created a button to trigger a modal for mood entry. Inside the modal, there's a form. After submission, the modal closes and the page refreshes asynchronously if successful, or shows an error message otherwise.

3. New View Function: Created a view function to handle the mood entry submission using AJAX POST, which adds data to the database securely.

4. /create-ajax/ Path: Set up the URL routing to the new view function. Connected the modal form to this route.
Asynchronous Refresh: Added a function to refresh the mood list dynamically after successful form submission without reloading the main page.


