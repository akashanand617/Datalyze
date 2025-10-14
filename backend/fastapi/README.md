# Datalyze FastAPI Backend

FastAPI backend for the Datalyze intelligent data-pipeline visualizer.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📁 Project Structure

```
backend/fastapi/
├── app/
│   ├── api/                 # API route handlers
│   │   ├── health.py       # Health check endpoints
│   │   ├── uploads.py      # File upload endpoints
│   │   ├── pipelines.py    # Pipeline management
│   │   ├── models.py       # ML model endpoints
│   │   └── visualizations.py # Visualization endpoints
│   ├── core/               # Core configuration
│   │   └── config.py       # Application settings
│   ├── models/             # Database models (future)
│   ├── services/           # Business logic (future)
│   ├── utils/              # Utility functions (future)
│   └── main.py             # FastAPI application
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
└── README.md              # This file
```

## 🔧 Development

### Run with hot reload
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run tests
```bash
pytest tests/ -v
```

### Code formatting
```bash
black app/
flake8 app/
```

## 📊 API Endpoints

### Health Check
- `GET /api/v1/health` - Basic health check
- `GET /api/v1/health/detailed` - Detailed system status
- `GET /api/v1/health/ready` - Readiness check
- `GET /api/v1/health/live` - Liveness check

### File Uploads
- `POST /api/v1/upload` - Upload single file
- `POST /api/v1/upload/batch` - Upload multiple files
- `GET /api/v1/upload/{file_id}` - Get upload status
- `DELETE /api/v1/upload/{file_id}` - Delete uploaded file
- `GET /api/v1/uploads` - List all uploads
- `GET /api/v1/upload/{file_id}/preview` - Preview file data
- `GET /api/v1/upload/{file_id}/metadata` - Get file metadata
- `POST /api/v1/upload/{file_id}/validate` - Validate file

### Pipelines
- `GET /api/v1/pipelines` - List pipelines
- `POST /api/v1/pipelines` - Create pipeline
- `GET /api/v1/pipelines/{pipeline_id}` - Get pipeline details
- `PUT /api/v1/pipelines/{pipeline_id}` - Update pipeline
- `DELETE /api/v1/pipelines/{pipeline_id}` - Delete pipeline
- `POST /api/v1/pipelines/{pipeline_id}/execute` - Execute pipeline
- `GET /api/v1/pipelines/{pipeline_id}/status` - Get execution status
- `POST /api/v1/pipelines/{pipeline_id}/eda` - Generate EDA report

### Models
- `POST /api/v1/models/train` - Train ML model
- `GET /api/v1/models` - List models
- `GET /api/v1/models/{model_id}` - Get model details
- `POST /api/v1/models/{model_id}/predict` - Make predictions
- `GET /api/v1/models/{model_id}/performance` - Get performance metrics
- `POST /api/v1/models/{model_id}/evaluate` - Evaluate model
- `DELETE /api/v1/models/{model_id}` - Delete model

### Visualizations
- `GET /api/v1/visualizations/{visualization_id}` - Get visualization
- `POST /api/v1/visualizations` - Create visualization
- `GET /api/v1/visualizations` - List visualizations
- `PUT /api/v1/visualizations/{visualization_id}` - Update visualization
- `DELETE /api/v1/visualizations/{visualization_id}` - Delete visualization
- `GET /api/v1/visualizations/{visualization_id}/data` - Get visualization data
- `GET /api/v1/visualizations/{visualization_id}/image` - Get as image
- `GET /api/v1/visualizations/{visualization_id}/svg` - Get as SVG

## 🐳 Docker

### Build image
```bash
docker build -t datalyze-fastapi .
```

### Run container
```bash
docker run -p 8000:8000 datalyze-fastapi
```

## 🔮 Future Enhancements

- [ ] Database integration (SQLAlchemy + PostgreSQL)
- [ ] Redis integration for caching
- [ ] Celery integration for background tasks
- [ ] Authentication and authorization
- [ ] File storage (AWS S3)
- [ ] Data processing (pandas, numpy)
- [ ] ML model training (scikit-learn)
- [ ] EDA generation (ydata-profiling)
- [ ] Visualization generation (matplotlib, plotly)
