"use client"

import { useState } from "react"
import { Send, Loader2, AlertTriangle } from "lucide-react"
import "./QueryForm.css"

const QueryForm = ({ onSubmit, loading, disabled }) => {
  const [query, setQuery] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    if (query.trim() && !loading && !disabled) {
      onSubmit(query.trim())
    }
  }

  const sampleQueries = [
    "What are the top five portfolios of our wealth members?",
    "Give me the breakup of portfolio values per relationship manager",
    "Tell me the top relationship managers in my firm",
    "Which clients are the highest holders of stocks?",
    "Show me all client profiles from Mumbai",
    "What are the recent transactions for John Doe?",
    "List all clients with their risk appetite",
    "Show me portfolio distribution by asset type",
  ]

  const handleSampleQuery = (sampleQuery) => {
    if (!disabled) {
      setQuery(sampleQuery)
    }
  }

  return (
    <div className="query-form-container card">
      <div className="query-form-header">
        <h2>Ask Your Question</h2>
        <p>Query your wealth management data using natural language</p>
        {disabled && (
          <div className="connection-warning">
            <AlertTriangle size={16} />
            <span>Backend connection required to submit queries</span>
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="query-form">
        <div className="form-group">
          <label htmlFor="query">Your Question</label>
          <textarea
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g., What are the top five portfolios of our wealth members?"
            className="input textarea"
            disabled={loading || disabled}
          />
        </div>

        <button type="submit" className="btn btn-primary submit-btn" disabled={!query.trim() || loading || disabled}>
          {loading ? (
            <>
              <Loader2 size={16} className="spinner" />
              Processing...
            </>
          ) : (
            <>
              <Send size={16} />
              Submit Query
            </>
          )}
        </button>
      </form>

      <div className="sample-queries">
        <h3>Sample Queries</h3>
        <div className="sample-queries-grid">
          {sampleQueries.map((sampleQuery, index) => (
            <button
              key={index}
              onClick={() => handleSampleQuery(sampleQuery)}
              className="sample-query-btn"
              disabled={loading || disabled}
            >
              {sampleQuery}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}

export default QueryForm
