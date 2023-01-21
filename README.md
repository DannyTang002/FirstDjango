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
