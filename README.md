# abcbus
abc to collect busdata,use django+bootstrap+buildin template engine

#how to install & run it?
pip install -r requirements.txt

python manage.py makemigrations collect

python manage.py migrate

python manage.py runserver

#how to access?
1. python manage.py createsuperuser 
2. login in admin page and create dept,user,etc.specfy some rights
3. logout as admin and login as a odinary user
