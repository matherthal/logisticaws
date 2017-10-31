from psycopg2 import connect

def insertMap(map):
    # Connect to an existing database and open a cursor
    with connect("host='localhost' dbname='vagrant' user='vagrant' password='vagrant'") as conn, conn.cursor() as cur:
        
        #cur.execute("DROP TABLE distance")

        # Execute a command: this creates a new table
        cur.execute("CREATE TABLE distance (origin varchar, destination varchar, value integer);")

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no more SQL injections!)
        cur.execute("INSERT INTO distance (origin, destination, value) VALUES (%s, %s, %s)",
             ("A", "B", 100))

        # Query the database and obtain data as Python objects
        cur.execute("SELECT * FROM distance;")
        cur.fetchone()
        #(1, 100, "abc'def")

        # Make the changes to the database persistent
        conn.commit()