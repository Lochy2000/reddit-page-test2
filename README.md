![image](https://github.com/user-attachments/assets/b03c7bf3-1959-4f3f-8b73-5a1874fb20e1)

# Redit clone Practise for Project 4

## Getting Started 

### Inital Setup

* Installing Django
pip install django

* Createing new Django project
django-admin startproject redditclone

 * Navigating into project directory
cd redditclone

* Creating main app 
python manage.py startapp posts

### Update Redditclone settings 

* In redditclone / setting.py added 'posts' app to INSTALLED_APPS
  
![image](https://github.com/user-attachments/assets/80bf3f59-9f41-49e1-ab26-7b758165c5fc)



### Create Models 

* In Posts added models.py.
* Added some basic functionality for Title, Comments and posts.
* Using foreign key to make sure users link to posts, categories to posts and comments to posts.

![image](https://github.com/user-attachments/assets/b7b84f6d-bd25-4875-b0bb-08b3a8d0a282)


 ### Setup Main URLS 

  * redditclone / urls.py created urls for posts app:
    
![image](https://github.com/user-attachments/assets/521274ae-c126-4f72-a87e-8bbd7640e91f)


### Setup App URLS

* Next setup the urls for the posts.py pages.
* Pre-added some urls for example the upvoting, updating and deleting. Why it looks longer.

![image](https://github.com/user-attachments/assets/d9af6f49-098b-4dc4-b2d7-01a1eb496daa)

### Started on the posts / views.py 

* Will request and reutrn the different HTML pages, posts, categories forms
* Will also use to validte and login users.

![image](https://github.com/user-attachments/assets/abf2ede5-fcb0-41e0-957b-7ab3e43abf65)

### Setup Templates / posts 

* Added some base.html and different posts and categories page
* Used Tailwind to quickly get some basic css setup.
* Used {% extends 'posts/base.html' %} to add base.html for quick setup on different pages.

  ![image](https://github.com/user-attachments/assets/32a06177-85a0-4c53-9a87-67e033ff8bab)

  ### Run Migrations

  * Using djangos built in database system for quick setup :
  * python manage.py makemigrations  ,  python manage.py migrate
 
  ### Start Server (python manage.py)

  * current progress, server runs showing basic layout.
  * Next need to connet up functionality to allow login, register and creating posts.

  ![image](https://github.com/user-attachments/assets/cc817e3b-4692-45f4-ab39-36881763997d)






