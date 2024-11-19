# sqlserver database connection i azure

import pyodbc

print(pyodbc.drivers())

# Connection details
server = 'iotkea.database.windows.net'  # Replace with your Azure SQL Server name
database = 'iotdb'                   # Replace with your database name
driver = '{ODBC Driver 17 for SQL Server}'  # Make sure this matches your installed driver

# Connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'

# Establish the connection
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful")

    # Example query
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM your_table")  # Replace 'your_table' with a table name from your database
    for row in cursor:
        print(row)

    # Close the connection
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
