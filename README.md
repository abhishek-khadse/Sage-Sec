# MalwareSage Backend

A secure, scalable backend API for MalwareSage, a Malware Reverse Engineering Toolkit. This backend provides REST and WebSocket endpoints for managing and analyzing uploaded malware samples using both static and dynamic techniques.

## Features

- File upload and management
- Static analysis of PE/ELF files
- Dynamic analysis in sandbox environment
- ML-based malware classification
- Real-time log streaming via WebSockets
- JWT-based authentication
- MongoDB database integration
- Docker containerization

## Prerequisites

- Python 3.9+
- MongoDB
- Docker (optional)
- Redis (for Celery tasks, optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/malwaresage.git
cd malwaresage/Backend
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

4. Create a `.env` file with the following variables:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=malwaresage
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
UPLOAD_DIR=uploads
VIRUSTOTAL_API_KEY=your-virustotal-api-key
```

## Running the Application

1. Start MongoDB:
```bash
# If using Docker
docker run -d -p 27017:27017 mongo

# Or start your local MongoDB instance
```

2. Run the FastAPI application:
```bash
uvicorn main:app --reload
```

3. Access the API documentation at:
```
http://localhost:8000/docs
```

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t malwaresage-backend .
```

2. Run the container:
```bash
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/uploads:/app/uploads \
  -e MONGODB_URL=mongodb://host.docker.internal:27017 \
  -e DATABASE_NAME=malwaresage \
  -e SECRET_KEY=your-secret-key \
  malwaresage-backend
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user information

### File Management
- `POST /api/files/upload` - Upload a malware sample
- `GET /api/files` - List all uploaded files
- `DELETE /api/files/{id}` - Delete a sample
- `GET /api/files/{id}` - Get file information

### Analysis
- `POST /api/analyze/static` - Run static analysis
- `GET /api/analyze/static/{id}` - Get static analysis results
- `POST /api/analyze/dynamic` - Start dynamic analysis
- `GET /api/analyze/dynamic/{id}` - Get dynamic analysis results

### Classification
- `POST /api/classify` - Run ML classification
- `GET /api/classify/{id}` - Get classification results

### WebSocket
- `ws:///ws/logs/{file_id}` - Real-time analysis logs
- `ws:///ws/alerts` - Real-time alerts

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