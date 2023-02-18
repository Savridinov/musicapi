FROM python:3.10

WORKDIR /code

COPY . .

RUN pip3 install djangorestframework-simplejwt

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]