import os
from dotenv import load_dotenv
from pymongo import MongoClient
import mysql.connector

load_dotenv()

def seed_enhanced_mongodb():
    """Seed MongoDB with realistic film star and sports personality data"""
    
    try:
        mongo_uri = os.getenv("MONGO_URI")
        mongo_db = os.getenv("MONGO_DB")
        
        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        collection = db["client_profiles"]
        
        # Enhanced client profiles for film stars and sports personalities
        celebrity_clients = [
            {
                "name": "Shah Rukh Khan",
                "age": 58,
                "city": "Mumbai",
                "email": "srk@example.com",
                "profession": "Film Actor",
                "risk_appetite": "Moderate",
                "investment_preferences": ["Stocks", "Real Estate", "International Markets"],
                "relationship_manager": "1",
                "phone": "+91-9876543210",
                "net_worth_category": "Ultra High",
                "investment_horizon": "Long Term",
                "preferred_sectors": ["Technology", "Entertainment", "Healthcare"]
            },
            {
                "name": "Virat Kohli",
                "age": 35,
                "city": "Delhi",
                "email": "virat@example.com",
                "profession": "Cricket Player",
                "risk_appetite": "High",
                "investment_preferences": ["Stocks", "Startups", "Cryptocurrency"],
                "relationship_manager": "2",
                "phone": "+91-9876543211",
                "net_worth_category": "Ultra High",
                "investment_horizon": "Medium Term",
                "preferred_sectors": ["Sports Tech", "Fitness", "FMCG"]
            },
            {
                "name": "Deepika Padukone",
                "age": 38,
                "city": "Mumbai",
                "email": "deepika@example.com",
                "profession": "Film Actress",
                "risk_appetite": "Conservative",
                "investment_preferences": ["Mutual Funds", "Bonds", "Gold"],
                "relationship_manager": "1",
                "phone": "+91-9876543212",
                "net_worth_category": "High",
                "investment_horizon": "Long Term",
                "preferred_sectors": ["Fashion", "Beauty", "Healthcare"]
            },
            {
                "name": "MS Dhoni",
                "age": 42,
                "city": "Chennai",
                "email": "dhoni@example.com",
                "profession": "Cricket Player",
                "risk_appetite": "Moderate",
                "investment_preferences": ["Real Estate", "Stocks", "Agriculture"],
                "relationship_manager": "3",
                "phone": "+91-9876543213",
                "net_worth_category": "Ultra High",
                "investment_horizon": "Long Term",
                "preferred_sectors": ["Agriculture", "Sports", "Automotive"]
            },
            {
                "name": "Priyanka Chopra",
                "age": 41,
                "city": "Mumbai",
                "email": "priyanka@example.com",
                "profession": "Film Actress",
                "risk_appetite": "High",
                "investment_preferences": ["International Stocks", "Tech Startups", "Real Estate"],
                "relationship_manager": "2",
                "phone": "+91-9876543214",
                "net_worth_category": "Ultra High",
                "investment_horizon": "Medium Term",
                "preferred_sectors": ["Technology", "Entertainment", "Beauty"]
            },
            {
                "name": "Rohit Sharma",
                "age": 36,
                "city": "Mumbai",
                "email": "rohit@example.com",
                "profession": "Cricket Player",
                "risk_appetite": "Moderate",
                "investment_preferences": ["Mutual Funds", "Stocks", "Fixed Deposits"],
                "relationship_manager": "1",
                "phone": "+91-9876543215",
                "net_worth_category": "High",
                "investment_horizon": "Long Term",
                "preferred_sectors": ["Sports", "Food & Beverage", "Real Estate"]
            },
            {
                "name": "Alia Bhatt",
                "age": 30,
                "city": "Mumbai",
                "email": "alia@example.com",
                "profession": "Film Actress",
                "risk_appetite": "High",
                "investment_preferences": ["Startups", "Stocks", "Sustainable Investments"],
                "relationship_manager": "2",
                "phone": "+91-9876543216",
                "net_worth_category": "High",
                "investment_horizon": "Long Term",
                "preferred_sectors": ["Sustainable Energy", "Fashion", "Technology"]
            },
            {
                "name": "Hardik Pandya",
                "age": 30,
                "city": "Ahmedabad",
                "email": "hardik@example.com",
                "profession": "Cricket Player",
                "risk_appetite": "High",
                "investment_preferences": ["Stocks", "Cryptocurrency", "Luxury Assets"],
                "relationship_manager": "3",
                "phone": "+91-9876543217",
                "net_worth_category": "High",
                "investment_horizon": "Medium Term",
                "preferred_sectors": ["Sports", "Luxury", "Technology"]
            }
        ]
        
        # Insert clients
        for client in celebrity_clients:
            if not collection.find_one({"name": client["name"]}):
                collection.insert_one(client)
                print(f"✅ Inserted celebrity client: {client['name']}")
            else:
                print(f"⚠️ Client already exists: {client['name']}")
        
        print("✅ Enhanced MongoDB seeding complete.")
        client.close()
        
    except Exception as e:
        print(f"❌ Enhanced MongoDB seeding failed: {e}")

