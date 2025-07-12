import { BarChart3, PieChart, TrendingUp } from "lucide-react"
import "./PortfolioDashboard.css"

const PortfolioDashboard = () => {
  return (
    <div className="portfolio-dashboard">
      <div className="dashboard-header">
        <BarChart3 size={24} />
        <h2>Portfolio Dashboard</h2>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-card">
          <div className="card-header">
            <PieChart size={20} />
            <h3>Asset Allocation</h3>
          </div>
          <div className="card-content">
            <p>Interactive portfolio allocation charts and breakdowns will be displayed here.</p>
          </div>
        </div>

        <div className="dashboard-card">
          <div className="card-header">
            <TrendingUp size={20} />
            <h3>Performance Metrics</h3>
          </div>
          <div className="card-content">
            <p>Real-time performance data and analytics will be shown here.</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default PortfolioDashboard
