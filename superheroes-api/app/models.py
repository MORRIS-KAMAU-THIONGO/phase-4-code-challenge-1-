from app import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    # Relationships
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')
    powers = association_proxy('hero_powers', 'power')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }
    
    def to_dict_with_powers(self):
        hero_dict = self.to_dict()
        hero_powers_data = []
        
        for hero_power in self.hero_powers:
            hp_dict = {
                'id': hero_power.id,
                'hero_id': hero_power.hero_id,
                'power_id': hero_power.power_id,
                'strength': hero_power.strength,
                'power': hero_power.power.to_dict()
            }
            hero_powers_data.append(hp_dict)
        
        hero_dict['hero_powers'] = hero_powers_data
        return hero_dict

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    # Relationships
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')
    heroes = association_proxy('hero_powers', 'hero')
    
    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError('Description must be present')
        if len(description) < 20:
            raise ValueError('Description must be at least 20 characters long')
        return description
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    
    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError(f'Strength must be one of: {", ".join(valid_strengths)}')
        return strength
    
    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength
        }