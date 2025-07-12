// FIXED Mock API service with proper query type detection
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export const mockCheckHealth = async () => {
  await delay(500);
  return true;
};

export const mockQueryDatabase = async (query) => {
  await delay(1500); // Simulate processing time

  const queryLower = query.toLowerCase();

  console.log("Mock API processing query:", query);
  console.log("Query lowercase:", queryLower);

  // CHART RESPONSES - Specific detection logic
  const chartKeywords = [
    "asset allocation distribution",
    "breakup of portfolio values",
    "distribution across",
    "allocation across",
    "breakdown",
    "distribution",
    "allocation",
    "share of",
    "percentage of",
  ];

  const isChartQuery = chartKeywords.some((keyword) =>
    queryLower.includes(keyword)
  );

  if (isChartQuery) {
    console.log("✅ Detected CHART query");

    if (
      queryLower.includes("asset allocation") ||
      queryLower.includes("allocation distribution")
    ) {
      return {
        type: "chart",
        data: {
          type: "pie",
          labels: [
            "Stocks & Equity",
            "Real Estate",
            "Mutual Funds",
            "Bonds & Fixed Income",
            "Alternative Investments",
          ],
          datasets: [
            {
              label: "Asset Allocation (₹ Crores)",
              data: [425, 280, 195, 125, 85],
              backgroundColor: [
                "rgba(59, 130, 246, 0.8)", // Blue
                "rgba(16, 185, 129, 0.8)", // Green
                "rgba(245, 158, 11, 0.8)", // Yellow
                "rgba(139, 92, 246, 0.8)", // Purple
                "rgba(239, 68, 68, 0.8)", // Red
              ],
              borderColor: [
                "rgba(59, 130, 246, 1)",
                "rgba(16, 185, 129, 1)",
                "rgba(245, 158, 11, 1)",
                "rgba(139, 92, 246, 1)",
                "rgba(239, 68, 68, 1)",
              ],
              borderWidth: 2,
            },
          ],
        },
        metadata: {
          source: "enhanced_mock",
          query_type: "asset_allocation_chart",
          chart_type: "pie",
          total_aum: "₹1,110 Crores",
        },
      };
    }

    if (
      queryLower.includes(
        "breakup of portfolio values per relationship manager"
      )
    ) {
      return {
        type: "chart",
        data: {
          type: "pie",
          labels: ["Amit Sharma", "Priya Patel", "Rohit Singh"],
          datasets: [
            {
              label: "Portfolio Distribution by RM (₹ Crores)",
              data: [450, 320, 280],
              backgroundColor: [
                "rgba(59, 130, 246, 0.8)",
                "rgba(16, 185, 129, 0.8)",
                "rgba(245, 158, 11, 0.8)",
              ],
              borderColor: [
                "rgba(59, 130, 246, 1)",
                "rgba(16, 185, 129, 1)",
                "rgba(245, 158, 11, 1)",
              ],
              borderWidth: 2,
            },
          ],
        },
        metadata: {
          source: "enhanced_mock",
          query_type: "rm_distribution_chart",
          chart_type: "pie",
        },
      };
    }

    if (queryLower.includes("geographic") || queryLower.includes("city")) {
      return {
        type: "chart",
        data: {
          type: "bar",
          labels: ["Mumbai", "Delhi", "Chennai", "Bangalore", "Ahmedabad"],
          datasets: [
            {
              label: "Clients by City",
              data: [4, 1, 1, 1, 1],
              backgroundColor: [
                "rgba(59, 130, 246, 0.8)",
                "rgba(16, 185, 129, 0.8)",
                "rgba(245, 158, 11, 0.8)",
                "rgba(139, 92, 246, 0.8)",
                "rgba(239, 68, 68, 0.8)",
              ],
              borderWidth: 2,
            },
          ],
        },
        metadata: {
          source: "enhanced_mock",
          query_type: "geographic_distribution",
          chart_type: "bar",
        },
      };
    }

    if (queryLower.includes("risk appetite")) {
      return {
        type: "chart",
        data: {
          type: "doughnut",
          labels: ["High Risk", "Moderate Risk", "Conservative"],
          datasets: [
            {
              label: "Risk Appetite Distribution (%)",
              data: [45, 35, 20],
              backgroundColor: [
                "rgba(239, 68, 68, 0.8)", // Red for High Risk
                "rgba(245, 158, 11, 0.8)", // Yellow for Moderate
                "rgba(16, 185, 129, 0.8)", // Green for Conservative
              ],
              borderWidth: 2,
            },
          ],
        },
        metadata: {
          source: "enhanced_mock",
          query_type: "risk_distribution",
          chart_type: "doughnut",
        },
      };
    }
  }

  // TABLE RESPONSES - Specific table keywords
  const tableKeywords = [
    "top five portfolios",
    "top 5 portfolios",
    "top relationship managers",
    "highest holders",
    "client profiles from mumbai",
    "show me all client profiles",
    "list all",
  ];

  const isTableQuery = tableKeywords.some((keyword) =>
    queryLower.includes(keyword)
  );

  if (isTableQuery) {
    console.log("✅ Detected TABLE query");

    if (
      queryLower.includes("top five portfolios") ||
      queryLower.includes("top 5 portfolios")
    ) {
      return {
        type: "table",
        data: [
          {
            rank: 1,
            client_name: "MS Dhoni",
            portfolio_value: "₹156 Cr",
            primary_asset: "Real Estate",
            rm: "Rohit Singh",
            growth: "+18.5%",
          },
          {
            rank: 2,
            client_name: "Shah Rukh Khan",
            portfolio_value: "₹125 Cr",
            primary_asset: "Stocks",
            rm: "Amit Sharma",
            growth: "+15.2%",
          },
          {
            rank: 3,
            client_name: "Virat Kohli",
            portfolio_value: "₹98 Cr",
            primary_asset: "Stocks",
            rm: "Priya Patel",
            growth: "+22.1%",
          },
          {
            rank: 4,
            client_name: "Deepika Padukone",
            portfolio_value: "₹87 Cr",
            primary_asset: "Mutual Funds",
            rm: "Amit Sharma",
            growth: "+12.8%",
          },
          {
            rank: 5,
            client_name: "Priyanka Chopra",
            portfolio_value: "₹76 Cr",
            primary_asset: "International Stocks",
            rm: "Priya Patel",
            growth: "+19.7%",
          },
        ],
        metadata: {
          source: "enhanced_mock",
          query_type: "top_portfolios_table",
          record_count: 5,
        },
      };
    }

    if (queryLower.includes("top relationship managers")) {
      return {
        type: "table",
        data: [
          {
            rank: 1,
            rm_name: "Amit Sharma",
            client_count: 25,
            total_aum: "₹450 Cr",
            avg_portfolio: "₹18 Cr",
            performance_rating: "Excellent",
          },
          {
            rank: 2,
            rm_name: "Priya Patel",
            client_count: 18,
            total_aum: "₹320 Cr",
            avg_portfolio: "₹17.8 Cr",
            performance_rating: "Very Good",
          },
          {
            rank: 3,
            rm_name: "Rohit Singh",
            client_count: 12,
            total_aum: "₹280 Cr",
            avg_portfolio: "₹23.3 Cr",
            performance_rating: "Good",
          },
        ],
        metadata: {
          source: "enhanced_mock",
          query_type: "rm_performance_table",
          record_count: 3,
        },
      };
    }

    if (
      queryLower.includes("client profiles from mumbai") ||
      queryLower.includes("mumbai")
    ) {
      return {
        type: "table",
        data: [
          {
            name: "Shah Rukh Khan",
            age: 58,
            city: "Mumbai",
            profession: "Film Actor",
            risk_appetite: "Moderate",
            portfolio_value: "₹125 Cr",
          },
          {
            name: "Deepika Padukone",
            age: 38,
            city: "Mumbai",
            profession: "Film Actress",
            risk_appetite: "Conservative",
            portfolio_value: "₹87 Cr",
          },
          {
            name: "Rohit Sharma",
            age: 36,
            city: "Mumbai",
            profession: "Cricket Player",
            risk_appetite: "Moderate",
            portfolio_value: "₹65 Cr",
          },
          {
            name: "Alia Bhatt",
            age: 30,
            city: "Mumbai",
            profession: "Film Actress",
            risk_appetite: "High",
            portfolio_value: "₹45 Cr",
          },
        ],
        metadata: {
          source: "enhanced_mock",
          query_type: "mumbai_clients_table",
          record_count: 4,
        },
      };
    }

    if (queryLower.includes("highest holders")) {
      return {
        type: "table",
        data: [
          {
            client_name: "Shah Rukh Khan",
            stock_symbol: "RELIANCE",
            holding_value: "₹50 Cr",
            percentage_of_portfolio: "40%",
          },
          {
            client_name: "Virat Kohli",
            stock_symbol: "TCS",
            holding_value: "₹45 Cr",
            percentage_of_portfolio: "46%",
          },
          {
            client_name: "Priyanka Chopra",
            stock_symbol: "US_TECH",
            holding_value: "₹40 Cr",
            percentage_of_portfolio: "53%",
          },
          {
            client_name: "Hardik Pandya",
            stock_symbol: "TECH_STOCKS",
            holding_value: "₹25 Cr",
            percentage_of_portfolio: "42%",
          },
        ],
        metadata: {
          source: "enhanced_mock",
          query_type: "stock_holdings_table",
          record_count: 4,
        },
      };
    }
  }

  // TEXT RESPONSES - Analytical queries
  console.log("✅ Detected TEXT query");

  if (
    queryLower.includes("why") &&
    queryLower.includes("sports personalities") &&
    queryLower.includes("real estate")
  ) {
    return {
      type: "text",
      data: `**Why Sports Personalities Prefer Real Estate Investments:**

**Career Stability & Longevity Concerns:**
Sports careers are inherently shorter than traditional professions, typically spanning 10-15 years of peak earning potential. This creates unique investment needs:

• **Wealth Preservation**: Need for assets that maintain value beyond active career
• **Steady Income**: Real estate provides rental income during and after retirement  
• **Tangible Security**: Physical assets offer psychological comfort and control

**Risk Management Benefits:**
• **Lower Volatility**: Real estate markets are generally more stable than equity markets
• **Inflation Hedge**: Property values typically appreciate with inflation
• **Diversification**: Reduces overall portfolio risk when combined with other investments

**Tax Advantages:**
• **Depreciation Benefits**: Significant tax deductions available on property investments
• **Capital Gains Treatment**: Favorable long-term capital gains tax rates
• **1031 Exchanges**: Ability to defer taxes through property exchanges

**Celebrity Case Study - MS Dhoni:**
Our client MS Dhoni has allocated 51% of his ₹156 Cr portfolio to real estate, including:
- Agricultural land in Ranchi (₹80 Cr)
- Commercial properties in Chennai (₹45 Cr) 
- Residential properties in Mumbai (₹31 Cr)

This strategy has delivered consistent 12-15% annual returns while providing personal satisfaction through his farming interests.

**Industry Trends:**
65% of our sports personality clients have real estate allocations above 25%, compared to 18% for film industry clients who prefer more liquid investments.`,
      metadata: {
        source: "enhanced_mock",
        query_type: "sports_real_estate_analysis",
        analysis_depth: "comprehensive",
      },
    };
  }

  if (
    queryLower.includes("investment strategy") &&
    queryLower.includes("celebrity")
  ) {
    return {
      type: "text",
      data: `**Celebrity Investment Strategy Framework:**

**Unique Challenges in Celebrity Wealth Management:**

**Income Volatility & Career Uncertainty:**
• **Peak Earning Concentration**: Most celebrities earn 70-80% of lifetime income during 10-15 peak years
• **Industry Cyclicality**: Entertainment and sports industries face significant ups and downs
• **Career Risk**: Injury, scandal, or changing public preferences can end careers abruptly

**Our Strategic Asset Allocation Model:**

**Tier 1 - Core Holdings (60-70%):**
• **Blue-chip Stocks (25%)**: Reliance, TCS, HDFC Bank - stable, dividend-paying companies
• **Real Estate (20%)**: Mix of commercial and residential properties
• **Fixed Income (15%)**: Government bonds and high-grade corporate debt

**Tier 2 - Growth Investments (20-25%):**
• **International Equity (10%)**: US tech stocks, global diversification
• **Mutual Funds (8%)**: Professionally managed diversified portfolios
• **Sector-specific Investments (7%)**: Entertainment, sports, and related industries

**Tier 3 - Alternative Investments (10-15%):**
• **Private Equity (5%)**: Stakes in private companies and startups
• **Luxury Assets (3%)**: Art, collectibles, rare assets
• **Cryptocurrency (2%)**: Limited exposure for younger, tech-savvy clients

**Performance Results:**
- Average annual return: 12.5% (vs market 8.2%)
- Risk-adjusted Sharpe ratio: 1.8
- Client satisfaction: 94%
- Portfolio volatility: 11.2% (well-managed risk)`,
      metadata: {
        source: "enhanced_mock",
        query_type: "celebrity_strategy_analysis",
        analysis_depth: "comprehensive",
      },
    };
  }

  // Default text response
  return {
    type: "text",
    data: `**Comprehensive Wealth Management Analysis:**

Our AI-powered celebrity wealth management system has analyzed extensive portfolio data to provide strategic insights tailored to high-net-worth individuals in entertainment and sports.

**Portfolio Performance Overview:**
• **Total Assets Under Management**: ₹1,050+ Crores
• **Average Portfolio Size**: ₹19.1 Crores  
• **Year-to-Date Performance**: +12.5% (outperforming benchmark by 4.3%)
• **Client Satisfaction Score**: 94%

**Key Investment Principles:**
• **Diversification**: Strategic allocation across multiple asset classes and geographies
• **Risk Management**: Balanced approach between growth and capital preservation
• **Liquidity Management**: Maintaining sufficient liquid assets for lifestyle needs
• **Tax Efficiency**: Implementing structures to optimize after-tax returns

**Celebrity-Specific Considerations:**
• **Career Volatility**: Investment strategies adapted to irregular income patterns
• **Public Scrutiny**: Avoiding controversial or reputation-damaging investments
• **Lifestyle Requirements**: Balancing investment growth with liquidity needs
• **Succession Planning**: Long-term wealth preservation and transfer strategies`,
    metadata: {
      source: "enhanced_mock",
      query_type: "general_analysis",
      analysis_depth: "comprehensive",
    },
  };
};
