
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
 python manage.py migrate --run-syncdb     
python manage.py createsuperuser
python manage.py runserver
Админка: admin
