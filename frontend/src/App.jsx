"use client"

import { useState, useEffect } from "react"
import MetricsCards from "./components/MetricsCards"
import QueryInterface from "./components/QueryInterface"
import ConnectionStatus from "./components/ConnectionStatus"
import { queryDatabase, checkHealth } from "./services/api"
import "./App.css"

function App() {
  const [response, setResponse] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [backendStatus, setBackendStatus] = useState("checking")

  // Detect if we're in v0 preview environment
  const isV0Preview =
    typeof window !== "undefined" &&
    (window.location.hostname.includes("v0.dev") ||
      window.location.hostname.includes("vercel.app") ||
      !window.location.hostname.includes("localhost"))

  // Check backend connection on component mount
  useEffect(() => {
    const checkBackendConnection = async () => {
      try {
        const healthy = await checkHealth()
        setBackendStatus(healthy ? "connected" : "disconnected")
      } catch (err) {
        setBackendStatus("disconnected")
      }
    }

    checkBackendConnection()

    // Only set up interval for localhost (not in preview)
    if (!isV0Preview) {
      const interval = setInterval(checkBackendConnection, 30000)
      return () => clearInterval(interval)
    }
  }, [isV0Preview])

  const handleQuery = async (queryData) => {
    setLoading(true)
    setError(null)
    setResponse(null)

    try {
      const result = await queryDatabase(queryData.query)
      if (result.error) {
        setError(result.error)
      } else {
        setResponse(result)
      }
    } catch (err) {
      setError(err.message || "Failed to process query. Please check if the backend is running.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <ConnectionStatus status={backendStatus} />

      <main className="main-content">
        <div className="container">
          <div className="hero-section">
            <h1 className="hero-title">Wealth Management AI Query System</h1>
            <p className="hero-subtitle">
              Natural language interface for querying client portfolios, transactions, and performance data across
              multiple data sources
            </p>
            {isV0Preview && (
              <div
                style={{
                  background: "rgba(255,255,255,0.2)",
                  padding: "8px 16px",
                  borderRadius: "8px",
                  marginTop: "12px",
                  fontSize: "14px",
                }}
              >
                🚀 Preview Mode: Using mock data for demonstration
              </div>
            )}
          </div>

          <MetricsCards />

          <QueryInterface
            onSubmit={handleQuery}
            loading={loading}
            disabled={backendStatus !== "connected"}
            response={response}
            error={error}
          />
        </div>
      </main>
    </div>
  )
}

export default App
