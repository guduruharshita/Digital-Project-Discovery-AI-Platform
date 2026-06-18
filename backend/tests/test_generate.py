def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_list_artifact_types(client):
    r = client.get("/api/artifact-types")
    assert r.status_code == 200
    types = r.json()["types"]
    assert "srs" in types
    assert "user_stories" in types
    assert "boilerplate" in types


def test_generate_srs(client, mock_ai):
    r = client.post(
        "/api/generate",
        json={"description": "A project management tool for remote teams", "artifact_type": "srs"},
    )
    assert r.status_code == 200
    body = r.json()
    assert "title" in body
    assert "requirements" in body
    assert len(body["requirements"]) > 0


def test_generate_too_short(client):
    r = client.post("/api/generate", json={"description": "short"})
    assert r.status_code == 422


def test_generate_empty(client):
    r = client.post("/api/generate", json={"description": ""})
    assert r.status_code == 422


def test_generate_invalid_type(client):
    r = client.post(
        "/api/generate",
        json={"description": "A valid product description here", "artifact_type": "invalid"},
    )
    assert r.status_code == 422
