# 💸 WealthQuery AI  
_Natural Language Cross-Platform Data Query RAG Agent_  

[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)](https://fastapi.tiangolo.com/)  
[![React](https://img.shields.io/badge/React-Frontend-blue?logo=react)](https://reactjs.org/)  
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb)](https://www.mongodb.com/)  
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)](https://www.mysql.com/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-LLM-blueviolet?logo=openai)](https://platform.openai.com/)  

A full-stack application that enables business users to query multiple data sources using plain English and receive responses in **text**, **tables**, and **graphs**.  

---

## 📖 Table of Contents

- [🏗️ Architecture](#️architecture)
- [🚀 Quick Start](#-quick-start)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [📊 Sample Queries](#-sample-queries)
- [🔧 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🔌 API Endpoints](#-api-endpoints)
- [🛠️ Development](#️development)
  - [Adding New Queries](#adding-new-queries)
  - [Extending Response Types](#extending-response-types)
- [🔒 Security Notes](#-security-notes)
- [📈 Scaling Considerations](#-scaling-considerations)

---

## 🏗️ Architecture  

- **Frontend**: React + Vite  
- **Backend**: FastAPI + LangChain  
- **Databases**: 
  - MongoDB (client profiles)  
  - MySQL (transactions)  
- **AI**: OpenAI GPT for natural language processing  

---


---

## 📸 Screenshots

### 🖥️ Home Page  
 
Here’s what the application looks like:  

![Home Page 1](https://github.com/user-attachments/assets/878c443f-056f-458f-b2e6-7169500993c6)  
![Home Page 2](https://github.com/user-attachments/assets/b4d9178d-3830-49ad-a6f8-0476a401b1dd)  
![Home Page 3](https://github.com/user-attachments/assets/313047ea-a519-4316-9f90-04597ddcf956)  



---

# 🎥 Demo Video

[![WealthQuery Demo](https://drive.google.com/thumbnail?id=1CIY2orbcYA3d7wnP8D7EHPUlbvlqnoiQ)](https://drive.google.com/file/d/1CIY2orbcYA3d7wnP8D7EHPUlbvlqnoiQ/view?usp=drive_link)


Click the thumbnail above to watch on YouTube.

---

## 📂 Assets Folder

📁 Make sure to put your screenshots and video thumbnail in an **`assets/` folder** in the repo:  



## 🚀 Quick Start  

### 🖥 Backend Setup  

1. Navigate to the backend directory:  
   ```bash
   cd backend


## 🚀 Quick Start

### Backend Setup

1. Navigate to the backend directory:
\`\`\`bash
cd backend
\`\`\`

2. Install Python dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Set up environment variables in `.env`:
\`\`\`env
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=your_mongodb_connection_string
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=wealth_db
MONGO_DB=wealth_db
\`\`\`

4. Start the backend server:
\`\`\`bash
python run_server.py
\`\`\`

The backend will:
- Seed the databases with sample data
- Start the FastAPI server on http://localhost:8000

### Frontend Setup

1. Install Node.js dependencies:
\`\`\`bash

# 1. Go to frontend directory
cd frontend

# 2. Install all dependencies from package.json
npm install

# 3. Install any required libraries (in case they are missing)
npm install lucide-react axios tailwindcss chart.js react-chartjs-2

# 4. Start the development server
npm run dev



\`\`\`

2. Start the development server:
\`\`\`bash
npm run dev
\`\`\`

3. Open http://localhost:3000 in your browser

## 📊 Sample Queries

Try these natural language queries:

- "What are the top five portfolios of our wealth members?"
- "Give me the breakup of portfolio values per relationship manager"
- "Tell me the top relationship managers in my firm"
- "Which clients are the highest holders of stocks?"
- "Show me all client profiles from Mumbai"
- "What are the recent transactions for John Doe?"

## 🔧 Features

- **Natural Language Processing**: Query data using plain English
- **Multi-Database Support**: Connects to both MongoDB and MySQL
- **Multiple Response Formats**: Text, tables, and charts
- **Real-time Connection Status**: Shows backend connectivity
- **Professional UI**: Clean interface for wealth management
- **Error Handling**: Comprehensive error messages and recovery

## 📁 Project Structure

```text
├── backend/
│   ├── main.py              # FastAPI application
│   ├── langchain_agent.py   # LangChain AI agent
│   ├── formatter.py         # Response formatting
│   ├── run_server.py        # Server startup script
│   ├── db/
│   │   ├── mongo_connect.py # MongoDB connection
│   │   ├── mysql_connect.py # MySQL connection
│   │   └── seed_data.py     # Database seeding
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
├── src/
│   ├── components/          # React components
│   ├── services/            # API services
│   └── App.jsx              # Main application
├── package.json             # Node.js dependencies
└── README.md



## 🔌 API Endpoints

- `GET /health` - Health check
- `POST /query` - Process natural language queries

## 🛠️ Development

### Adding New Queries

The LangChain agent automatically handles new query types. The system uses:

1. **MongoDB Tool**: For client profile lookups
2. **MySQL Tool**: For portfolio and transaction queries
3. **OpenAI LLM**: For natural language understanding

### Extending Response Types

Add new response formatters in `backend/formatter.py` and corresponding React components in `src/components/`.

## 🔒 Security Notes

- Environment variables contain sensitive API keys
- Database connections use proper authentication
- CORS is configured for development (adjust for production)

## 📈 Scaling Considerations

- Add connection pooling for databases
- Implement caching for frequent queries
- Add rate limiting for API endpoints
- Consider using Redis for session management
