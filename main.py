from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel #библиотека автоматической проверкой формата и типа данных api

app = FastAPI() #создаем приложение fastapi в переменной app 
model_checkpoint = "Helsinki-NLP/opus-mt-en-ru"
translator = pipeline("translation", model=model_checkpoint)
translator("How are you?")

class Item(BaseModel): #ообщить FastAPI, какие именно параметры и какого типа мы ожидаем
    text: str
    
@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/predict/")
def predict(item: Item): #класс для наших данных на основе базовой модели из pydantic
    return translator(item.text)[0]
    

