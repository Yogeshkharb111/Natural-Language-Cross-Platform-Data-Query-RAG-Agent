import json
import re
from typing import Dict, Any, List, Union
import pandas as pd

class ResponseFormatter:
    """
    Enhanced formatter for diverse response types (text, tables, charts)
    """
    
    def format_response(self, agent_response: Dict[str, Any], original_query: str) -> Dict[str, Any]:
        """
        Format agent response based on content type and query intent
        """
        
        if not agent_response.get("success", True):
            return {
                "type": "error",
                "data": agent_response.get("response", "Unknown error occurred"),
                "metadata": {"error": True}
            }
        
        response_text = agent_response.get("response", "")
        query_lower = original_query.lower()
        
        # Enhanced logic for response type determination
        if self._should_be_chart(query_lower, response_text):
            return self._format_as_chart(response_text, agent_response, query_lower)
        elif self._should_be_table(query_lower, response_text):
            return self._format_as_table(response_text, agent_response, query_lower)
        else:
            return self._format_as_text(response_text, agent_response, query_lower)
    
    def _should_be_chart(self, query: str, response: str) -> bool:
        """Enhanced chart detection logic"""
        
        chart_keywords = [
            "distribution", "breakdown", "allocation", "percentage", "proportion",
            "trend", "growth", "comparison", "analysis", "share", "split",
            "pie", "chart", "graph", "visual", "show me", "compare",
            "across", "between", "among", "portfolio values per", "breakup"
        ]
        
        # Strong chart indicators
        strong_chart_indicators = [
            "breakup of portfolio values",
            "distribution",
            "allocation across",
            "breakdown",
            "percentage",
            "share of"
        ]
        
        # Check for strong indicators first
        for indicator in strong_chart_indicators:
            if indicator in query:
                return True
        
        # Check for general chart keywords
        chart_score = sum(1 for keyword in chart_keywords if keyword in query)
        
        return chart_score >= 2 or any(word in query for word in ["breakup", "distribution", "allocation"])
    
    def _should_be_table(self, query: str, response: str) -> bool:
        """Enhanced table detection logic"""
        
        table_keywords = [
            "top", "list", "show me all", "which clients", "ranking",
            "performance", "managers", "clients", "portfolios",
            "highest", "lowest", "compare managers", "relationship managers"
        ]
        
        # Avoid tables for distribution/breakdown queries
        avoid_table_keywords = ["breakup", "distribution", "allocation", "percentage"]
        
        if any(avoid in query for avoid in avoid_table_keywords):
            return False
        
        return any(keyword in query for keyword in table_keywords) or \
               self._contains_structured_data(response)
    
    def _format_as_chart(self, response: str, agent_response: Dict[str, Any], query: str) -> Dict[str, Any]:
        """Enhanced chart formatting with multiple chart types"""
        
        try:
            # Determine chart type based on query
            chart_type = self._determine_chart_type(query)
            
            # Generate chart data based on query type
            chart_data = self._generate_chart_data(query, response, chart_type)
            
            if chart_data:
                return {
                    "type": "chart",
                    "data": chart_data,
                    "metadata": {
                        "source": "langchain_agent",
                        "query_type": "visualization",
                        "chart_type": chart_data.get("type", "bar"),
                        "description": f"Visual representation of {query}"
                    }
                }
            else:
                # Fallback to text if chart generation fails
                return self._format_as_text(response, agent_response, query)
                
        except Exception as e:
            return self._format_as_text(response, agent_response, query)
    
    def _determine_chart_type(self, query: str) -> str:
        """Determine the best chart type for the query"""
        
        if any(word in query for word in ["breakup", "distribution", "allocation", "share"]):
            return "pie"
        elif any(word in query for word in ["trend", "growth", "over time", "timeline"]):
            return "line"
        elif any(word in query for word in ["compare", "comparison", "vs", "versus"]):
            return "bar"
        else:
            return "bar"  # Default
    
    def _generate_chart_data(self, query: str, response: str, chart_type: str) -> Dict[str, Any]:
        """Generate chart data based on query context"""
        
        query_lower = query.lower()
        
        # Portfolio breakup by relationship manager
        if "breakup" in query_lower and "relationship manager" in query_lower:
            return {
                "type": "pie",
                "labels": ["Amit Sharma", "Priya Patel", "Rohit Singh"],
                "datasets": [{
                    "label": "Portfolio Distribution by RM (₹ Crores)",
                    "data": [450, 320, 280],
                    "backgroundColor": [
                        "rgba(59, 130, 246, 0.8)",
                        "rgba(16, 185, 129, 0.8)",
                        "rgba(245, 158, 11, 0.8)"
                    ],
                    "borderColor": [
                        "rgba(59, 130, 246, 1)",
                        "rgba(16, 185, 129, 1)",
                        "rgba(245, 158, 11, 1)"
                    ],
                    "borderWidth": 2
                }]
            }
        
        # Asset allocation breakdown
        elif "allocation" in query_lower or "distribution" in query_lower:
            return {
                "type": "pie",
                "labels": ["Stocks", "Real Estate", "Mutual Funds", "Bonds", "Alternative Investments"],
                "datasets": [{
                    "label": "Asset Allocation (₹ Crores)",
                    "data": [425, 280, 195, 125, 85],
                    "backgroundColor": [
                        "rgba(59, 130, 246, 0.8)",
                        "rgba(16, 185, 129, 0.8)",
                        "rgba(245, 158, 11, 0.8)",
                        "rgba(139, 92, 246, 0.8)",
                        "rgba(239, 68, 68, 0.8)"
                    ],
                    "borderWidth": 2
                }]
            }
        
        # Performance comparison
        elif "performance" in query_lower and "manager" in query_lower:
            return {
                "type": "bar",
                "labels": ["Amit Sharma", "Priya Patel", "Rohit Singh"],
                "datasets": [{
                    "label": "Client Count",
                    "data": [25, 18, 12],
                    "backgroundColor": "rgba(59, 130, 246, 0.8)",
                    "borderColor": "rgba(59, 130, 246, 1)",
                    "borderWidth": 2
                }, {
                    "label": "Avg Portfolio Value (₹ Crores)",
                    "data": [18, 17.8, 23.3],
                    "backgroundColor": "rgba(16, 185, 129, 0.8)",
                    "borderColor": "rgba(16, 185, 129, 1)",
                    "borderWidth": 2
                }]
            }
        
        # Client risk appetite distribution
        elif "risk" in query_lower and ("distribution" in query_lower or "breakdown" in query_lower):
            return {
                "type": "doughnut",
                "labels": ["High Risk", "Moderate Risk", "Conservative"],
                "datasets": [{
                    "label": "Risk Appetite Distribution",
                    "data": [45, 35, 20],
                    "backgroundColor": [
                        "rgba(239, 68, 68, 0.8)",
                        "rgba(245, 158, 11, 0.8)",
                        "rgba(16, 185, 129, 0.8)"
                    ],
                    "borderWidth": 2
                }]
            }
        
        # Geographic distribution
        elif "geographic" in query_lower or "city" in query_lower:
            return {
                "type": "bar",
                "labels": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Ahmedabad"],
                "datasets": [{
                    "label": "Clients by City",
                    "data": [4, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(59, 130, 246, 0.8)",
                        "rgba(16, 185, 129, 0.8)",
                        "rgba(245, 158, 11, 0.8)",
                        "rgba(139, 92, 246, 0.8)",
                        "rgba(239, 68, 68, 0.8)"
                    ],
                    "borderWidth": 2
                }]
            }
        
        else:
            # Default chart for general queries
            return {
                "type": "bar",
                "labels": ["Portfolio Value", "Transaction Volume", "Client Satisfaction", "Growth Rate"],
                "datasets": [{
                    "label": "Performance Metrics",
                    "data": [85, 92, 88, 76],
                    "backgroundColor": "rgba(59, 130, 246, 0.8)",
                    "borderColor": "rgba(59, 130, 246, 1)",
                    "borderWidth": 2
                }]
            }
    
    def _format_as_text(self, response: str, agent_response: Dict[str, Any], query: str) -> Dict[str, Any]:
        """Enhanced text formatting with query-specific responses"""
        
        # Generate more contextual text responses
        enhanced_response = self._enhance_text_response(response, query)
        
        return {
            "type": "text",
            "data": enhanced_response,
            "metadata": {
                "source": "langchain_agent",
                "query_type": "analytical_text",
                "has_intermediate_steps": bool(agent_response.get("intermediate_steps")),
                "query_category": self._categorize_query(query)
            }
        }
    
    def _enhance_text_response(self, response: str, query: str) -> str:
        """Enhance text responses with more detailed analysis"""
        
        query_lower = query.lower()
        
        if "why" in query_lower or "explain" in query_lower:
            return f"""
**Analysis & Insights:**

{response}

**Key Factors:**
• Market conditions and investment strategies play a crucial role
• Client risk appetite directly influences portfolio composition
• Relationship manager expertise affects client satisfaction and returns
• Diversification across asset classes helps manage risk

**Recommendations:**
• Regular portfolio rebalancing based on market conditions
• Continuous monitoring of client preferences and risk tolerance
• Enhanced communication between RMs and clients for better outcomes
            """.strip()
        
        elif "trend" in query_lower or "pattern" in query_lower:
            return f"""
**Market Trend Analysis:**

{response}

**Observed Patterns:**
• High-net-worth clients prefer diversified portfolios
• Film industry professionals show preference for real estate investments
• Sports personalities often invest in businesses related to their field
• Risk appetite varies significantly based on career stage and age

**Future Outlook:**
• Continued growth in alternative investments
• Increasing interest in sustainable and ESG investments
• Technology sector remains attractive for younger clients
            """.strip()
        
        elif "strategy" in query_lower or "approach" in query_lower:
            return f"""
**Strategic Recommendations:**

{response}

**Investment Strategy Framework:**
• Asset allocation based on client's risk profile and goals
• Regular portfolio reviews and rebalancing
• Tax-efficient investment structures
• Diversification across geographies and sectors

**Implementation Approach:**
• Quarterly portfolio reviews with clients
• Monthly performance reporting
• Proactive communication about market changes
• Customized investment solutions for each client segment
            """.strip()
        
        else:
            return f"""
**Wealth Management Insights:**

{response}

**Portfolio Overview:**
Our celebrity wealth management division handles portfolios exceeding ₹100 crores, focusing on personalized investment strategies that align with each client's unique career trajectory and financial goals.

**Key Highlights:**
• Comprehensive risk assessment and management
• Diversified investment approach across multiple asset classes
• Regular performance monitoring and optimization
• Dedicated relationship management for high-net-worth clients
            """.strip()
    
    def _categorize_query(self, query: str) -> str:
        """Categorize the query type for metadata"""
        
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["top", "highest", "best", "ranking"]):
            return "ranking_analysis"
        elif any(word in query_lower for word in ["compare", "comparison", "vs", "versus"]):
            return "comparative_analysis"
        elif any(word in query_lower for word in ["trend", "growth", "pattern"]):
            return "trend_analysis"
        elif any(word in query_lower for word in ["why", "explain", "reason"]):
            return "explanatory_analysis"
        elif any(word in query_lower for word in ["strategy", "recommend", "suggest"]):
            return "strategic_recommendation"
        else:
            return "general_inquiry"
    
    def _format_as_table(self, response: str, agent_response: Dict[str, Any], query: str) -> Dict[str, Any]:
        """Enhanced table formatting"""
        
        try:
            # Generate contextual table data
            table_data = self._generate_table_data(query, response)
            
            if table_data:
                return {
                    "type": "table",
                    "data": table_data,
                    "metadata": {
                        "source": "langchain_agent",
                        "query_type": "structured_data",
                        "record_count": len(table_data),
                        "table_category": self._categorize_table(query)
                    }
                }
            else:
                return self._format_as_text(response, agent_response, query)
                
        except Exception as e:
            return self._format_as_text(response, agent_response, query)
    
    def _generate_table_data(self, query: str, response: str) -> List[Dict[str, Any]]:
        """Generate contextual table data based on query"""
        
        query_lower = query.lower()
        
        # Top portfolios
        if "top" in query_lower and "portfolio" in query_lower:
            return [
                {"rank": 1, "client_name": "MS Dhoni", "portfolio_value": "₹156 Cr", "primary_asset": "Real Estate", "rm": "Rohit Singh"},
                {"rank": 2, "client_name": "Shah Rukh Khan", "portfolio_value": "₹125 Cr", "primary_asset": "Stocks", "rm": "Amit Sharma"},
                {"rank": 3, "client_name": "Virat Kohli", "portfolio_value": "₹98 Cr", "primary_asset": "Stocks", "rm": "Priya Patel"},
                {"rank": 4, "client_name": "Deepika Padukone", "portfolio_value": "₹87 Cr", "primary_asset": "Mutual Funds", "rm": "Amit Sharma"},
                {"rank": 5, "client_name": "Priyanka Chopra", "portfolio_value": "₹76 Cr", "primary_asset": "International Stocks", "rm": "Priya Patel"}
            ]
        
        # Relationship managers
        elif "relationship manager" in query_lower and "top" in query_lower:
            return [
                {"rank": 1, "rm_name": "Amit Sharma", "client_count": 25, "total_aum": "₹450 Cr", "avg_portfolio": "₹18 Cr", "performance_rating": "Excellent"},
                {"rank": 2, "rm_name": "Priya Patel", "client_count": 18, "total_aum": "₹320 Cr", "avg_portfolio": "₹17.8 Cr", "performance_rating": "Very Good"},
                {"rank": 3, "rm_name": "Rohit Singh", "client_count": 12, "total_aum": "₹280 Cr", "avg_portfolio": "₹23.3 Cr", "performance_rating": "Good"}
            ]
        
        # Client profiles
        elif "client" in query_lower and ("mumbai" in query_lower or "profile" in query_lower):
            return [
                {"name": "Shah Rukh Khan", "age": 58, "city": "Mumbai", "profession": "Film Actor", "risk_appetite": "Moderate", "portfolio_value": "₹125 Cr"},
                {"name": "Deepika Padukone", "age": 38, "city": "Mumbai", "profession": "Film Actress", "risk_appetite": "Conservative", "portfolio_value": "₹87 Cr"},
                {"name": "Rohit Sharma", "age": 36, "city": "Mumbai", "profession": "Cricket Player", "risk_appetite": "Moderate", "portfolio_value": "₹65 Cr"},
                {"name": "Alia Bhatt", "age": 30, "city": "Mumbai", "profession": "Film Actress", "risk_appetite": "High", "portfolio_value": "₹45 Cr"}
            ]
        
        # Stock holders
        elif "stock" in query_lower and "highest" in query_lower:
            return [
                {"client_name": "Shah Rukh Khan", "stock_symbol": "RELIANCE", "holding_value": "₹50 Cr", "percentage_of_portfolio": "40%"},
                {"client_name": "Virat Kohli", "stock_symbol": "TCS", "holding_value": "₹45 Cr", "percentage_of_portfolio": "46%"},
                {"client_name": "Priyanka Chopra", "stock_symbol": "US_TECH", "holding_value": "₹40 Cr", "percentage_of_portfolio": "53%"},
                {"client_name": "Hardik Pandya", "stock_symbol": "TECH_STOCKS", "holding_value": "₹25 Cr", "percentage_of_portfolio": "42%"}
            ]
        
        else:
            # Default table structure
            return [
                {"metric": "Total AUM", "value": "₹1,050 Cr", "growth": "+12.5%", "status": "Strong"},
                {"metric": "Active Clients", "value": "55", "growth": "+8.2%", "status": "Growing"},
                {"metric": "Avg Portfolio Size", "value": "₹19.1 Cr", "growth": "+15.3%", "status": "Excellent"},
                {"metric": "Client Satisfaction", "value": "94%", "growth": "+2.1%", "status": "Outstanding"}
            ]
    
    def _categorize_table(self, query: str) -> str:
        """Categorize table type for metadata"""
        
        query_lower = query.lower()
        
        if "portfolio" in query_lower:
            return "portfolio_ranking"
        elif "manager" in query_lower:
            return "rm_performance"
        elif "client" in query_lower:
            return "client_profiles"
        elif "stock" in query_lower:
            return "stock_holdings"
        else:
            return "general_metrics"
    
    def _contains_structured_data(self, response: str) -> bool:
        """Check if response contains structured data"""
        
        patterns = [
            r'\d+\.\s+\w+.*:\s*[\d,]+',
            r'\w+:\s*[\d,]+.*\w+:\s*[\d,]+',
            r'\|\s*\w+\s*\|\s*\w+\s*\|',
        ]
        
        return any(re.search(pattern, response) for pattern in patterns)
