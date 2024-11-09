![image](https://github.com/user-attachments/assets/b03c7bf3-1959-4f3f-8b73-5a1874fb20e1)

# Reddit clone Practise for Project 4

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


## Adding Function
Once the basic layout was created the next step was to setup some functionality. Following the full CRUD (Cread, Read, Update and Delete).
* Using attribute assignment allowed for quick and simple updating of the the SQL data.

### Updating posts / view.py to render all the HTML templates.

#### Post_list
* Access posts data base using Post.objects.all()
* Ordered posts by creation newest date using order_by('-created_at')
* Rendered post_list.html template
* Made posts and categories avaliable in template aswell.

![image](https://github.com/user-attachments/assets/cdd4bd87-5f15-4518-a6b9-02f4e3b49832)

### Post_details 
* Follows same strucutre as post_list
* Looks for post specific id or displays 404 if nothing found. get_object_or_404(Post, id=post_id)
* Fetches comment aswell. Added parent=none for threaded comment to be implemented later.

![image](https://github.com/user-attachments/assets/b41d1740-74bd-420e-a1ac-bd5f234f4ebe)

### @login_required
* Simple method to make sure users are logged in to edit,commit or add anything

### Post_create
* Used POST to hand and request form submission
* used if not all statementn to validate all fields in the form are filled out
* Used a try expect to create posts. Using author=request.user to validate only logged in user to edit or add to form.
* Display a success or failed message.
* Redirect user after post created.
* Get request to handle the display form.

![image](https://github.com/user-attachments/assets/fb0e94da-c680-426f-9f6e-020ad9400c1e)

### Edit_post
* This follows a similar pattern to the Post_create
* used if statement to check the correct user is trying to edit the post. If its the wrong user a message is displayed saying they cannot edit it.
* If its the correct user a If statement using POST requests the information for the post.
* Again using try expect to validate all the fields are field in and a catergory is selected. Using post.save() to update changes.
* Final if its not the POST request then the current post data is displayed.

![image](https://github.com/user-attachments/assets/4f680016-0838-41e3-8e7d-7187d7fba31f)

### Post_delete

* Check if user trying to delete is the correct user.
*  Using POST to request.
*  Delete post by updating object in memory using attribute assignment
*  Finally renders post_confirm_delete to check make sure user wants to delete.

![image](https://github.com/user-attachments/assets/62b2f621-4dee-48b9-a6cf-3425d8241fc7)


## Creating and Updating templates.
* By using a base template allowed to easily extend skeleton in all templates saving a lot of time. Helps reduce DRY (Dont repeat yourself).
* Layout for templates  posts/templates/post/ category_post.html, post_confirm_delete.html, post_form.html, post_list.html, post_details.html
* Using template variable interpolation meant the updated/changed python code in the view.py could easily be added to the html. For example {{ category.name }}.
### Post_list.html 

![image](https://github.com/user-attachments/assets/4de46a41-d1e6-4172-8c8f-de2b6402291e)








