import { Loader2, AlertCircle, CheckCircle, Wifi, WifiOff } from "lucide-react"
import TextResponse from "./TextResponse"
import TableResponse from "./TableResponse"
import ChartResponse from "./ChartResponse"
import "./ResponseDisplay.css"

const ResponseDisplay = ({ response, loading, error, backendStatus }) => {
  const renderContent = () => {
    if (backendStatus === "disconnected") {
      return (
        <div className="backend-disconnected">
          <WifiOff size={48} />
          <h3>Backend Disconnected</h3>
          <p>Unable to connect to the backend server.</p>
          <div className="connection-help">
            <h4>To start the backend:</h4>
            <ol>
              <li>Navigate to the backend directory</li>
              <li>
                Install dependencies: <code>pip install -r requirements.txt</code>
              </li>
              <li>
                Set up your environment variables in <code>.env</code>
              </li>
              <li>
                Run: <code>python run_server.py</code>
              </li>
            </ol>
          </div>
        </div>
      )
    }

    if (loading) {
      return (
        <div className="loading-state">
          <Loader2 size={24} className="spinner" />
          <p>Processing your query with AI...</p>
          <small>This may take a few moments</small>
        </div>
      )
    }

    if (error) {
      return (
        <div className="error-state">
          <AlertCircle size={24} />
          <div>
            <h3>Query Error</h3>
            <p>{error}</p>
          </div>
        </div>
      )
    }

    if (!response) {
      return (
        <div className="empty-state">
          <div className="empty-icon">🤖</div>
          <h3>Ready for Your Query</h3>
          <p>Enter a natural language question about your wealth management data to get started.</p>
          <div className="features-list">
            <div className="feature">
              <CheckCircle size={16} />
              <span>MongoDB client profiles</span>
            </div>
            <div className="feature">
              <CheckCircle size={16} />
              <span>MySQL transaction data</span>
            </div>
            <div className="feature">
              <CheckCircle size={16} />
              <span>AI-powered analysis</span>
            </div>
          </div>
        </div>
      )
    }

    // Render based on response type
    switch (response.type) {
      case "table":
        return <TableResponse data={response.data} />
      case "chart":
        return <ChartResponse data={response.data} />
      case "text":
      default:
        return <TextResponse data={response.data} />
    }
  }

  return (
    <div className="response-display card">
      <div className="response-header">
        <h2>Query Results</h2>
        <div className="header-status">
          {backendStatus === "connected" && (
            <div className="connection-indicator">
              <Wifi size={16} />
              <span>Connected</span>
            </div>
          )}
          {response && !loading && !error && backendStatus === "connected" && (
            <div className="success-indicator">
              <CheckCircle size={16} />
              <span>Query completed</span>
            </div>
          )}
        </div>
      </div>

      <div className="response-content">{renderContent()}</div>
    </div>
  )
}

export default ResponseDisplay
