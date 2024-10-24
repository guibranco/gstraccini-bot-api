def test_get_label_settings(client):
    response = client.get('/v1/label-settings')
    assert response.status_code == 200
    data = response.get_json()
    assert 'labels' in data
    assert 'total' in data
    assert 'page' in data
    assert 'per_page' in data

def test_pagination(client):
    response = client.get('/v1/label-settings?page=1&per_page=1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['labels']) == 1

def test_filter_by_default(client):
    response = client.get('/v1/label-settings?default=true')
    assert response.status_code == 200
    data = response.get_json()
    for label in data['labels']:
        assert label['default'] is True

def test_filter_by_category(client):
    response = client.get('/v1/label-settings?category=issues')
    assert response.status_code == 200
    data = response.get_json()
    for label in data['labels']:
        assert label['category'] == 'issues'
