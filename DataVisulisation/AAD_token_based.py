import pyodbc
from msal import ConfidentialClientApplication

# AAD and database details
tenant_id = 'JAME@power.kea.dk' # Azure AD Tenant ID
client_id = 'your_client_id'  # Azure AD Application ID
client_secret = 'your_client_secret'  # Azure AD Application Secret
authority = f'https://login.microsoftonline.com/{tenant_id}'
resource_app_id = 'https://database.windows.net/'  # Resource for Azure SQL

# SQL connection details
server = 'iotkea.database.windows.net'
database = 'iotdb'
driver = '{ODBC Driver 17 for SQL Server}'

# Acquire a token from AAD
app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
token_response = app.acquire_token_for_client(scopes=[resource_app_id + "/.default"])

if 'access_token' in token_response:
    access_token = token_response['access_token']
    conn_string = (
        f"DRIVER={driver};SERVER={server};DATABASE={database};"
        f"Authentication=ActiveDirectoryAccessToken;"
        f"AccessToken={access_token}"
    )

    # Connect to the database
    try:
        conn = pyodbc.connect(conn_string)
        print("Connection successful")

        # Example query
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 10 * FROM your_table")  # Replace 'your_table' with a table name
        for row in cursor:
            print(row)

        # Close the connection
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)
else:
    print("Failed to acquire AAD token:", token_response.get("error_description"))
