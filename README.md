# itog_project
##Приложение на модели Helsinki-NLP/opus-mt-en-ru, осущестляющее перевод.
#Запуск: 
uvicorn main:app
#Запрос
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text": "cat"}'


