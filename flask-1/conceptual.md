### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    Design Philosophy. Python emphasizes readability and simplicity. It has a clean and intuitive syntax, making it easy to write and understand code. Python follows the principle of "there should be one—and preferably only one—obvious way to do it." JavaScript was initially designed to add interactivity to web pages and has since evolved into a versatile language for both front-end and back-end development. JavaScript prioritizes flexibility and provides a wide range of features to manipulate web elements.
    
    Typing: Python is a dynamically typed language, meaning you don't have to explicitly declare variable types. Variable types are determined at runtime, which allows for flexibility but can lead to certain errors. JavaScript is also dynamically typed, but it includes a concept called "type coercion" where variables can be implicitly converted to other types. This can sometimes result in unexpected behavior and bugs.
    
    Syntax: Python uses whitespace indentation (usually four spaces) to define code blocks, which enhances code readability. It enforces a consistent indentation style and avoids the need for explicit braces or semicolons. JavaScript uses curly braces ({}) and semicolons (;) to delimit blocks and statements. While it does support indentation, it is not mandatory for defining code blocks.
    
    Use Cases: Python is commonly used for a wide range of applications, including web development, data analysis, scientific computing, artificial intelligence, machine learning, and automation. It has extensive libraries and frameworks, such as Django and Flask, that facilitate web development. JavaScript is primarily used for front-end web development, where it provides interactivity and dynamic content on websites. It is executed in web browsers and enables actions like form validation, animations, and DOM manipulation. With Node.js, JavaScript can also be used for server-side development.
    
    Ecosystem and Libraries: Python has a rich ecosystem with a vast collection of third-party libraries and frameworks. It has powerful libraries for scientific computing (NumPy, SciPy), data analysis (Pandas), machine learning (scikit-learn, TensorFlow, PyTorch), and web development (Django, Flask). JavaScript has a thriving ecosystem primarily focused on web development. It offers numerous frameworks like React, Angular, and Vue.js for building front-end applications. Additionally, Node.js enables server-side JavaScript development, providing access to a wide range of packages through the npm package manager.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    Using the get() method. This allows you to provide a default value to be returned if the key is missing. By default, it returns None when the key is not found.
    Use a try-except block. In this approach, the code tries to access the value corresponding to the key "c" using square brackets. If the key is not found, a KeyError exception is raised. By wrapping the code in a try-except block, you can catch the exception and handle it gracefully. In this case, the except KeyError block assigns None to value when "c" is missing.

- What is a unit test?
    A unit test is a type of software testing that focuses on verifying the correctness of individual units or components of a software application. In programming, a unit typically refers to the smallest testable part of an application, such as a function, method, or class. A unit test is designed to isolate and test each unit in isolation, ensuring that it behaves as expected and produces the correct output for a given set of inputs.

- What is an integration test?
    An integration test is a type of software testing that focuses on verifying the interaction and behavior of multiple components or modules of a software system when integrated together. Unlike unit tests that isolate and test individual units in isolation, integration tests aim to validate the collaboration and communication between different parts of the system.

    Integration tests are typically performed after unit tests and are designed to ensure that the integrated components work correctly as a whole and can successfully exchange data and communicate with each other. They help identify issues that may arise due to incompatible interfaces, data flow problems, or incorrect interactions between various modules.

- What is the role of web application framework, like Flask?
    Overall, web application frameworks like Flask help streamline the development process by providing a set of tools, libraries, and conventions that simplify common web development tasks. They promote code organization, maintainability, and scalability, allowing developers to focus on building the core functionality of their web applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    Ultimately, the decision between route URL parameters and URL query parameters depends on the specific requirements and characteristics of your application. You can also mix both approaches, using route URL parameters for essential and fixed information and query parameters for optional or variable parameters. If the thing is a category/persistent, use a URL string, if its an item/non-persistent, use a URL query param.

- How do you collect data from a URL placeholder parameter using Flask?
  In Flask, you can collect data from a URL placeholder parameter by defining a route with a variable placeholder in the URL pattern. You can then access the value of the placeholder parameter within your view function.

- How do you collect data from the query string using Flask?
    In Flask, you can collect data from the query string using the request.args object. The request.args object contains a dictionary of key-value pairs representing the parameters in the query string of the URL.

- How do you collect data from the body of the request using Flask?
    In Flask, you can collect data from the body of the request using the request object. The request object provides access to the incoming request data, including the data sent in the request body.

    To collect data from the body of the request, you'll need to ensure that the request is sent with the appropriate content type and format. For example, if you're sending JSON data, the request should have the Content-Type header set to application/json.

- What is a cookie and what kinds of things are they commonly used for?
    A cookie is a small piece of data, a txt file, that is stored on the user's device by a website. It is sent by the web server to the user's web browser and then sent back to the server with subsequent requests. Cookies are commonly used for session management, tracking user preferences, and personalizing the user experience on websites. They keep track of important information between sessions.

- What is the session object in Flask?
    In Flask, the session object is a user-specific storage container that allows you to store data across multiple requests. It is a convenient way to store user-related information on the server side, typically in a cookie or a session ID.

    The session object in Flask uses cookies to store a session ID on the client side. This session ID is used to retrieve the corresponding session data stored on the server. The session data is encrypted to prevent tampering by the client.

    The session object provides a dictionary-like interface to store and retrieve data. You can access it using flask.session or simply session in your Flask application.

- What does Flask's `jsonify()` do?
    In Flask, the jsonify() function is a utility provided by Flask's json module. It is used to create a JSON response from a Python object. It converts the Python object into a JSON-formatted string and sets the appropriate Content-Type header in the response.
