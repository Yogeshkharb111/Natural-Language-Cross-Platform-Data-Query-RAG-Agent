import os
from pymongo import MongoClient
from typing import List, Dict, Any
import json

class MongoDBTool:
    """
    MongoDB tool for LangChain agent to query client profiles
    """
    
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("MONGO_DB", "wealth_db")]
        self.collection = self.db["client_profiles"]
    
    def search_clients(self, query: str) -> List[Dict[str, Any]]:
        """
        Search client profiles based on natural language query
        """
        try:
            # Parse the query to determine search criteria
            search_filter = self._parse_search_query(query)
            
            # Execute MongoDB query
            results = list(self.collection.find(search_filter, {"_id": 0}))
            
            return results
            
        except Exception as e:
            return [{"error": f"MongoDB search failed: {str(e)}"}]
    
    def _parse_search_query(self, query: str) -> Dict[str, Any]:
        """
        Parse natural language query into MongoDB filter
        """
        query_lower = query.lower()
        filter_dict = {}
        
        # Location-based searches
        cities = ["mumbai", "delhi", "bangalore", "chennai", "pune", "hyderabad"]
        for city in cities:
            if city in query_lower:
                filter_dict["city"] = {"$regex": city, "$options": "i"}
        
        # Risk appetite searches
        if "high risk" in query_lower or "aggressive" in query_lower:
            filter_dict["risk_appetite"] = "High"
        elif "conservative" in query_lower or "low risk" in query_lower:
            filter_dict["risk_appetite"] = "Conservative"
        elif "moderate" in query_lower:
            filter_dict["risk_appetite"] = "Moderate"
        
        # Investment preference searches
        if "stocks" in query_lower or "equity" in query_lower:
            filter_dict["investment_preferences"] = {"$in": ["Stocks", "Equity"]}
        elif "mutual funds" in query_lower:
            filter_dict["investment_preferences"] = {"$in": ["Mutual Funds"]}
        elif "real estate" in query_lower:
            filter_dict["investment_preferences"] = {"$in": ["Real Estate"]}
        
        # Age-based searches
        if "young" in query_lower:
            filter_dict["age"] = {"$lt": 35}
        elif "senior" in query_lower or "older" in query_lower:
            filter_dict["age"] = {"$gt": 45}
        
        # If no specific filters, return all (with limit)
        return filter_dict
    
    def get_client_by_name(self, name: str) -> Dict[str, Any]:
        """Get specific client by name"""
        try:
            result = self.collection.find_one(
                {"name": {"$regex": name, "$options": "i"}},
                {"_id": 0}
            )
            return result or {"error": f"Client '{name}' not found"}
        except Exception as e:
            return {"error": f"Error finding client: {str(e)}"}
    
    def get_clients_by_rm(self, rm_id: str) -> List[Dict[str, Any]]:
        """Get all clients for a specific relationship manager"""
        try:
            results = list(self.collection.find(
                {"relationship_manager": rm_id},
                {"_id": 0}
            ))
            return results
        except Exception as e:
            return [{"error": f"Error finding clients for RM: {str(e)}"}]
