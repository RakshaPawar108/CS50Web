
CREATE TABLE flights(
    -- PRIMARY KEY means this is the primary way I am going to reference flights.
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights
    (origin, destination, duration)
    VALUES('India', 'Paris', 500);

INSERT INTO flights(origin, destination, duration) VALUES('New York', 'London', 415);
INSERT INTO flights(origin, destination, duration) VALUES('Shanghai', 'Paris', 760);
INSERT INTO flights(origin, destination, duration) VALUES('Istanbul', 'Tokyo', 700);
INSERT INTO flights(origin, destination, duration) VALUES('New York', 'Zurich', 435);
INSERT INTO flights(origin, destination, duration) VALUES('Moscow', 'Paris', 245);
INSERT INTO flights(origin, destination, duration) VALUES('Lima', 'New York', 455);

SELECT * FROM flights;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE id = 1;
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
SELECT AVG(duration) from flights;
SELECT AVG(duration) from flights WHERE origin = 'New York';
SELECT COUNT(*) FROM flights;

UPDATE flights
    SET duration = 780
    WHERE origin = 'India'
    AND destination = 'Paris';

DELETE FROM flights WHERE destination = 'Tokyo';

SELECT * FROM flights LIMIT 2;
SELECT * FROM flights ORDER BY duration ASC;
SELECT * FROM flights ORDER BY id ASC;
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;


CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers(name, flight_id) VALUES('Raksha', 1);
INSERT INTO passengers(name, flight_id) VALUES('Alice', 2);
INSERT INTO passengers(name, flight_id) VALUES('Bob', 5);
INSERT INTO passengers(name, flight_id) VALUES('Priya', 1);
INSERT INTO passengers(name, flight_id) VALUES('Charlie', 3);
INSERT INTO passengers(name, flight_id) VALUES('Eric', 6);
INSERT INTO passengers(name, flight_id) VALUES('Brian', 7);
INSERT INTO passengers(name, flight_id) VALUES('Grace', 7);
INSERT INTO passengers(name, flight_id) VALUES('Cece', 3);

SELECT * FROM passengers;

SELECT name, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT name, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';

DELETE FROM passengers WHERE name = 'Bob';
DELETE FROM passengers WHERE name = 'Eric';

SELECT name, origin, destination FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;

-- nested queries

SELECT flight_id from passengers GROUP BY flight_id HAVING COUNT(*) > 1;

SELECT * FROM flights WHERE id IN (SELECT flight_id from passengers GROUP BY flight_id HAVING COUNT(*) > 1);
