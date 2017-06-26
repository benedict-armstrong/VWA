drop database if exists cinema_reservation_db;
CREATE DATABASE cinema_reservation_db;

drop sequence if exists user_id_seq cascade;
CREATE SEQUENCE user_id_seq;

drop table if exists users cascade;
CREATE TABLE users (
	id	INTEGER default nextval('user_id_seq') NOT NULL,
	name varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
	password varchar(100) NOT NULL,
    PRIMARY KEY(id)
);

drop sequence if exists movie_id_seq cascade;
CREATE SEQUENCE movie_id_seq;

drop table if exists movie cascade;
CREATE TABLE movie (
	id	INTEGER default nextval('movie_id_seq') NOT NULL,
	length_in_minutes	INTEGER NOT NULL,
	name	varchar(100) NOT NULL UNIQUE,
	release_date	varchar(100) NOT NULL,
    PRIMARY KEY(id)
);

drop sequence if exists cinema_id_seq cascade;
CREATE SEQUENCE cinema_id_seq;

drop table if exists cinema cascade;
CREATE TABLE cinema (
	id	INTEGER default nextval('cinema_id_seq') NOT NULL,
	name	varchar(100) NOT NULL,
	location	varchar(100) NOT NULL,
    PRIMARY KEY(id)
);

drop sequence if exists customer_id_seq cascade;
CREATE SEQUENCE customer_id_seq;

drop table if exists customer cascade;
CREATE TABLE customer(
	id	INTEGER default nextval('customer_id_seq') NOT NULL,
	name	varchar(100) NOT NULL,
	email	varchar(100) NOT NULL,
    telephone_number varchar(100) NOT NULL,
    password	varchar(100) NOT NULL,
    PRIMARY KEY(id)
);

drop sequence if exists room_id_seq cascade;
CREATE SEQUENCE room_id_seq;

drop table if exists room cascade;
CREATE TABLE room (
	id	INTEGER default nextval('room_id_seq') NOT NULL,
	number	varchar(100) NOT NULL UNIQUE,
	cinema_id INTEGER REFERENCES cinema(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

drop sequence if exists seat_id_seq cascade;
CREATE SEQUENCE seat_id_seq;

drop table if exists seat cascade;
CREATE TABLE seat (
	id	INTEGER default nextval('seat_id_seq') NOT NULL,
	seat_number	INTEGER NOT NULL,
	seat_row	INTEGER NOT NULL,
	room_id INTEGER REFERENCES room(id) ON DELETE CASCADE,
    PRIMARY KEY(id),
	UNIQUE (seat_number, seat_row)
);

drop sequence if exists screening_id_seq cascade;
CREATE SEQUENCE screening_id_seq;

drop table if exists screening cascade;
CREATE TABLE screening (
	id	INTEGER default nextval('screening_id_seq') NOT NULL,
	screening_time	TIMESTAMP NOT NULL,
	room_id INTEGER REFERENCES room(id) ON DELETE CASCADE,
    movie_id INTEGER REFERENCES movie(id) ON DELETE CASCADE,
    PRIMARY KEY(id),
	UNIQUE (screening_time, room_id)
);

drop sequence if exists booking_id_seq cascade;
CREATE SEQUENCE booking_id_seq;

drop sequence if exists booking_reference_seq cascade;
CREATE SEQUENCE booking_reference_seq;

drop table if exists booking cascade;
CREATE TABLE booking (
	id	INTEGER default nextval('booking_id_seq') NOT NULL,
	screening_id INTEGER REFERENCES screening(id) ON DELETE CASCADE,
    customer_id INTEGER REFERENCES customer(id) ON DELETE CASCADE,
    booking_reference varchar(10) default nextval('booking_reference_seq') NOT NULL,
    PRIMARY KEY(id),

);

drop sequence if exists ticket_id_seq cascade;
CREATE SEQUENCE ticket_id_seq;

drop table if exists ticket cascade;
CREATE TABLE ticket (
	id	INTEGER default nextval('ticket_id_seq') NOT NULL,
	seat_id INTEGER REFERENCES seat(id) ON DELETE CASCADE,
  	booking_id INTEGER REFERENCES booking(id) ON DELETE CASCADE,
    PRIMARY KEY(id),
	UNIQUE (seat_id,booking_id)
);
