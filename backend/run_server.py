"""
Server startup script for the Wealth Query RAG Agent
"""
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Seed the databases on startup
    try:
        from db.seed_data import seed_mongodb, seed_mysql
        print("🌱 Seeding databases...")
        seed_mongodb()
        seed_mysql()
        print("✅ Database seeding completed!")
    except Exception as e:
        print(f"⚠️ Database seeding failed: {e}")
        print("Continuing with server startup...")
    
    # Start the FastAPI server
    print("🚀 Starting FastAPI server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
