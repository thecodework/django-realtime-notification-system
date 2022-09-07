
Notification APP:

So this application send notification to user in realtime like (Facebook, Instagram) and
this is very common uses of any application where we need to send notification to our user.

How it works?
Using this application system can send notification to their user on particular time, If admin will add any new data in notification table so using django channel It will set one crontab and using celery beat it will start the broadcast_notification task.   

Broadcast_notification Tasks:

This is a celery task which will send the notification to client using django channels which provide websocket connection between system and client.

Main packages that are required for this application are:

Notification App:

Check the notification_app in this repo where tasks and channels are created.

pip install celery
pip install celery_beat
pip install channels
pip install redis

You can look the requirement.txt file as well
