import psycopg2
from psycopg2.extras import RealDictCursor


def connect_test():
    test = psycopg2.connect("host=localhost dbname=cinema_reservation_db user=postgres password=tomturbo")
    cursor_test = test.cursor(cursor_factory=RealDictCursor)
    cursor_test.execute("select * from movie;")
    movie = cursor_test.fetchall()
    print movie

connect_test()