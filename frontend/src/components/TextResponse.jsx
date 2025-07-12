import { FileText } from "lucide-react"
import "./TextResponse.css"

const TextResponse = ({ data }) => {
  return (
    <div className="text-response">
      <div className="text-response-header">
        <FileText size={20} />
        <h3>Text Response</h3>
      </div>
      <div className="text-content">
        <pre>{data}</pre>
      </div>
    </div>
  )
}

export default TextResponse
