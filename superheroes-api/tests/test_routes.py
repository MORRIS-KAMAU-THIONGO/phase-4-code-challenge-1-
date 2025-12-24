import json
import pytest

def test_get_heroes(client, sample_hero):
    """Test GET /heroes endpoint."""
    response = client.get('/heroes')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]['name'] == sample_hero.name

def test_get_hero(client, sample_hero):
    """Test GET /heroes/:id endpoint."""
    response = client.get(f'/heroes/{sample_hero.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == sample_hero.id
    assert data['name'] == sample_hero.name

def test_get_nonexistent_hero(client):
    """Test GET /heroes/:id with non-existent ID."""
    response = client.get('/heroes/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

def test_get_powers(client, sample_power):
    """Test GET /powers endpoint."""
    response = client.get('/powers')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_update_power(client, sample_power):
    """Test PATCH /powers/:id endpoint."""
    update_data = {
        "description": "Updated description that is at least 20 characters"
    }
    response = client.patch(
        f'/powers/{sample_power.id}',
        data=json.dumps(update_data),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['description'] == update_data['description']

def test_create_hero_power(client, sample_hero, sample_power):
    """Test POST /hero_powers endpoint."""
    hero_power_data = {
        "strength": "Average",
        "hero_id": sample_hero.id,
        "power_id": sample_power.id
    }
    response = client.post(
        '/hero_powers',
        data=json.dumps(hero_power_data),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['strength'] == hero_power_data['strength']
    assert data['hero']['id'] == sample_hero.id
    assert data['power']['id'] == sample_power.id