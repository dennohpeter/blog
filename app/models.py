import psycopg2

conn = psycopg2.connect("dbname=d49pt4ur37g33c user=oqrnhavmylzeql password=290ca06f7d3667c7ebeb2d89f1ed502ce9db4ff7d91d2fd4269e92f7052a2283 host=ec2-54-225-241-25.compute-1.amazonaws.com port=5432")  # Connecting to the database
cur = conn.cursor()  # Activate connection using the cursor

