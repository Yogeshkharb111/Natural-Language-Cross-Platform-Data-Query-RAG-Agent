import { TrendingUp } from "lucide-react"
import "./Header.css"

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <TrendingUp size={32} className="logo-icon" />
            <div className="logo-text">
              <h1>WealthQuery AI</h1>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
