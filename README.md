# Sage Sec

A comprehensive malware analysis platform that provides both static and dynamic analysis capabilities.

## Project Structure

```
Sage-Sec/
├── Frontend/                 # React frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API service functions
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
│
└── Backend/                 # FastAPI backend
    ├── routes/             # API route handlers
    ├── models/             # Database models
    ├── services/           # Business logic
    ├── utils/              # Utility functions
    └── main.py             # FastAPI application
```

## Features

### Backend (FastAPI)
- File upload and management
- Static analysis (PE file analysis, strings extraction)
- Dynamic analysis (sandbox execution)
- User authentication and authorization
- WebSocket support for real-time updates
- Docker support for easy deployment

### Frontend (React)
- Modern, responsive UI with Material-UI
- Real-time analysis monitoring
- Interactive analysis reports
- Secure file upload interface
- User authentication and management

## Prerequisites

- Python 3.8+
- Node.js 14+
- Docker (optional)
- PostgreSQL (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhishek-khadse/Sage-Sec.git
cd Sage-Sec
```

2. Set up the backend:
```bash
cd Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd ../Frontend
npm install
```

## Running the Application

1. Start the backend:
```bash
cd Backend
uvicorn main:app --reload
```

2. Start the frontend:
```bash
cd Frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Docker Deployment

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## Security Considerations

- All file uploads are scanned for malware before processing
- Secure file storage with access controls
- Rate limiting on API endpoints
- JWT-based authentication
- HTTPS support
- Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 