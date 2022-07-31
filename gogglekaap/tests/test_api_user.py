def test_get_users(client):
    r = client.get(
        '/api/users',
        follow_redirects=True
    )
    assert r.status_code == 200
    assert len(r.json) == 1


def test_get_user(client, user_data):
    r = client.get(
        '/api/users/1',
        follow_redirects=True
    )
    assert r.status_code == 200
    assert r.json.get("user_id") == user_data.get("user_id")
    assert r.json.get("user_name") == user_data.get("user_name")
