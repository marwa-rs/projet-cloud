from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_returns_200():
    response = client().get("/")
    assert response.status_code == 200


def test_home_contains_title():
    response = client().get("/")
    assert b"Plateforme Cloud" in response.data


def test_health_returns_ok():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_returns_404():
    response = client().get("/nexiste-pas")
    assert response.status_code == 404
