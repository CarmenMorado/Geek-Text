# Geek-Text


Getting Started  

 

# Create the project directory 

mkdir geek-text 

cd geek-text 

git clone # add the url for this repository here 

# Create a virtual environment to isolate our package dependencies locally 

python3 -m venv env 

source env/bin/activate  # On Windows use `env\Scripts\activate` 

# Install Django and Django REST framework into the virtual environment 

pip install django 

pip install djangorestframework 

# Change to the direction that you cloned earlier 

cd Geek-Text 

cd mysite 

# Run the server 

python manage.py runserver 

# now you can navigate to the local host on your machine to use this api 

http://localhost:8000 

 

 

Functionality 

 

Book Browsing and Sorting 

 

Users are able to retrieve list of books by genre by visiting http://localhost:8000/Books/Genre and using ?genre= to search. For example, http://localhost:8000/Books/Genre/?genre=technology  

 

Users are able to retrieve list of the top 10 sellers by visiting http://localhost:8000/Books/TopSellers  

 

Users are able to retrieve list of books for a particular rating and higher http://localhost:8000/Books/Rating/ and using ?rating= to search. For example, 

http://localhost:8000/Books/Rating/?rating=2  

 

Users are able to retrieve list of x books at a time where x is an integer from a given position in the overall record set by visiting http://localhost:8000/Books/ and using ?limit = and ?offset= to search. For example, http://localhost:8000/Books/?limit=3&offset=2. The default is 3 books per page. 

 

Profile Management 

 

Administrators are able to create new users using a POST call to  

http://127.0.0.1:8000/Users/ using this format in the body: 

{ 

"username": "", 

"password": "", 

"firstname": "", 

"lastname": "" 

"email": "", 

"address": "" 

} 

(username, password, and email are required.) 

 

Administrators are able to search for a user by their username or email using: 

http://127.0.0.1:8000/Users/search/?username= 

 

Administrators are able to update a user’s info by using a PATCH call: 

http://127.0.0.1:8000/Users/1/ 

Where “1” is the id of the user and using the format: 

{ 

"username": "", 

"password": "", 

"firstname": "", 

"lastname": "" 

"email": "", 

"address": "" 

} 

Exclude any fields which are not needed. 

 

Administrators are able to search for user’s credit card info by using: 

http://127.0.0.1:8000/Users/creditcard/?username= 

 

Shopping Cart 

 

Book Details 

 

Users are able to retrieve list of books by ISBN by visiting 

http://127.0.0.1:8000/Books/Author/ and using ?name= in a GET call. For example, http://127.0.0.1:8000/Books/Author/?name=Matthew Ball 

 

Users are able to search a books by author by visiting 

http://127.0.0.1:8000/Books/ISBN/ and using ?search= in a GET call. For example,  

http://127.0.0.1:8000/Books/ISBN/?search= 978-1324092032 

 

Administrators are able to create authors by making a POST call to http://127.0.0.1:8000/Authors/ and the format in the body must be: 

{ 

    "firstname": "", 

    "lastname": "", 

    "biography": "", 

    "publisher": "" 

} 

 

Administrators are able to create books by making a POST call to http://127.0.0.1:8000/Books/ and the format in the body must be: 

{ 

    "isbn": "", 

    "authorid": "", 

    "genreid": "", 

    "name": "", 

    "description": "", 

    "price": "", 

    "publisher": "", 

    "yearpublished": "", 

    "copiessold": "" 

} 

 

Book Rating and Commenting 

 

Users are able to create a rating review for a book by using a POST call to: 

http://127.0.0.1:8000/Bookratings/ and the format in the body must be: 

 

{	 

    "userid": “", 

    "bookid": "", 

    "rating":  "", 

    "ratingtimestamp":  "{{currentDate}}", 

    "comment":  "", 

    "commenttimestamp":  "{{currentDate}}"     

} 

 

Users are able to retrieve a list of top-rated books by highest to lowest by visiting: 

http://127.0.0.1:8000/Bookratings/TopRated/ 

 

Users are able to retrieve the average rating of a book by visiting: 

http://127.0.0.1:8000/Bookratings/AverageRating/ 

 

 

 

Wishlist Management 

 

Users are able to create a Wishlist of books that belongs to a user by going on Postman, selecting “POST” and using the following URL: http://localhost:8000/Wishlists/. Then, by clicking on “Body” and “x-www-form-urlencoded." In order to create a Wishlist, the keys for “userid,” “bookid,” and “name” must all contain a value.  

 

Users are able to add a book to an existing Wishlist by going on Postman, selecting “POST” and using the following URL: http://localhost:8000/Wishlists/. Then, by clicking on “Body” and “x-www-form-urlencoded." In order to add a book to a Wishlist, the keys for “userid,” “bookid,” and “name” must all contain a value. Users will not be able to add a book twice to the same Wishlist. 

 

Users are able to remove a book from one of their existing Wishlists into their shopping carts by first selecting “DELETE” and using the following URL: http://localhost:8000/Wishlists/id/. The “id” at the end of the URL must correspond to the primary key / id from the existing Wishlist instance that contains the book for deletion. This call will perform two actions at the same time: The book will be removed from their Wishlist and, finally, the book will be added into their shopping cart. In order to view the newly added book in the shopping cart, first select “GET” and use the following URL: http://localhost:8000/Shoppingcarts/. 

 

Users are able to retrieve a list of books from a user’s Wishlist by using query parameters. First, select “GET” and use the following URL: http://localhost:8000/Wishlists/. Next, click “Params.” The keys for “userid” and “name” must all contain a value in order to achieve this.   




Database Schema 

<img width="1065" alt="Database Schema" src="https://user-images.githubusercontent.com/42749527/204108728-a4ebbb4c-4f64-41a6-ae68-5b04c0e1c8c6.png">


