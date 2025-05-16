# 🧠 Sentiment Analyzer - FastAPI Microservice

![CI Status](https://github.com/poudelsaroj/sentiment/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue)

A simple FastAPI-based microservice that performs sentiment analysis on user input text. Built with the 12-Factor App principles in mind.

---

## 🚀 Features

- REST API for sentiment analysis
- Docker & Docker Compose support
- Clean project structure
- GitHub Actions CI with test/lin
t steps
- Environment-based configuration using Pydantic
- Pytest test coverage
- Pre-commit hooks

---
# video link 
https://drive.google.com/file/d/1RYYYm85OvJI-NZPoqh_JMXbNyC3dPTV2/view?usp=sharing
## 📋 API Documentation

### Endpoints

- `GET /` - Health check endpoint
- `GET /ping` - Simple ping endpoint
- `POST /api/v1/analyze` - Sentiment analysis endpoint

### Sentiment Analysis Example

**Request:**
```json
POST /api/v1/analyze
{
  "text": "I love working on this project!"
}
```

**Response:**
```json
{
  "sentiment": "positive"
}
```

Full API documentation available at `/docs` or `/redoc` when the service is running.

---

## 🛠 Installation & Setup

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/poudelsaroj/sentiment-analysis.git
cd sentiment-analysis
```

2. Run with Docker Compose:
```bash
docker-compose up --build
```

3. Access the API at http://localhost:8000

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/poudelsaroj/sentiment-analysis.git
cd sentiment-analysis
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```
MODEL_NAME=sentiment-analysis-model
ENV=development
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

6. Access the API at http://localhost:8000

---

## 🧪 Testing

Run the test suite:

```bash
# From project root with PYTHONPATH set
PYTHONPATH=. pytest

# Or with pytest directly
python -m pytest
```

---

## 📁 Project Structure

```
.
├── .github/workflows   # CI/CD configuration
├── app/                # Application code
│   ├── api/            # API routes and controllers 
│   ├── core/           # Core functionality (config, etc)
│   ├── models/         # Data models and business logic
│   └── main.py         # Application entry point
├── tests/              # Test files
├── .env                # Environment variables
├── docker-compose.yml  # Docker compose configuration
├── Dockerfile          # Docker build instructions
└── requirements.txt    # Python dependencies
```

---

## 📝 License

MIT

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
