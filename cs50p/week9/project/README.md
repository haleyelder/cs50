# Average Reads
#### Description:

This project is a command line program connected to a Firestore database to keep track of reading lists and books titles similar to the Goodreads platform. Originally, I was going to use their API for this project but they halted use of their API a couple years ago. All functionality is found in the project.py file and there were a few iterations and roadblocks for this project to come to fruition.

The main functionality to connect a database and CRUD (create, read, update, delete) operations has stayed the same through but the way to do so had changed. At first, I began working with the GUI toolkit, Tkinter, to create a styled interface to view the lists, entry field to move books around, and buttons to add or delete the titles. I have never worked with a GUI package and had to learn Tkinter functionality and how to apply my functions would interact with it. Over time, I found it quite difficult to get it to do what I had wanted as well as finding a way to test at the end and scrapped the GUI idea. I also was not a fan of the styling capabilities and would have been a whole seperate issue to deal with.

The second main issue I ran into was the database design and connection. Luckily, the documentation to connect and use Firestore were pretty straight forward, but I had still run into a couple bumps. Initially, the main collection was the main "shelf" with three documents of 'to read','reading', and 'read'. The titles were to be the fields within each of the documents, but reading over Firestore's documentation and applying the add and delete operations, this was not going to work well either. Instead, the three shelves of 'to read','reading' and 'read' became the three collections with the titles as the documents so looking up by field names can add and delete said books.

If the initial database structure would have worked out for this project, a stretch goal of mine was to see if it was possible for other users to create their own shelf for these three lists so they can look up other's books and add them to their own lists.

Since we had already practiced these libraries and concepts in the past, I changed my project to use command line arguments to perform specific functions and create specific validations in case the user mistyped. The other items I had used was tabulate to format the lists nicely in the terminal and CSV to write and output the lists file. This is one shortfall I'd like to improve in possible future iterations is there is a lot of repetitive code that could be cleared up and possibly due to the mixing of a database and libraries that needed a specific format of input to complete their tasks.

Let me know if there are any further questions, comments, or concerns about this final.

This is CS50P!