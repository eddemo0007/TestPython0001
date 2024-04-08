import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create a new customer
def create_customer(name, email):
    query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    cur.execute(query, (name, email))
    conn.commit()

# Read all customers
def read_customers():
    query = "SELECT * FROM customers"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Update a customer
def update_customer(id, name, email):
    query = "UPDATE customers SET name = %s, email = %s WHERE id = %s"
    cur.execute(query, (name, email, id))
    conn.commit()

# Delete a customer
def delete_customer(id):
    query = "DELETE FROM customers WHERE id = %s"
    cur.execute(query, (id,))
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()