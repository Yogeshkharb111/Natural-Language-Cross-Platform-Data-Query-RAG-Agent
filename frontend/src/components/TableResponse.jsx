import { TableIcon } from "lucide-react"
import "./TableResponse.css"

const TableResponse = ({ data }) => {
  if (!Array.isArray(data) || data.length === 0) {
    return (
      <div className="table-response">
        <div className="table-response-header">
          <TableIcon size={20} />
          <h3>Table Response</h3>
        </div>
        <p>No data available to display in table format.</p>
      </div>
    )
  }

  const columns = Object.keys(data[0])

  return (
    <div className="table-response">
      <div className="table-response-header">
        <TableIcon size={20} />
        <h3>Table Response</h3>
        <span className="record-count">{data.length} records</span>
      </div>

      <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              {columns.map((column) => (
                <th key={column}>{column.replace(/_/g, " ").replace(/\b\w/g, (l) => l.toUpperCase())}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                {columns.map((column) => (
                  <td key={column}>{row[column] !== null && row[column] !== undefined ? String(row[column]) : "-"}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default TableResponse
