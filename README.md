
# Realtime Notification APP:

Notification app is useful to send realtime notification to users like(Facebook, Instagram) and this is very common uses case for any application where we need to send notification to our user in realtime.

## How this app works?

Using this App we can send notification to our user on particular time which will be set by the Admin user and all the users will be notified on their page(without refresh) once admin time will reach.

## Workflow

* First open the url [homepage](http://localhost:8000)
* Check your homepage whether it is connected as websocket or not.
* Open Django [admin](http://localhost:8000/admin/) page in another tab
* Go to the **BroadcastNotification** model and crate one new notification object and set the time
* Check your homepage notification icon where the counter will be incremented once admin time will reach
* Click on notification icon where it will list out all the notifications

When admin will add any new data in notification table it will trigger one django post_save signal which will create one crontab object using celery beat and it will start the broadcast_notification task which will pass the data from backend to frontend using django channels.   


## Setup this notification App
1. First of all create one Django project
2. Create one Django app like notification
3. Add 'notification' to your INSTALLED_APPS setting like this: 
  ```
  INSTALLED_APPS = [
    ...
    'notification',

]
```
4. Check the folder path(mainapp\templates\mainapp\base.html.) in this repo for notification icon template. 

5. Consider main app as outer app which is using the feature of notification app.

6. Setup your celery settings
7. Setup  your channels settings
8. Check _consumer.py_ and _router.py_ file which makes websocket connection between backend and frontend.
9. Add asgi setting in _settings.py_ file
10. Update asgi.py file
11. Create one BroadcastNotification model inside the notification app
12. Check broadcast_notification task inside the notification app which  will pass the data to frontend using websocket in async manner. 

10. Create one post_save signal inside the notification app in _models.py_ file which will create one new task using crontab and It will start the broadcast_notification task using celery beat once admin time will reach.

11. Create one template context file(_mainapp\custom_context_processors.py_) for older notification which has to be added in the template list.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                '**mainapp.custom_context_processors.notifications**',
            ],
        },
    },
]

```
 
## Required packages
* pip install celery
* pip install celery_beat
* pip install channels
* pip install redis

You can look the requirements.txt file as well.
Once everything is done you can try the process mention for the application workflow.
***