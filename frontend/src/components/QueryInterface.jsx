"use client"

import { useState } from "react"
import { Search, Sparkles, Play, BarChart3, FileText, Table } from "lucide-react"
import ResponseDisplay from "./ResponseDisplay"
import "./QueryInterface.css"

const QueryInterface = ({ onSubmit, loading, disabled, response, error }) => {
  const [query, setQuery] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    if (query.trim() && !loading && !disabled) {
      onSubmit({
        query: query.trim(),
      })
    }
  }

  // Categorized sample queries
  const sampleQueries = {
    charts: [
      "Give me the breakup of portfolio values per relationship manager",
      "Show me the asset allocation distribution across all portfolios",
      "What's the geographic distribution of our celebrity clients?",
      "Show me the risk appetite distribution among clients",
    ],
    tables: [
      "What are the top five portfolios of our wealth members?",
      "Tell me the top relationship managers in my firm",
      "Which clients are the highest holders of stocks?",
      "Show me all client profiles from Mumbai",
    ],
    text: [
      "Why do sports personalities prefer real estate investments?",
      "Explain the investment strategy for celebrity wealth management",
      "What are the emerging trends in celebrity portfolio management?",
      "How do we manage risk for high-profile client portfolios?",
    ],
  }

  const handleSampleQuery = (sampleQuery) => {
    if (!disabled) {
      setQuery(sampleQuery)
    }
  }

  const getQueryTypeIcon = (type) => {
    switch (type) {
      case "charts":
        return <BarChart3 size={16} />
      case "tables":
        return <Table size={16} />
      case "text":
        return <FileText size={16} />
      default:
        return null
    }
  }

  return (
    <div className="query-interface">
      <div className="query-section card">
        <div className="query-header">
          <div className="query-title">
            <Search size={24} />
            <h2>Natural Language Query Interface</h2>
          </div>
          <p className="query-description">
            Ask questions about celebrity portfolios, transactions, and performance in plain English. Get comprehensive
            responses with text summaries, data tables, and visual charts.
          </p>
        </div>

        <form onSubmit={handleSubmit} className="query-form">
          <div className="form-group">
            <label htmlFor="query" className="form-label">
              Enter Your Query:
            </label>
            <textarea
              id="query"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., Give me the breakup of portfolio values per relationship manager"
              className="query-input"
              disabled={loading || disabled}
              rows={4}
            />
          </div>

          <button type="submit" className="execute-button" disabled={!query.trim() || loading || disabled}>
            <Play size={20} />
            <Sparkles size={16} />
            Execute Query & Generate Response
          </button>
        </form>

        <div className="sample-queries">
          <h3>Sample Queries by Response Type:</h3>

          {Object.entries(sampleQueries).map(([type, queries]) => (
            <div key={type} className="query-category">
              <h4 className="category-title">
                {getQueryTypeIcon(type)}
                {type.charAt(0).toUpperCase() + type.slice(1)} Responses
              </h4>
              <div className="sample-grid">
                {queries.map((sampleQuery, index) => (
                  <button
                    key={index}
                    onClick={() => handleSampleQuery(sampleQuery)}
                    className={`sample-button ${type}-button`}
                    disabled={loading || disabled}
                  >
                    {sampleQuery}
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      <ResponseDisplay
        response={response}
        loading={loading}
        error={error}
        backendStatus={disabled ? "disconnected" : "connected"}
      />
    </div>
  )
}

export default QueryInterface
