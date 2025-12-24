#!/usr/bin/env python3
"""
Seed script to populate the database with initial data
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import Hero, Power, HeroPower

def seed_database():
    """Seed the database with initial data"""
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("🌱 Seeding database...")
        
        # Create heroes
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]
        
        heroes = []
        for data in heroes_data:
            hero = Hero(**data)
            heroes.append(hero)
        
        db.session.add_all(heroes)
        db.session.commit()
        print(f"✅ Created {len(heroes)} heroes")
        
        # Create powers
        powers_data = [
            {
                "name": "super strength",
                "description": "gives the wielder super-human strengths and abilities beyond normal human capacity"
            },
            {
                "name": "flight",
                "description": "gives the wielder the ability to fly through the skies at supersonic speed"
            },
            {
                "name": "super human senses",
                "description": "allows the wielder to use her senses at a super-human level of perception"
            },
            {
                "name": "elasticity",
                "description": "can stretch the human body to extreme lengths and contort into various shapes"
            }
        ]
        
        powers = []
        for data in powers_data:
            power = Power(**data)
            powers.append(power)
        
        db.session.add_all(powers)
        db.session.commit()
        print(f"✅ Created {len(powers)} powers")
        
        # Create hero_powers associations
        hero_powers_data = [
            {"strength": "Strong", "hero_id": 1, "power_id": 2},
            {"strength": "Average", "hero_id": 2, "power_id": 3},
            {"strength": "Weak", "hero_id": 3, "power_id": 4},
            {"strength": "Average", "hero_id": 4, "power_id": 1},
            {"strength": "Strong", "hero_id": 5, "power_id": 1},
            {"strength": "Average", "hero_id": 6, "power_id": 2},
            {"strength": "Strong", "hero_id": 7, "power_id": 3},
            {"strength": "Average", "hero_id": 8, "power_id": 4},
            {"strength": "Weak", "hero_id": 9, "power_id": 1},
            {"strength": "Strong", "hero_id": 10, "power_id": 2}
        ]
        
        hero_powers = []
        for data in hero_powers_data:
            hero_power = HeroPower(**data)
            hero_powers.append(hero_power)
        
        db.session.add_all(hero_powers)
        db.session.commit()
        print(f"✅ Created {len(hero_powers)} hero-power associations")
        
        print("🎉 Database seeding completed successfully!")

if __name__ == '__main__':
    seed_database()