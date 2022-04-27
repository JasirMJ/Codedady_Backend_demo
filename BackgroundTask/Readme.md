https://realpython.com/asynchronous-tasks-with-django-and-celery/

pip install celery

docker run -p 6379:6379 -d redis:5


celery -A BackgroundTask worker -l info

celery -A BackgroundTask beat -l info