def seed_enhanced_mysql():
    """Seed MySQL with realistic portfolio and transaction data"""
    
    try:
        mysql_config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DB"),
        }
        
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        # Enhanced relationship managers
        rm_data = [
            (1, "Amit Sharma", 45000000000.00),  # 450 Cr AUM
            (2, "Priya Patel", 32000000000.00),  # 320 Cr AUM
            (3, "Rohit Singh", 28000000000.00),  # 280 Cr AUM
        ]
        
        cursor.execute("DELETE FROM relationship_managers")
        for rm in rm_data:
            cursor.execute("""
            INSERT INTO relationship_managers (id, manager_name, portfolio_value)
            VALUES (%s, %s, %s)
            """, rm)
            print(f"✅ Inserted RM: {rm[1]}")
        
        # Enhanced portfolio data with realistic amounts for celebrities
        portfolio_data = [
            # Shah Rukh Khan's portfolio - 125 Cr
            (1, 1, "Stocks", 5000000000.00, "RELIANCE"),
            (2, 1, "Real Estate", 4000000000.00, "REALTY"),
            (3, 1, "International Stocks", 3500000000.00, "NASDAQ_ETF"),
            
            # Virat Kohli's portfolio - 98 Cr
            (4, 2, "Stocks", 4500000000.00, "TCS"),
            (5, 2, "Startups", 2800000000.00, "STARTUP_FUND"),
            (6, 2, "Cryptocurrency", 2500000000.00, "CRYPTO_FUND"),
            
            # Deepika Padukone's portfolio - 87 Cr
            (7, 3, "Mutual Funds", 4200000000.00, "HDFC_MF"),
            (8, 3, "Bonds", 2800000000.00, "GOVT_BOND"),
            (9, 3, "Gold", 1700000000.00, "GOLD_ETF"),
            
            # MS Dhoni's portfolio - 156 Cr
            (10, 4, "Real Estate", 8000000000.00, "AGRI_LAND"),
            (11, 4, "Stocks", 5600000000.00, "AUTO_STOCKS"),
            (12, 4, "Agriculture", 2000000000.00, "AGRI_FUND"),
            
            # Priyanka Chopra's portfolio - 76 Cr
            (13, 5, "International Stocks", 4000000000.00, "US_TECH"),
            (14, 5, "Tech Startups", 2600000000.00, "TECH_VC"),
            (15, 5, "Real Estate", 1000000000.00, "US_REALTY"),
        ]
        
        cursor.execute("DELETE FROM portfolios")
        for portfolio in portfolio_data:
            cursor.execute("""
            INSERT INTO portfolios (id, client_id, asset_type, amount, stock_symbol)
            VALUES (%s, %s, %s, %s, %s)
            """, portfolio)
            print(f"✅ Inserted portfolio: Client {portfolio[1]} - {portfolio[2]}")
        
        # Enhanced transaction data
        transaction_data = [
            (1, 1, "Buy", 5000000000.00, "Stocks", "RELIANCE", "2024-01-15"),
            (2, 2, "Buy", 4500000000.00, "Stocks", "TCS", "2024-01-20"),
            (3, 3, "Buy", 4200000000.00, "Mutual Funds", "HDFC_MF", "2024-02-01"),
            (4, 4, "Buy", 8000000000.00, "Real Estate", "AGRI_LAND", "2023-12-01"),
            (5, 5, "Buy", 4000000000.00, "International Stocks", "US_TECH", "2024-01-05"),
            (6, 1, "Sell", 500000000.00, "Stocks", "OLD_STOCK", "2024-02-15"),
            (7, 2, "Buy", 2800000000.00, "Startups", "STARTUP_FUND", "2024-02-20"),
            (8, 3, "Buy", 1700000000.00, "Gold", "GOLD_ETF", "2024-03-01"),
        ]
        
        cursor.execute("DELETE FROM transactions")
        for txn in transaction_data:
            cursor.execute("""
            INSERT INTO transactions (id, client_id, transaction_type, amount, asset_type, stock_symbol, transaction_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, txn)
            print(f"✅ Inserted transaction: Client {txn[1]} - {txn[2]} {txn[3]/10000000:.1f} Cr")
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print("✅ Enhanced MySQL seeding complete.")
        
    except Exception as e:
        print(f"❌ Enhanced MySQL seeding failed: {e}")

if __name__ == "__main__":
    print("🌱 Starting enhanced database seeding for celebrity wealth management...")
    seed_enhanced_mongodb()
    seed_enhanced_mysql()
    print("🎉 Enhanced seeding complete!")
