import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """

roles_users = Table(
    "roles_users",
    Base.metadata,
    Column("roles_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("users_id", Integer, ForeignKey("users.id"), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    profile = relationship("Profile", uselist=False) # object
    # roles = relationship("Role", secondary="roles_users") # list
    roles = relationship("Role", secondary=roles_users, backref="users")

""" 
class RoleUser(Base):
    __tablename__ = "roles_users"
    roles_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"), primary_key=True) 
"""

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)

class Priority(Base):
    __tablename__ = "priorities"
    id = Column(Integer, primary_key=True)

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="todos", uselist=False)
    priorities_id = Column(Integer, ForeignKey("priorities.id"), nullable=False)
    priority = relationship("Priority", backref="todos", uselist=False)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
