import { BarChart3 } from "lucide-react"
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement } from "chart.js"
import { Bar, Pie } from "react-chartjs-2"
import "./ChartResponse.css"

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ArcElement)

const ChartResponse = ({ data }) => {
  // Default chart options
  const defaultOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Data Visualization",
      },
    },
  }

  // If data is not in expected format, show error
  if (!data || !data.labels || !data.datasets) {
    return (
      <div className="chart-response">
        <div className="chart-response-header">
          <BarChart3 size={20} />
          <h3>Chart Response</h3>
        </div>
        <div className="chart-error">
          <p>Chart data is not in the expected format.</p>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      </div>
    )
  }

  const chartType = data.type || "bar"

  const renderChart = () => {
    switch (chartType.toLowerCase()) {
      case "pie":
        return <Pie data={data} options={defaultOptions} />
      case "bar":
      default:
        return <Bar data={data} options={defaultOptions} />
    }
  }

  return (
    <div className="chart-response">
      <div className="chart-response-header">
        <BarChart3 size={20} />
        <h3>Chart Response</h3>
        <span className="chart-type">{chartType.toUpperCase()}</span>
      </div>

      <div className="chart-container">{renderChart()}</div>
    </div>
  )
}

export default ChartResponse
