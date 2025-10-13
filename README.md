# 🧠 Datalyze

**Intelligent Data-Pipeline Visualizer & Auto-EDA Platform**

Datalyze is an intelligent data-pipeline visualizer that automates exploratory data analysis (EDA) and guided model experimentation. Built using FastAPI, React, D3.js, and scikit-learn — fully containerized and deployable via Docker and AWS ECS.

## 🚀 Features

- **Automated EDA**: Generate comprehensive dataset summaries and correlations
- **Pipeline Visualization**: Interactive D3.js visualizations of data processing stages
- **Auto-Modeling**: Guided model experimentation with scikit-learn
- **Real-time Processing**: Background task execution with Celery and Redis
- **Cloud Ready**: Docker containerization with AWS ECS deployment
- **Modern UI**: React-based frontend with responsive design

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend │    │  FastAPI Backend │    │   PostgreSQL    │
│   (D3.js viz)   │◄──►│  (Python 3.10+) │◄──►│   (Production)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │  Celery + Redis │
                       │ (Background Jobs)│
                       └─────────────────┘
```

## ⚙️ Tech Stack

### Backend Stack

| Component | Library | Purpose |
|-----------|---------|---------|
| **Web Framework** | `fastapi` | REST API for uploads, ETL stages, AutoModel endpoints |
| **Server** | `uvicorn[standard]` | ASGI server for FastAPI |
| **Async Tasks** | `celery + redis` | Background execution for EDA/AutoModel jobs |
| **ORM / DB** | `sqlalchemy + psycopg2` | Pipeline metadata, metrics, model logs |
| **Database** | `PostgreSQL` (prod) / `SQLite` (dev) | Persistent data store |
| **Data Handling** | `pandas, numpy` | Data cleaning, transformation, feature extraction |
| **Auto-EDA** | `ydata-profiling` | Generate dataset summaries & correlations |
| **ML / Modeling** | `scikit-learn` | Regression, classification, evaluation metrics |
| **Visualization** | `matplotlib, seaborn, plotly` | Create stage plots & feature charts |
| **File Uploads** | `python-multipart, boto3` | CSV upload handling, S3 integration |
| **Serialization** | `pydantic` | Data validation for API models |
| **Logging** | `loguru` | Structured backend logs |
| **Packaging** | `joblib` | Save / load trained models |

### Frontend Stack

| Component | Library | Purpose |
|-----------|---------|---------|
| **Framework** | `React 18` | Modern UI framework |
| **Visualization** | `D3.js` | Interactive data visualizations |
| **HTTP Client** | `axios` | API communication |
| **State Management** | `Redux Toolkit` | Global state management |
| **Styling** | `Tailwind CSS` | Utility-first CSS framework |
| **Build Tool** | `Vite` | Fast build tool and dev server |
| **Type Safety** | `TypeScript` | Type-safe JavaScript |

### DevOps & Deployment

| Component | Tool | Purpose |
|-----------|------|---------|
| **Containerization** | `Docker` | Application containerization |
| **Orchestration** | `Docker Compose` | Local development environment |
| **Cloud Platform** | `AWS ECS` | Production deployment |
| **Database** | `AWS RDS PostgreSQL` | Managed database service |
| **Storage** | `AWS S3` | File storage and model artifacts |
| **Monitoring** | `AWS CloudWatch` | Application monitoring |

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/Datalyze.git
   cd Datalyze
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Database Setup**
   ```bash
   # Using Docker Compose
   docker-compose up -d postgres redis
   
   # Or set up PostgreSQL manually
   createdb Datalyze
   ```

5. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   uvicorn app.main:app --reload
   
   # Terminal 2: Frontend
   cd frontend
   npm run dev
   
   # Terminal 3: Celery Worker (optional)
   cd backend
   celery -A app.celery worker --loglevel=info
   ```

7. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
Datalyze/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Core configuration
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utility functions
│   ├── tests/              # Backend tests
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   ├── store/          # Redux store
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   ├── package.json        # Node dependencies
│   └── Dockerfile          # Frontend container
├── docker-compose.yml      # Local development
├── docker-compose.prod.yml # Production deployment
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔧 Development

### Backend Development

```bash
cd backend
# Install dependencies
pip install -r requirements.txt

# Run with hot reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest

# Run linting
black app/
flake8 app/
```

### Frontend Development

```bash
cd frontend
# Install dependencies
npm install

# Run development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

### Database Migrations

```bash
cd backend
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

## 🐳 Docker Deployment

### Local Development

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Deployment

```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy to AWS ECS
# (Configure AWS CLI and ECS CLI)
```

## 📊 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

- `POST /api/upload` - Upload CSV files
- `GET /api/pipelines` - List data pipelines
- `POST /api/pipelines/{id}/eda` - Generate EDA report
- `POST /api/models/train` - Train ML models
- `GET /api/visualizations/{id}` - Get visualization data

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm test
```

### Integration Tests
```bash
# Run with Docker Compose
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

## 📈 Monitoring & Logging

- **Application Logs**: Structured logging with Loguru
- **Performance**: AWS CloudWatch metrics
- **Health Checks**: `/health` endpoint for load balancer
- **Error Tracking**: Integrated error reporting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [Wiki](https://github.com/your-org/Datalyze/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-org/Datalyze/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/Datalyze/discussions)

## 🗺️ Roadmap

- [ ] Advanced ML model selection
- [ ] Real-time data streaming support
- [ ] Multi-tenant architecture
- [ ] Advanced visualization types
- [ ] Model versioning and A/B testing
- [ ] Integration with popular ML platforms

---

**Built with ❤️ by the Datalyze Team**
