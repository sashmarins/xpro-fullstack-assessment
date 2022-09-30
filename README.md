# xpro-fullstack-assessment

BACKEND: working (almost) fully
only issue is I forgot to add email to each of the users so the search endpoint doesn't include searching by email

Frontend Issues: UserLists not added, when logged in you aren't automatically taken to the home page, no place to create a user

Steps to use: 

Create a MySQL database through the cli by opening the terminal and typing ``` mysql -u root -p ``` (or if you changed the login at some point to your mysql login) then run ``` CREATE DATABASE Sasha_Marinskiy ``` (or whatever you would like, but if you do change the database name you will have to change the config in the seed.py file.

find the requirements.txt in the aalbackend directory and install each of the dependincies using ```pip3 install <dependency name> ```

Optionally you can create a virtual environment for this specific project prior to installing the dependincies with pip3 install.

Navigate to the seed.py file in the aalbackend and configure lines 3-9 to match the mysql settings on your system, and even change the database name if you'd like. 

Then navigate to the directrory which holds the seed.py file in your terminal and run ``` python3 seed.py ```

Then you can run ``` python3 manage.py runserver ``` and test the endpoints locally via postman or another service

Endpoints: The default Get, Post, Put, and Delete endpoints are present for both clients and users at http://127.0.0.1:8000/api/{table}/

Custom endpoints: 
POST http://127.0.0.1:8000/api/users/byClient/ with the body { client_id: (int) } will return all the clients for a specific client_id

POST http://127.0.0.1:8000/api/users/login/ {username: (string)} will return a user with a specific username (and also log them in on the frontend)

POST http://127.0.0.1:8000/api/users/search/ {UserSearch: (string)} will return all the users with a first name or username similar to the value inputted into the UserSearch

from my experience with django rest framework if I want to add a body to a query the method needs to be a post or else the body isn't recognized

frontend instructions: navigate to the meshuggah-react directory in your terminal and run npm install, then you should be able to run npm start and access what I have for the website, or you can access the website at https://vast-beach-28015.herokuapp.com
to login:
  as client: tomashaake17
  as user: djentleman99
  or as admin: sashmarins

