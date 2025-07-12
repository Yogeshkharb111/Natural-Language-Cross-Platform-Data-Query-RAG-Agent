import { CheckCircle, XCircle, Loader2 } from "lucide-react"
import "./ConnectionStatus.css"

const ConnectionStatus = ({ status }) => {
  const getStatusConfig = () => {
    switch (status) {
      case "connected":
        return {
          icon: <CheckCircle size={16} />,
          text: "Backend Connected",
          className: "status-connected",
        }
      case "disconnected":
        return {
          icon: <XCircle size={16} />,
          text: "Backend Disconnected",
          className: "status-disconnected",
        }
      case "checking":
      default:
        return {
          icon: <Loader2 size={16} className="spinner" />,
          text: "Checking Connection...",
          className: "status-checking",
        }
    }
  }

  const config = getStatusConfig()

  return (
    <div className={`connection-status ${config.className}`}>
      <div className="container">
        <div className="status-content">
          {config.icon}
          <span>{config.text}</span>
          {status === "disconnected" && (
            <span className="status-help">Make sure the backend server is running on port 8000</span>
          )}
        </div>
      </div>
    </div>
  )
}

export default ConnectionStatus
