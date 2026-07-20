backend exposes some APIs to work with it.


# API
Application Programming Interface

- a interface to interact with server.

# Designing APIs 

**Use HTTP Methods**
(GET, POST, PUT, DELETE)

**REST ( Representational State Transfer) API **
Two principles:
- URL(endpoint) represents the resource.\
  --> details of user.


- HTTP Method represents the action  
  --> users/profile
  --> users/about
  --> users/

 **Users are the endpoint and profile is the action.**

 # Structure Data 
 - When we get a request for some data, we need to send it in a structured format.
 - One of the famous data formats nowadays is JSON. 

 **JavaScript Object Notation** 

Structured Data is a way to represent key-value pairs.

{
    name : "human",
    key : value
}


# Python FastAPI
- Library in Python to create APIs easily.
- GET endpoint: @app.get('/users')
- POST endpoint: @app.post('/users')


Creating routes in FastAPI : GET endpoints
WE want to access data of all users. Then the endpoint wouls be:
localhost:8000/users

WE can create a function that returns all the usersinside this endpoint.
@app.get('/users')
def get_users():
