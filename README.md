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


