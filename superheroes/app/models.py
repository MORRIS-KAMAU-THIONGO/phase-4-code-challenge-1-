from app import db

class Hero(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers": [hp.to_dict() for hp in self.hero_powers]
        }

class Power(db.Model):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class HeroPower(db.Model):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)
    strength = db.Column(db.String(50), nullable=False)

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    def to_dict(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "strength": self.strength,
            "hero": {
                "id": self.hero.id,
                "name": self.hero.name,
                "super_name": self.hero.super_name
            },
            "power": {
                "id": self.power.id,
                "name": self.power.name,
                "description": self.power.description
            }
        }
