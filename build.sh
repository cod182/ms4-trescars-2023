 set -o errexit
 pip3 install --upgrade pip
 pip install -r requirements.txt
 python manage.py collectstatic --noinput
 python manage.py makemigrations && python manage.py migrate