# TASK 1: UNDERSTANDING THE DJANGO REQUEST-RESPONSE CYCLE

"""
1. GET /api/courses/ Request

- URL Router: Django matches the string '/api/courses/' to a specific view function.
- Middleware: Intercepts the request before it hits the view.
- View: Contains the business logic. It queries the Model to get the course list.
- Model: Converts Python commands to a SQL query, pulls the data from the DB, and returns Python objects to the View.
- Template: The view injects the objects into a template and sends a HTTP response back to the client.

"""

"""
2. The Middleware

Where is it: 
Middleware is a framework of hooks into Django's request/response cycle. 
It is bidirectional.

- During the REQUEST phase, it executes from top to bottom.
- During the RESPONSE phase, it executes from bottom to top.

Two Built-in Django Middlewares:
- `django.middleware.security.SecurityMiddleware`: Enhances server security by automatically handling SSL redirects, cross-site scripting (XSS) protection headers, and content-type sniffing protection.
- `django.contrib.auth.middleware.AuthenticationMiddleware`: Associates users with requests using sessions. It runs on every request to find out which user logged in, attaching a `request.user` object directly to the incoming data for your views to read.
"""

"""
3. WSGI vs ASGI

- WSGI (Web Server Gateway Interface): The traditional, synchronous Python standard. It handles requests one by one per worker thread. 
- ASGI (Asynchronous Server Gateway Interface): The modern successor to WSGI. It allows asynchronous handling, meaning a single thread can process multiple background tasks or concurrent connections without blocking.

Default: Django uses WSGI by default for standard, synchronous request-response loops.
When to switch to ASGI: To build real-time asynchronous features into the application, such as 
WebSockets, chat applications, long-polling, or massive background processes.
"""

"""
4. MVC PATTERN TO DJANGO MVT MAPPING

- Model (MVC)      -->  Model (MVT): Maps directly. It manages the data models, 
                        database constraints, and queries.
- Controller (MVC) -->  View (MVT): The controller manages logic, receives input, 
                        and updates the data/view. In Django, the `views.py` 
                        functions perform this logical routing and data fetching.
- View (MVC)       -->  Template (MVT): The view in MVC handles user presentation. 
                        In Django, templates (.html files with template language) 
                        display the frontend to the end user.

Django itself acts as the structural Controller behind the scenes by 
handling the URL routing system and core middleware mechanics.
"""