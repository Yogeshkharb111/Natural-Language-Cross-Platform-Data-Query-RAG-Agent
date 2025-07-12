import os
from dotenv import load_dotenv
from pymongo import MongoClient
import mysql.connector

# ✅ Load environment variables
load_dotenv()

def get_table_columns(cursor, table_name):
    """
    Get column names and types for a specific table
    """
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        return {column[0]: column[1] for column in columns}  # Return dict with column name and type
    except:
        return {}

def seed_mongodb():
    """
    Seed MongoDB with dummy client profiles.
    """
    try:
        mongo_uri = os.getenv("MONGO_URI")
        mongo_db = os.getenv("MONGO_DB")

        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        collection = db["client_profiles"]

        # 📝 Enhanced client profiles with more realistic data
        dummy_clients = [
            {
                "name": "John Doe", 
                "age": 35, 
                "city": "Mumbai", 
                "email": "john@example.com",
                "risk_appetite": "Moderate",
                "investment_preferences": ["Stocks", "Mutual Funds"],
                "relationship_manager": "1",
                "phone": "+91-9876543210"
            },
            {
                "name": "Jane Smith", 
                "age": 28, 
                "city": "Delhi", 
                "email": "jane@example.com",
                "risk_appetite": "High",
                "investment_preferences": ["Stocks", "Derivatives"],
                "relationship_manager": "2",
                "phone": "+91-9876543211"
            },
            {
                "name": "Arjun Kapoor", 
                "age": 42, 
                "city": "Bangalore", 
                "email": "arjun@example.com",
                "risk_appetite": "Conservative",
                "investment_preferences": ["Bonds", "Fixed Deposits"],
                "relationship_manager": "1",
                "phone": "+91-9876543212"
            },
            {
                "name": "Meera Singh", 
                "age": 30, 
                "city": "Pune", 
                "email": "meera@example.com",
                "risk_appetite": "Moderate",
                "investment_preferences": ["Real Estate", "Gold"],
                "relationship_manager": "3",
                "phone": "+91-9876543213"
            },
            {
                "name": "Rajesh Kumar", 
                "age": 45, 
                "city": "Chennai", 
                "email": "rajesh@example.com",
                "risk_appetite": "High",
                "investment_preferences": ["Stocks", "Crypto"],
                "relationship_manager": "2",
                "phone": "+91-9876543214"
            }
        ]

        # ✅ Insert only if the client does not already exist
        for client_profile in dummy_clients:
            if not collection.find_one({"name": client_profile["name"]}):
                collection.insert_one(client_profile)
                print(f"✅ Inserted: {client_profile['name']}")
            else:
                print(f"⚠️ Skipped (already exists): {client_profile['name']}")

        print("✅ MongoDB seeding complete.")
        client.close()

    except Exception as e:
        print(f"❌ MongoDB seeding failed: {e}")

