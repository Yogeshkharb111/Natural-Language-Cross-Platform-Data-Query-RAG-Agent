import os
from dotenv import load_dotenv
import mysql.connector
from typing import List, Dict, Any
import json

# Load environment variables
load_dotenv()

class MySQLTool:
    """
    MySQL tool for LangChain agent to query portfolio and transaction data
    """
    
    def __init__(self):
        self.config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DB"),
        }
    
    def execute_portfolio_query(self, query_description: str) -> List[Dict[str, Any]]:
        """
        Execute portfolio queries based on natural language description
        """
        try:
            # Parse the query description to determine what data to fetch
            sql_query = self._generate_portfolio_sql(query_description)
            
            return self._execute_sql(sql_query)
            
        except Exception as e:
            return [{"error": f"Portfolio query failed: {str(e)}"}]
    
    def analyze_transactions(self, analysis_type: str) -> List[Dict[str, Any]]:
        """
        Analyze transaction patterns and trends
        """
        try:
            sql_query = self._generate_transaction_sql(analysis_type)
            return self._execute_sql(sql_query)
            
        except Exception as e:
            return [{"error": f"Transaction analysis failed: {str(e)}"}]
    
    def get_rm_analytics(self, analysis_type: str) -> List[Dict[str, Any]]:
        """
        Get relationship manager performance analytics
        """
        try:
            if "performance" in analysis_type.lower() or "ranking" in analysis_type.lower():
                sql_query = """
                SELECT 
                    rm.manager_name,
                    COUNT(DISTINCT p.client_id) as client_count,
                    SUM(p.amount) as total_aum,
                    AVG(p.amount) as avg_portfolio_value,
                    rm.portfolio_value
                FROM relationship_managers rm
                LEFT JOIN portfolios p ON rm.id = p.client_id
                GROUP BY rm.id, rm.manager_name, rm.portfolio_value
                ORDER BY total_aum DESC
                """
            else:
                sql_query = "SELECT * FROM relationship_managers ORDER BY portfolio_value DESC"
            
            return self._execute_sql(sql_query)
            
        except Exception as e:
            return [{"error": f"RM analytics failed: {str(e)}"}]
    
    def get_portfolio_summary(self) -> Dict[str, Any]:
        """Get overall portfolio summary statistics"""
        try:
            queries = {
                "total_aum": "SELECT SUM(amount) as total_aum FROM portfolios",
                "client_count": "SELECT COUNT(DISTINCT client_id) as client_count FROM portfolios",
                "avg_portfolio": "SELECT AVG(amount) as avg_portfolio FROM portfolios",
                "top_assets": """
                    SELECT asset_type, SUM(amount) as total_amount 
                    FROM portfolios 
                    GROUP BY asset_type 
                    ORDER BY total_amount DESC 
                    LIMIT 5
                """
            }
            
            summary = {}
            for key, query in queries.items():
                result = self._execute_sql(query)
                summary[key] = result[0] if result else {}
            
            return summary
            
        except Exception as e:
            return {"error": f"Portfolio summary failed: {str(e)}"}
    
    def _generate_portfolio_sql(self, description: str) -> str:
        """Generate SQL query based on natural language description"""
        
        desc_lower = description.lower()
        
        if "top" in desc_lower and "portfolio" in desc_lower:
            limit = self._extract_number(description) or 5
            return f"""
            SELECT client_id, asset_type, amount, stock_symbol
            FROM portfolios 
            ORDER BY amount DESC 
            LIMIT {limit}
            """
        
        elif "breakdown" in desc_lower and "relationship manager" in desc_lower:
            return """
            SELECT 
                rm.manager_name,
                SUM(p.amount) as total_portfolio_value,
                COUNT(p.client_id) as client_count,
                AVG(p.amount) as avg_portfolio_value
            FROM relationship_managers rm
            LEFT JOIN portfolios p ON rm.id = p.client_id
            GROUP BY rm.id, rm.manager_name
            ORDER BY total_portfolio_value DESC
            """
        
        elif "stock" in desc_lower or "symbol" in desc_lower:
            return """
            SELECT client_id, stock_symbol, amount, asset_type
            FROM portfolios 
            WHERE stock_symbol IS NOT NULL
            ORDER BY amount DESC
            """
        
        else:
            # Default portfolio query
            return """
            SELECT client_id, asset_type, amount, stock_symbol
            FROM portfolios 
            ORDER BY amount DESC 
            LIMIT 10
            """
    
    def _generate_transaction_sql(self, analysis_type: str) -> str:
        """Generate SQL for transaction analysis"""
        
        analysis_lower = analysis_type.lower()
        
        if "recent" in analysis_lower:
            return """
            SELECT client_id, transaction_type, amount, asset_type, transaction_date
            FROM transactions 
            ORDER BY transaction_date DESC 
            LIMIT 20
            """
        
        elif "volume" in analysis_lower or "pattern" in analysis_lower:
            return """
            SELECT 
                asset_type,
                transaction_type,
                COUNT(*) as transaction_count,
                SUM(amount) as total_amount,
                AVG(amount) as avg_amount
            FROM transactions 
            GROUP BY asset_type, transaction_type
            ORDER BY total_amount DESC
            """
        
        else:
            return """
            SELECT client_id, transaction_type, amount, asset_type, transaction_date
            FROM transactions 
            ORDER BY amount DESC 
            LIMIT 15
            """
    
    def _execute_sql(self, query: str) -> List[Dict[str, Any]]:
        """Execute SQL query and return results"""
        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            cursor.close()
            connection.close()
            
            return results
            
        except Exception as e:
            return [{"error": f"SQL execution failed: {str(e)}"}]
    
    def _extract_number(self, text: str) -> int:
        """Extract number from text"""
        import re
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else None

def run_sql_query(sql_query: str) -> list:
    """
    Run a SELECT query on MySQL database.
    """
    try:
        if not sql_query.strip().lower().startswith("select"):
            return {"error": "Only SELECT queries are allowed."}

        connection = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = connection.cursor(dictionary=True)

        cursor.execute(sql_query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    except Exception as e:
        return {"error": f"MySQL Error: {e}"}

def get_portfolio_summary():
    """
    Get portfolio summary for all clients
    """
    query = """
    SELECT 
        client_name,
        asset_type,
        amount,
        current_value,
        relationship_manager,
        stock_symbol
    FROM portfolios 
    ORDER BY current_value DESC
    """
    return run_sql_query(query)

def get_top_portfolios(limit=5):
    """
    Get top portfolios by value
    """
    query = f"""
    SELECT 
        client_name,
        asset_type,
        amount,
        current_value,
        relationship_manager,
        stock_symbol,
        (current_value - amount) as profit_loss
    FROM portfolios 
    ORDER BY current_value DESC 
    LIMIT {limit}
    """
    return run_sql_query(query)

def get_rm_performance():
    """
    Get relationship manager performance
    """
    query = """
    SELECT 
        rm.name as rm_name,
        rm.id as rm_id,
        COUNT(DISTINCT p.client_name) as client_count,
        SUM(p.current_value) as total_aum,
        AVG(p.current_value) as avg_portfolio_value
    FROM relationship_managers rm
    LEFT JOIN portfolios p ON rm.id = p.relationship_manager
    GROUP BY rm.id, rm.name
    ORDER BY total_aum DESC
    """
    return run_sql_query(query)
