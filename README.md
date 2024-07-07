# Phase 3 CLI+ORM Project 
## Simple Taxonomy 


## Introduction
This command line interface provides a way to track different zoos and the
animals that live there. You can run this program by entering `python lib.cli.py` 
into the terminal from the project directory. You may need to run `chmod +x` on 
the file first to gain permissions.


# File Descriptions

## cli.py
This file provides the user interface for the program. Users can select
from a list of options to manipulate and view the data in the database.

### main
This is the function that is called when the program is started and which
runs the entire time the program is being executed. It's a simple while 
loop that waits for user input and then displays the appropriate data and
options that the user requests.

### menu
Menu is a helper function that simply displays the primary input options
available to the user.




You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

