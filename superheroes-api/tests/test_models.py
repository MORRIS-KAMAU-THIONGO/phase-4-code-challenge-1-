import pytest
from app.models import Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError

def test_hero_creation(app):
    """Test hero model creation."""
    with app.app_context():
        hero = Hero(name="Test Hero", super_name="Test Super")
        assert hero.name == "Test Hero"
        assert hero.super_name == "Test Super"

def test_power_creation(app):
    """Test power model creation."""
    with app.app_context():
        power = Power(
            name="Test Power",
            description="A description that is at least 20 characters long"
        )
        assert power.name == "Test Power"
        assert len(power.description) >= 20

def test_power_description_validation(app):
    """Test power description validation."""
    with app.app_context():
        # Should fail with short description
        with pytest.raises(ValueError):
            power = Power(name="Test", description="Too short")
        
        # Should pass with long description
        power = Power(
            name="Test Power",
            description="This is a valid description that is long enough"
        )
        assert power.description

def test_hero_power_creation(app, sample_hero, sample_power):
    """Test hero_power model creation."""
    with app.app_context():
        hero_power = HeroPower(
            strength="Average",
            hero_id=sample_hero.id,
            power_id=sample_power.id
        )
        assert hero_power.strength == "Average"
        assert hero_power.hero_id == sample_hero.id
        assert hero_power.power_id == sample_power.id

def test_hero_power_strength_validation(app):
    """Test hero_power strength validation."""
    with app.app_context():
        # Should fail with invalid strength
        with pytest.raises(ValueError):
            hero_power = HeroPower(strength="Invalid")
        
        # Should pass with valid strength
        hero_power = HeroPower(strength="Strong")
        assert hero_power.strength == "Strong"