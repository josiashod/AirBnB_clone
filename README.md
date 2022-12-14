0x00. AirBnB clone
==================

Group project

-   By: Guillaume

### Concepts

*For this project, we expect you to look at these concepts:*

-   [Python packages](https://alx-intranet.hbtn.io/concepts/66)
-   [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)

-   [HTML/CSS](https://alx-intranet.hbtn.io/concepts/2)
-   [The trinity of front-end quality](https://alx-intranet.hbtn.io/concepts/4)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220801T224031Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=68f485489aaa32149422beba9da9fd875e6b498542b758940281cb91b2f94eab)

Background Context
------------------

### Welcome to the AirBnB clone project!

Before starting, please read the **AirBnB** concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help you to:

-   put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-   create all classes used for AirBnB (`User`, `State`, `City`, `Place`...) that inherit from `BaseModel`
-   create the first abstracted storage engine of the project: File storage.
-   create all unittests to validate all our classes and storage engine

### What's a command interpreter?

Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc...
-   Do operations on objects (count, compute stats, etc...)
-   Update attributes of an object
-   Destroy an object

### Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it's time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to "design" / "sketch" / "prototype" each element:

-   Create simple HTML static pages
-   Style guide
-   Fake contents
-   No Javascript
-   No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can't apply any design.

Before starting, please fork or clone the repository `AirBnB_clone` from your partner if you were not the owner of the previous project.


Resources
---------

**Read or watch**:

-   [cmd module](https://alx-intranet.hbtn.io/rltoken/8ecCwE6veBmm3Nppw4hz5A "cmd module")
-   **packages** concept page
-   [uuid module](https://alx-intranet.hbtn.io/rltoken/KfL9TqwdI69W6ttG6gTPPQ "uuid module")
-   [datetime](https://alx-intranet.hbtn.io/rltoken/1d8I3jSKgnYAtA1IZfEDpA "datetime")
-   [unittest module](https://alx-intranet.hbtn.io/rltoken/IlFiMB8UmqBG2CxA0AD3jA "unittest module")
-   [args/kwargs](https://alx-intranet.hbtn.io/rltoken/C_a0EKbtvKdMcwIAuSIZng "args/kwargs")
-   [Python test cheatsheet](https://alx-intranet.hbtn.io/rltoken/tgNVrKKzlWgS4dfl3mQklw "Python test cheatsheet")
-   [Learn to Code HTML & CSS](https://alx-intranet.hbtn.io/rltoken/T9KyiA6_Tm3Ny6oTn08S-A "Learn to Code HTML & CSS") (*until "Creating Lists" included*)
-   [Inline Styles in HTML](https://alx-intranet.hbtn.io/rltoken/7NdYbImFNofpB_FXXn3otg "Inline Styles in HTML")
-   [Specifics on CSS Specificity](https://alx-intranet.hbtn.io/rltoken/z_OTPFCjmhXJJi7KJqBCbQ "Specifics on CSS Specificity")
-   [CSS SpeciFishity](https://alx-intranet.hbtn.io/rltoken/7iqk-el4ZVnKeyLoON8Rqg "CSS SpeciFishity")
-   [Introduction to HTML](https://alx-intranet.hbtn.io/rltoken/okP4V3RxFXHkEcQo19AnuQ "Introduction to HTML")
-   [CSS](https://alx-intranet.hbtn.io/rltoken/Ir8Ka59FO6Z_vJQ-gkSG_w "CSS")
-   [MDN](https://alx-intranet.hbtn.io/rltoken/BpSXtcWOGH0UT4XLCoQyJg "MDN")
-   [center boxes](https://alx-intranet.hbtn.io/rltoken/Tlje4XYwyZbUfHkQWGi1WQ "center boxes")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/uV5eZkRZ_XEqYbgPd-0CWw "explain to anyone"), **without the help of Google**:

### General

-   How to create a Python package
-   How to create a command interpreter in Python using the `cmd` module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage `datetime`
-   What is an `UUID`
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function
-   What is HTML
-   How to create an HTML page
-   What is a markup language
-   What is the DOM
-   What is an element / tag
-   What is an attribute
-   How does the browser load a webpage
-   What is CSS
-   How to add style to an element
-   What is a class
-   What is a selector
-   How to compute CSS Specificity Value
-   What are Box properties in CSS


### Copyright - Plagiarism

-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should be W3C compliant and validate with [W3C-Validator](https://alx-intranet.hbtn.io/rltoken/NzQ96QXtBTCMRDicPORzbA "W3C-Validator")
-   All your CSS files should be in `styles` folder
-   All your images should be in `images` folder
-   You are not allowed to use `!important` and `id` (`#...` in the CSS file)
-   You are not allowed to use tags `img`, `embed` and `iframe`
-   You are not allowed to use Javascript
-   Current screenshots have been done on `Chrome 56` or more.
-   No cross browsers
-   You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)


### Python Unit Tests

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder `tests`
-   You have to use the [unittest module](https://alx-intranet.hbtn.io/rltoken/op1-rQGlw0wwwqNBsn1yaw "unittest module")
-   All your test files should be python files (extension: `.py`)
-   All your test files and folders should start by `test_`
-   Your file organization in the tests folder should be the same as your project
-   e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
-   e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
-   All your tests should be executed by using this command: `python3 -m unittest discover tests`
-   You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don't miss any edge case

### GitHub

**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**

More Info
---------

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

### Execution

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

```