def seed_mysql():
    """
    Seed MySQL by adapting to existing table structure
    """
    try:
        mysql_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DB"),
        }

        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()

        # 🔍 Check existing table structures
        cursor.execute("SHOW TABLES")
        existing_tables = [table[0] for table in cursor.fetchall()]
        print(f"📋 Existing tables: {existing_tables}")

        # 🛡️ Disable foreign key checks temporarily
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        # 📊 Handle relationship_managers table
        if 'relationship_managers' in existing_tables:
            rm_columns = get_table_columns(cursor, 'relationship_managers')
            print(f"🔍 relationship_managers columns: {list(rm_columns.keys())}")
            
            # Clear existing data
            cursor.execute("DELETE FROM relationship_managers")
            
            # Adapt data insertion based on available columns and types
            if 'id' in rm_columns and 'manager_name' in rm_columns:
                # Your table structure: id (int), manager_name, portfolio_value
                rm_data = [
                    (1, "Amit Sharma", 1300000.00),
                    (2, "Priya Patel", 850000.00),
                    (3, "Rohit Singh", 200000.00),
                ]
                
                for rm in rm_data:
                    try:
                        if 'portfolio_value' in rm_columns:
                            cursor.execute("""
                            INSERT INTO relationship_managers (id, manager_name, portfolio_value)
                            VALUES (%s, %s, %s)
                            """, rm)
                        else:
                            cursor.execute("""
                            INSERT INTO relationship_managers (id, manager_name)
                            VALUES (%s, %s)
                            """, (rm[0], rm[1]))
                        print(f"✅ Inserted RM: {rm[1]} (ID: {rm[0]})")
                    except Exception as e:
                        print(f"⚠️ Could not insert RM {rm[1]}: {e}")

        # 📊 Handle clients table (if it exists)
        if 'clients' in existing_tables:
            clients_columns = get_table_columns(cursor, 'clients')
            print(f"🔍 clients columns: {list(clients_columns.keys())}")
            
            # Clear existing data
            cursor.execute("DELETE FROM clients")
            
            # Sample client data
            clients_data = [
                (1, "John Doe", "Mumbai", "john@example.com", 1),
                (2, "Jane Smith", "Delhi", "jane@example.com", 2),
                (3, "Arjun Kapoor", "Bangalore", "arjun@example.com", 1),
                (4, "Meera Singh", "Pune", "meera@example.com", 3),
                (5, "Rajesh Kumar", "Chennai", "rajesh@example.com", 2),
            ]
            
            for client in clients_data:
                try:
                    if 'name' in clients_columns and 'city' in clients_columns:
                        cursor.execute("""
                        INSERT INTO clients (id, name, city, email, manager_id)
                        VALUES (%s, %s, %s, %s, %s)
                        """, client)
                        print(f"✅ Inserted client: {client[1]}")
                except Exception as e:
                    print(f"⚠️ Could not insert client {client[1]}: {e}")

        # 📊 Handle portfolios table
        if 'portfolios' in existing_tables:
            portfolio_columns = get_table_columns(cursor, 'portfolios')
            print(f"🔍 portfolios columns: {list(portfolio_columns.keys())}")
            
            # Clear existing data
            cursor.execute("DELETE FROM portfolios")
            
            # Sample portfolio data adapted to your structure
            portfolio_data = [
                (1, 1, "Stocks", 500000.00, "RELIANCE"),
                (2, 1, "Mutual Funds", 300000.00, "HDFC_MF"),
                (3, 2, "Stocks", 400000.00, "TCS"),
                (4, 2, "Derivatives", 150000.00, "NIFTY_FUT"),
                (5, 3, "Real Estate", 800000.00, "REALTY"),
                (6, 3, "Bonds", 200000.00, "GOVT_BOND"),
                (7, 4, "Gold", 200000.00, "GOLD_ETF"),
                (8, 5, "Stocks", 600000.00, "INFOSYS"),
            ]
            
            for portfolio in portfolio_data:
                try:
                    # Adapt based on your column structure
                    if 'client_id' in portfolio_columns and 'asset_type' in portfolio_columns:
                        cursor.execute("""
                        INSERT INTO portfolios (id, client_id, asset_type, amount, stock_symbol)
                        VALUES (%s, %s, %s, %s, %s)
                        """, portfolio)
                        print(f"✅ Inserted portfolio: Client {portfolio[1]} - {portfolio[2]}")
                    elif 'client_name' in portfolio_columns:
                        # If it uses client_name instead
                        client_names = ["John Doe", "John Doe", "Jane Smith", "Jane Smith", "Arjun Kapoor", "Arjun Kapoor", "Meera Singh", "Rajesh Kumar"]
                        cursor.execute("""
                        INSERT INTO portfolios (client_name, asset_type, amount, stock_symbol)
                        VALUES (%s, %s, %s, %s)
                        """, (client_names[portfolio[0]-1], portfolio[2], portfolio[3], portfolio[4]))
                        print(f"✅ Inserted portfolio: {client_names[portfolio[0]-1]} - {portfolio[2]}")
                except Exception as e:
                    print(f"⚠️ Could not insert portfolio: {e}")

        # 📊 Handle holdings table
        if 'holdings' in existing_tables:
            holdings_columns = get_table_columns(cursor, 'holdings')
            print(f"🔍 holdings columns: {list(holdings_columns.keys())}")
            
            # Clear existing data
            cursor.execute("DELETE FROM holdings")
            
            # Sample holdings data
            holdings_data = [
                (1, 1, "RELIANCE", 1000, 520.00),
                (2, 1, "HDFC_MF", 15000, 21.00),
                (3, 2, "TCS", 800, 531.25),
                (4, 3, "GOVT_BOND", 200, 1010.00),
                (5, 4, "GOLD_ETF", 100, 2100.00),
                (6, 5, "INFOSYS", 1200, 533.33),
            ]
            
            for holding in holdings_data:
                try:
                    if 'client_id' in holdings_columns and 'symbol' in holdings_columns:
                        cursor.execute("""
                        INSERT INTO holdings (id, client_id, symbol, quantity, current_price)
                        VALUES (%s, %s, %s, %s, %s)
                        """, holding)
                        print(f"✅ Inserted holding: Client {holding[1]} - {holding[2]}")
                except Exception as e:
                    print(f"⚠️ Could not insert holding: {e}")

        # 📊 Handle transactions table
        if 'transactions' in existing_tables:
            transaction_columns = get_table_columns(cursor, 'transactions')
            print(f"🔍 transactions columns: {list(transaction_columns.keys())}")
            
            # Sample transaction data
            transaction_data = [
                (1, 1, "Buy", 500000.00, "Stocks", "RELIANCE", "2024-01-15"),
                (2, 2, "Buy", 400000.00, "Stocks", "TCS", "2024-01-20"),
                (3, 3, "Buy", 800000.00, "Real Estate", "REALTY", "2023-12-01"),
                (4, 4, "Buy", 200000.00, "Gold", "GOLD_ETF", "2024-02-15"),
                (5, 5, "Buy", 600000.00, "Stocks", "INFOSYS", "2024-01-05"),
            ]
            
            for txn in transaction_data:
                try:
                    if 'client_id' in transaction_columns:
                        cursor.execute("""
                        INSERT INTO transactions (id, client_id, transaction_type, amount, asset_type, stock_symbol, transaction_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """, txn)
                        print(f"✅ Inserted transaction: Client {txn[1]} - {txn[2]}")
                except Exception as e:
                    print(f"⚠️ Could not insert transaction: {e}")

        # 🛡️ Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        connection.commit()
        cursor.close()
        connection.close()

        print("✅ MySQL seeding complete.")

    except Exception as e:
        print(f"❌ MySQL seeding failed: {e}")

# ---------------------------------------
# 🚀 SEED BOTH DATABASES
# ---------------------------------------

if __name__ == "__main__":
    print("🌱 Starting database seeding...")
    seed_mongodb()
    seed_mysql()
    print("🎉 Seeding complete!")
