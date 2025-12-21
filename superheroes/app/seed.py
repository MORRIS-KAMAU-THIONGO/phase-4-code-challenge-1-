from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    ]
    db.session.add_all(heroes)
    
    # Seed Powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")
    ]
    db.session.add_all(powers)
    db.session.commit()

    # Seed HeroPowers
    hero_powers = [
        HeroPower(hero_id=1, power_id=1, strength="Strong"),
        HeroPower(hero_id=1, power_id=2, strength="Average"),
        HeroPower(hero_id=2, power_id=1, strength="Weak")
    ]
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Database seeded successfully!")
