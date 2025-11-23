Project Overview:

This project is a console-based quiz application built using Python. It retrieves quiz questions from a MySQL database and displays them one by one to the user. The program allows the user to answer questions, move through the quiz, and exit at any time using keyboard actions. The main goal of the project is to understand Python–MySQL connectivity, basic input handling, and simple program logic.

Key Features:

Question Retrieval from Database:
The quiz questions are stored in a MySQL table. Each question is fetched dynamically based on the question number.

Loop-Based Navigation:
The program runs inside a loop so that each question is displayed in sequence until the quiz ends.

Safe Exit Handling:
The project uses keyboard detection to allow the user to exit instantly by pressing the Escape key.

Simple Input Processing:
User input is managed using standard Python functions to collect answers and handle incorrect or empty entries.

Modules Used:
mysql.connector-->

This module is used to:

Connect Python to a MySQL database

Open and close database sessions

Execute SQL queries using a cursor

Fetch rows from the quiz table
It enables full communication between the Python script and the database where quiz questions are stored.

msvcrt-->

This Windows-specific module is used for:

Detecting key presses without waiting for the Enter key

Checking if the Escape key (ESC) was pressed

Allowing the program to break out of the quiz loop instantly
It provides low-level keyboard event control in a console environment.
