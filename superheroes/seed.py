from app import db
from app.models import Hero, Power, HeroPower

# Drop all existing data (optional, for fresh start)
db.drop_all()
db.create_all()

# ------------------- Heroes -------------------
heroes = [
    Hero(name="Peter Parker", super_name="Spider-Man"),
    Hero(name="Bruce Wayne", super_name="Batman"),
    Hero(name="Clark Kent", super_name="Superman"),
    Hero(name="Diana Prince", super_name="Wonder Woman")
]

# ------------------- Powers -------------------
powers = [
    Power(name="Web-Slinging", description="Can shoot webs and swing between buildings"),
    Power(name="Martial Arts", description="Expert hand-to-hand combat skills"),
    Power(name="Super Strength", description="Incredible physical strength"),
    Power(name="Flight", description="Can fly through the air at high speeds"),
]

# ---------------- Hero-Power Associations ----------------
hero_powers = [
    HeroPower(hero=heroes[0], power=powers[0], strength="Strong"),
    HeroPower(hero=heroes[1], power=powers[1], strength="Average"),
    HeroPower(hero=heroes[2], power=powers[2], strength="Very Strong"),
    HeroPower(hero=heroes[2], power=powers[3], strength="Very Strong"),
    HeroPower(hero=heroes[3], power=powers[2], strength="Strong"),
]

# Add all to session
for hero in heroes:
    db.session.add(hero)
for power in powers:
    db.session.add(power)
for hp in hero_powers:
    db.session.add(hp)

# Commit to database
db.session.commit()

print("Database seeded successfully!")
