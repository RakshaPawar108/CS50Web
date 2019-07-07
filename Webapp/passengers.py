import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost/flights")
db = scoped_session(sessionmaker(bind = engine))

def main():

    #List of all flights

    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes")

    #Prompt user to choose a flight

    flight_id = int(input("\n Flight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id": flight_id}).fetchone()

    #Check if flight is valid

    if flight is None:
        print("Error: no such flight.")
        return

    #List passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()
    print("\n Passengers: ")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No Passengers.")

if __name__ == "__main__":
    main()
