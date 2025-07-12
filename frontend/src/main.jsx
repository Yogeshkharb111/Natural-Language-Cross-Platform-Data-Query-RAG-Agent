import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App.jsx"
import "./index.css"

// Safely get the container and mount the app
const container = document.getElementById("root")

if (container) {
  ReactDOM.createRoot(container).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
  )
} else {
  console.error('React root element with id="root" not found.')
}
