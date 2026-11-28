
import pymysql

#pymysql = Third-party library.

# MySQL Connection
def get_db_connection(): # connect DB
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Lakshmi@1",
        database="bank_db",
        
    )


# Retrieve all bank accounts

def get_bank_accounts():

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bank_accounts")

        bank_accounts = cursor.fetchall()

        return bank_accounts

    finally:
        cursor.close()
        conn.close() # memory cosume, concurancy , locking, security 


# Calling the function
result = get_bank_accounts()

print("All Bank Account Records:")

for bank_account in result:
    print(bank_account)
