# itog_project
[![Typing SVG](http://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&background=FFFFFF00&random=false&width=600&lines=This+is+the+final+software+engineering+project)](https://git.io/typing-svg)
## In this project, the machine learning model (Helsinki-NLP/opus-mt-en-ru) is deployed in the cloud using Back4App Container.
___________
## Application launch
### Launch: 
uvicorn main:app
### Request:
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text": "cat"}'
