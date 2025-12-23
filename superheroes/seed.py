from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    hero = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    power = Power(
        name="flight",
        description="gives the wielder the ability to fly through the skies at supersonic speed"
    )

    db.session.add_all([hero, power])
    db.session.commit()

    hp = HeroPower(strength="Strong", hero_id=hero.id, power_id=power.id)
    db.session.add(hp)
    db.session.commit()

    print("Database seeded!")
