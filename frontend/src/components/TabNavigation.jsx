"use client"

import { Search, BarChart3, Bug, TestTube } from "lucide-react"
import "./TabNavigation.css"

const TabNavigation = ({ activeTab, onTabChange }) => {
  const tabs = [
    {
      id: "query",
      label: "Natural Language Query",
      icon: <Search size={18} />,
    },
    {
      id: "dashboard",
      label: "Portfolio Dashboard",
      icon: <BarChart3 size={18} />,
    },
    {
      id: "debug",
      label: "Chart Debug",
      icon: <Bug size={18} />,
    },
    {
      id: "test",
      label: "Chart Test",
      icon: <TestTube size={18} />,
    },
  ]

  return (
    <div className="tab-navigation">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() => onTabChange(tab.id)}
          className={`tab-button ${activeTab === tab.id ? "active" : ""}`}
        >
          {tab.icon}
          <span>{tab.label}</span>
        </button>
      ))}
    </div>
  )
}

export default TabNavigation
