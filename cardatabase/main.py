from typing import List, Optional
from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase): pass

class Owner(Base):
    __tablename__ = "owner"
    ownerid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    cars: Mapped[List["Car"]] = relationship(back_populates="owner")

    def __repr__(self) -> str:
        return f"Owner({self.firstname} {self.lastname})"

class Car(Base):
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String(255))
    model: Mapped[str] = mapped_column(String(255))
    model_year: Mapped[int]
    
    owner_id: Mapped[Optional[int]] = mapped_column(ForeignKey("owner.ownerid"))
    owner: Mapped[Optional[Owner]] = relationship(back_populates="cars")

    def __repr__(self) -> str:
        return f"Car({self.brand} {self.model}, {self.model_year})"

engine = create_engine ("sqlite:///cardatabase.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    # CREATE: Adding owners
    owner1 = Owner(firstname="John", lastname="Johnson")
    owner2 = Owner(firstname="Mary", lastname="Robinson")
    
    car1 = Car(brand="Ford", model="Mustang", model_year=2023, owner=owner1)
    car2 = Car(brand="Nissan", model="Leaf", model_year=2020, owner=owner1)
    car3 = Car(brand="Toyota", model="Prius", model_year=2022, owner=owner2)
    
    session.add_all([owner1, owner2, car1, car2, car3])
    session.commit()

    # READ
    print("=== All cars of the owner John ===")
    john = session.scalars(select(Owner).where(Owner.firstname == "John")).first()
    for car in john.cars:
        print(f"- {car} принадлежит {car.owner}")

    # UPDATE
    print("\n=== Updating dates ===")
    car1.model_year = 2024
    session.commit()
    print(f"Updated Mustang: {car1}")

    # DELETE: Удаляем запись
    print("\n=== Deleting ===")
    session.delete(car2)
    session.commit()
    
    remaining_cars = session.scalars(select(Car)).all()
    print(f"Another cars on database: {remaining_cars}")