import { Users, DollarSign, TrendingUp, UserCheck } from "lucide-react"
import "./MetricsCards.css"

const MetricsCards = () => {
  const metrics = [
    {
      title: "Total Clients",
      value: "150+",
      icon: <Users size={24} />,
      color: "blue",
    },
    {
      title: "AUM",
      value: "₹15,000 Cr",
      icon: <DollarSign size={24} />,
      color: "green",
    },
    {
      title: "Avg Return",
      value: "12.5%",
      icon: <TrendingUp size={24} />,
      color: "purple",
    },
    {
      title: "Active RMs",
      value: "25",
      icon: <UserCheck size={24} />,
      color: "orange",
    },
  ]

  return (
    <div className="metrics-grid">
      {metrics.map((metric, index) => (
        <div key={index} className={`metric-card metric-${metric.color}`}>
          <div className="metric-icon">{metric.icon}</div>
          <div className="metric-content">
            <div className="metric-title">{metric.title}</div>
            <div className="metric-value">{metric.value}</div>
          </div>
        </div>
      ))}
    </div>
  )
}

export default MetricsCards
