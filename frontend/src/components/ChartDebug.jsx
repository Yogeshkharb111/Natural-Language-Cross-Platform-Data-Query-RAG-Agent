import { Bug } from "lucide-react"

const ChartDebug = () => {
  return (
    <div className="chart-debug">
      <div className="debug-header">
        <Bug size={24} />
        <h2>Chart Debug</h2>
      </div>
      <div className="debug-content">
        <p>Chart debugging tools and diagnostics will be available here.</p>
      </div>
    </div>
  )
}

export default ChartDebug
