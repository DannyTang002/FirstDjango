"# FirstDjango" 
 

-views and templates
views are ways to give the user feedback when they are sending a html request. The views can be represented as renders, which gives back a html-site in forms of templates. 

Every view is represented by urls, and you can make more urls in the url.py folders where you create path objects. Each path has different url-headers and a method which fires when the url gets triggered. The methods are from the views file. 

-Apps
when you create a webapplication with django you want to divide the whole app into different smaller "functions" those functions are represented as apps. 

Apps can be created with the function
py manage.py startapp <Name>
Each app contains just like any other directory url.py admin.py etc.

Make sure to name-space the views url in each app so that django doesnt get confused. For instance when creating a homepage you want to make sure that the url to that homepage is called with index/appname. Each app has its own templates aswell, and are called upon with name-spacing aswell.
To make sure you can reach each app-page with html-request you also need to import the app's url to the main url list. That can be done by creating paths using include methods, to include urls from other apps. 


-Migrations
 Migration commands, if you want to make own migrations 
 create models(data that will be stored in the database)
run the command 
    py manage.py makemigrations
    py manage.py migrate
The database is represented as an table and each model is data stored in that table. The database is a sqlite3 database. 

-Database ORM
If you want to interact with the database you can call the command py manage.py shell.
This command sends you to a python shell and you can create objects to add in the database etc. But each time you add a model to the database and look into the database tabel, each object is refered as a model.object, and all objects look the same. To make sure that every object is different and that you can see that, have the function __str__(self) (returns something for example title) where you can it so every time a object is called upon, you will se it as something else.


-ADMIN
to create an admin for your webbapplication run the command: 
py manage.py createsuperuser

With this you can interact with your database etc. To make sure that your models get imported correctly into the admin page add an admin function to the admin.py file. 

In this instance: admin.site.register(Article)

then the Article, which is in the local database will be visible in the admin page. In the admin page you can now add new articles and edit article objects. Thanks to the __str__ method in the model all the article objects are presented by their title. 

-TEMPLATE TAGS 
This is a way to display your data(models) into the view. This is done by so called template tags which is sending a third parameter to the render object in the view. There you are essentially sending a list of data(your database). Since the view takes in the template as a parameter the template also has acsess to the database(template tag). 

the template tag is like this:
first make the database a variable

database = data.object.all()
then send in a template tag as a div 
{'database':databse}. The tag datas can now be used in the template 
When you want to do basic python code like if-staments forloop do it inside {% python code %}. When you want to represent data from the database you use {{ database stuff }}

for example if you want to have a list of your data in the template it will look like this 

{% for data in database %}
    h1>{{data.title}}h1
{% endfor %}


-METHODS IN MODELS
If you want to add methods to manipuate each model you can add functions there and call them in the template.

-static files and images
static files are images, js files css files, files that doesnt change for the client and the browser.
For instance if you want to style a certain template you can use a static style.css file. In the settings make sure that you add a function for your base dir. This is so that 

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    # '/var/www/static/',
)

för att django ska kunna hitta de statiska filer
Asåå basedir(vart vi är ) + assets som är Directory för våra statiska filer. 
urlpatterns +=staticfiles_urlpatterns() checks debug mode.

-EXTENDING TEMPLATES


