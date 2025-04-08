# MalwareSage

A comprehensive Malware Reverse Engineering Toolkit with both frontend and backend components.

## Project Structure

```
malwaresage/
├── Frontend/           # React-based frontend application
│   ├── src/           # Source code
│   ├── public/        # Static files
│   └── package.json   # Frontend dependencies
│
└── Backend/           # FastAPI-based backend application
    ├── routes/        # API routes
    ├── models/        # Database models
    ├── services/      # Business logic
    ├── utils/         # Utility functions
    └── main.py        # Application entry point
```

## Features

### Backend
- File upload and management
- Static analysis of PE/ELF files
- Dynamic analysis in sandbox environment
- ML-based malware classification
- Real-time log streaming via WebSockets
- JWT-based authentication
- MongoDB database integration
- Docker containerization

### Frontend
- Modern React-based UI
- Real-time analysis monitoring
- Interactive visualization of analysis results
- Secure file upload interface
- User authentication and management
- Responsive design

## Prerequisites

### Backend
- Python 3.9+
- MongoDB
- Docker (optional)
- Redis (for Celery tasks, optional)

### Frontend
- Node.js 16+
- npm or yarn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhishek-khadse/Sage-Sec.git
cd Sage-Sec
```

2. Backend Setup:
```bash
cd Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Frontend Setup:
```bash
cd Frontend
npm install
```

4. Configure Environment Variables:
- Create `.env` files in both Frontend and Backend directories
- See respective README files for required variables

## Running the Application

1. Start MongoDB:
```bash
# If using Docker
docker run -d -p 27017:27017 mongo
```

2. Start the Backend:
```bash
cd Backend
uvicorn main:app --reload
```

3. Start the Frontend:
```bash
cd Frontend
npm start
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Docker Deployment

1. Build and run the Backend:
```bash
cd Backend
docker build -t malwaresage-backend .
docker run -d -p 8000:8000 malwaresage-backend
```

2. Build and run the Frontend:
```bash
cd Frontend
docker build -t malwaresage-frontend .
docker run -d -p 3000:3000 malwaresage-frontend
```

## Security Considerations

1. Always use HTTPS in production
2. Keep your secret keys secure
3. Implement rate limiting
4. Validate all file uploads
5. Run dynamic analysis in isolated environments
6. Regularly update dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 