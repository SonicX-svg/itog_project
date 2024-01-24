from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test_cat_translate():
    response = client.post("/predict/",
        json={"text": "сat"}
    )
    json_data = response.json() 
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', json_data)
    assert response.status_code == 200
    assert json_data["translation_text"] == 'Cat'

