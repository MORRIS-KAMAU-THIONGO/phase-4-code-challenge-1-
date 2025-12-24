import pytest
from app import create_app, db
from app.models import Hero, Power, HeroPower

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def sample_hero(app):
    """Create a sample hero for testing."""
    with app.app_context():
        hero = Hero(name="Test Hero", super_name="Test Super")
        db.session.add(hero)
        db.session.commit()
        return hero

@pytest.fixture
def sample_power(app):
    """Create a sample power for testing."""
    with app.app_context():
        power = Power(
            name="Test Power",
            description="A test power description that is at least 20 characters"
        )
        db.session.add(power)
        db.session.commit()
        return power