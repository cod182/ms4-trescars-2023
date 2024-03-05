 set -o errexit
 pip3 install --upgrade pip
 pip3 install Django===4.0
 pip3 install -r requirements.txt
 python manage.py makemigrations && python manage.py migrate
#  python manage.py collectstatic --noinput