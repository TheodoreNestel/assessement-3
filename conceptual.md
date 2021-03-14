### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
- ans: the speed at which python compiles and execute is much faster than JS making it better for backend
  

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  ans: you could use the get method which will try and get c and if nothing is there it will return non unless you specify a value  setting it tho whatever you want
  

- What is a unit test?
- this is a test that test the smallest isolatable part of a code like a singular function

- What is an integration test?
- This type of test makes sure several piece of a software function together. making sure that together they achieve the desired result

- What is the role of web application framework, like Flask?
- flask and other frameworks are a set of tools to allow software developers to start working on their app's functionality without 
- having to write the lenghty code bases needed to get it the basic general functionality  running on a server for example

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application? 
  
  ans: when pulling data from a list or a database using url is better
  ans: when a user is searching for something q string is better



- How do you collect data from a URL placeholder parameter using Flask?
- request.args['name of the param']

- How do you collect data from the query string using Flask?
- using in the route name app.route("/home/<input value to grab here>)

- How do you collect data from the body of the request using Flask?
- request.data

- What is a cookie and what kinds of things are they commonly used for?
- cookies are small values stored in the client. the data they contain is specified by the server 
- the server also specifies when to update a cookie , delete it , or modify a value. also when to start storing the cookie

- What is the session object in Flask?
- a session object is essentially a dictionary built upon cookies. it lets developers store more useful values using the basic
- logic of cookies

- What does Flask's `jsonify()` do?
- returns what it was called on in a json formated string
