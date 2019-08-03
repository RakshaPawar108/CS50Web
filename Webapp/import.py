import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost/flights")
db = scoped_session(sessionmaker(bind = engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for ori, des, dur in reader:
#the entry in curly braces is what we call a python dictionary that tells the query what to fill in each of those individual placeholders.

# :origin means plceholder for origin that sqlalchemy supports
        db.execute("INSERT INTO flights(origin, destination, duration) VALUES( :origin, :destination, :duration)", {"origin":ori, "destination":des, "duration": dur})
        print(f"Added flight from {ori} to {des} lasting {dur} minutes")
    db.commit()

if __name__ == "__main__":
    main()
