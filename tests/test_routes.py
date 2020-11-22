import pytest
import json
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

def test_acessar_home_status_code_200(client):
    response = client.get("/home")
    assert response.status_code == 200

def test_numero_0(client):
    response = client.get("/extenso/0")
    assert response.get_json() == {"extenso": "zero"}

def test_numero_1(client):
    response = client.get("/extenso/1")
    assert response.get_json() == {"extenso": "um"}

def test_numero_menos_1(client):
    response = client.get("/extenso/-1")
    assert response.get_json() == {"extenso": "menos um"}

def test_numero_10(client):
    response = client.get("/extenso/10")
    assert response.get_json() == {"extenso": "dez"}

def test_numero_menos_10(client):
    response = client.get("/extenso/-10")
    assert response.get_json() == {"extenso": "menos dez"}

def test_numero_15(client):
    response = client.get("/extenso/15")
    assert response.get_json() == {"extenso": "quinze"}

def test_numero_menos_15(client):
    response = client.get("/extenso/-15")
    assert response.get_json() == {"extenso": "menos quinze"}

def test_numero_66(client):
    response = client.get("/extenso/66")
    assert response.get_json() == {"extenso": "sessenta e seis"}

def test_numero_menos_66(client):
    response = client.get("/extenso/-66")
    assert response.get_json() == {"extenso": "menos sessenta e seis"}

def test_numero_100(client):
    response = client.get("/extenso/100")
    assert response.get_json() == {"extenso": "cem"}

def test_numero_menos_100(client):
    response = client.get("/extenso/-100")
    assert response.get_json() == {"extenso": "menos cem"}

def test_numero_101(client):
    response = client.get("/extenso/101")
    assert response.get_json() == {"extenso": "cento e um"}

def test_numero_menos_101(client):
    response = client.get("/extenso/-101")
    assert response.get_json() == {"extenso": "menos cento e um"}

def test_numero_119(client):
    response = client.get("/extenso/119")
    assert response.get_json() == {"extenso": "cento e dezenove"}

def test_numero_menos_119(client):
    response = client.get("/extenso/-119")
    assert response.get_json() == {"extenso": "menos cento e dezenove"}

def test_numero_666(client):
    response = client.get("/extenso/666")
    assert response.get_json() == {"extenso": "seiscentos e sessenta e seis"}

def test_numero_menos_666(client):
    response = client.get("/extenso/-666")
    assert response.get_json() == {"extenso": "menos seiscentos e sessenta e seis"}

def test_numero_1001(client):
    response = client.get("/extenso/1001")
    assert response.get_json() == {"extenso": "mil e um"}

def test_numero_menos_1001(client):
    response = client.get("/extenso/-1001")
    assert response.get_json() == {"extenso": "menos mil e um"}

def test_numero_10001(client):
    response = client.get("/extenso/10001")
    assert response.get_json() == {"extenso": "dez mil e um"}

def test_numero_menos_10001(client):
    response = client.get("/extenso/-10001")
    assert response.get_json() == {"extenso": "menos dez mil e um"}

def test_numero_66666(client):
    response = client.get("/extenso/66666")
    assert response.get_json() == {"extenso": "sessenta e seis mil e seiscentos e sessenta e seis"}

def test_numero_menos_66666(client):
    response = client.get("/extenso/-66666")
    assert response.get_json() == {"extenso": "menos sessenta e seis mil e seiscentos e sessenta e seis"}
