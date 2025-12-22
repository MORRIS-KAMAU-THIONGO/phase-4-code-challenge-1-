# server/seed.py
#!/usr/bin/env python3

from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    print("Clearing existing data...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    print("Seeding powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    db.session.add_all(powers)
    db.session.commit()

    print("Seeding heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]
    db.session.add_all(heroes)
    db.session.commit()

    print("Seeding some hero_powers (for testing hero details)...")
    # Example association matching the deliverable sample
    hp_example = HeroPower(hero=heroes[0], power=powers[1], strength="Strong")
    db.session.add(hp_example)
    db.session.commit()

    print("Seeding complete!")