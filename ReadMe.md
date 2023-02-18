## Введение
Наш код сейчас будет запускатся на docker-compose потому что на settigs.py

DATABASES = {
    'default': {
        ...
        'HOST': '127.0.0.1', #working on django
        'HOST': 'db', # working on docker compose #right now i don't now how to fix it
        ...
        }
    }
    если хотите чтобы на Django запускался нужно раскоментировать и закомитировать другое

## JWT 
Я дабавил авторизацию через JWT и я писал Unit tests  но пака что незнаю как через токен писат тесты поэтому тесты и CI actions на GitHub тоже выдаст ошыбку


## Запуск
cd misicapi/

# create supersuser
docker-compose exec web python manage.py createsuperuser

#copmpose
docer-compose up
и все 
localhost:8000
 
## Obtain token
localhost:8000/api/token/
и введите свой username and password что вы создали

##  И Header JWT не забудьте
