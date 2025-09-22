# Python AI Editor API

A REST API that allows you to execute Python code with NumPy and Pandas libraries in a sandboxed environment.

## Features

- 🐍 **Python Code Execution**: Execute Python code with NumPy and Pandas via REST API
- 🚀 **Docker Ready**: Easy deployment with Docker and Docker Compose
- 🔒 **Sandboxed**: Safe code execution environment
- 📊 **Data Science Ready**: Pre-loaded with NumPy and Pandas
- 🔧 **API-First**: Backend-only deployment for integration with any frontend

## Quick Start

### Using Docker Compose (Recommended)

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd python-ai-editor
   ```

2. **Run with Docker Compose**

   ```bash
   # Development
   docker-compose up --build

   # Production
   docker-compose -f docker-compose.prod.yml up --build
   ```

3. **Test the API**

   ```bash
   # Health check
   curl http://localhost:5000/

   # Execute Python code
   curl -X POST http://localhost:5000/run \
     -H "Content-Type: application/json" \
     -d '{"code": "import numpy as np; print(np.array([1,2,3]))"}'
   ```

### Manual Docker Build

```bash
# Build the image
docker build -t python-ai-editor .

# Run the container
docker run -p 5000:5000 python-ai-editor
```

## Deployment in Coolify

### Option 1: Docker Compose Deployment

1. **Prepare your repository**

   - Ensure all files are committed to your Git repository
   - Make sure `docker-compose.yml` or `docker-compose.prod.yml` is in the root

2. **In Coolify**
   - Create a new project
   - Choose "Docker Compose" as the deployment method
   - Connect your Git repository
   - Coolify will automatically detect the `docker-compose.yml` file
   - Deploy!

### Option 2: Dockerfile Deployment

1. **In Coolify**
   - Create a new project
   - Choose "Dockerfile" as the deployment method
   - Connect your Git repository
   - Set the build context to the repository root
   - Use `Dockerfile.prod` for production deployments
   - Deploy!

### Environment Variables

You can set these environment variables in Coolify:

- `FLASK_ENV=production` (for production deployments)
- `PORT=5000` (default port, adjust if needed)

## Project Structure

```
python-ai-editor/
├── backend/
│   └── app.py              # Flask API application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Development Docker image
├── Dockerfile.prod        # Production Docker image
├── docker-compose.yml     # Development compose file
├── docker-compose.prod.yml # Production compose file
├── .dockerignore          # Docker ignore file
└── README.md              # This file
```

## API Endpoints

- `GET /` - Health check endpoint
  - Response: `{"status": "healthy", "message": "Python AI Editor API is running"}`
- `POST /run` - Executes Python code
  - Request body: `{"code": "your_python_code_here"}`
  - Response: `{"output": "execution_output"}`

## Available Libraries

The following Python libraries are available in the execution environment:

- **NumPy** (`numpy` as `np`) - Numerical computing
- **Pandas** (`pandas` as `pd`) - Data manipulation and analysis

## Security Considerations

⚠️ **Important**: This application executes arbitrary Python code. For production use:

1. Deploy behind a reverse proxy (nginx, Cloudflare, etc.)
2. Implement rate limiting
3. Consider adding authentication
4. Monitor resource usage
5. Use the production Dockerfile with Gunicorn for better performance

## Development

### Local Development

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**

   ```bash
   python backend/app.py
   ```

3. **Test the API**

   ```bash
   # Health check
   curl http://localhost:5000/

   # Execute Python code
   curl -X POST http://localhost:5000/run \
     -H "Content-Type: application/json" \
     -d '{"code": "import numpy as np; print(np.array([1,2,3]))"}'
   ```

### Building for Production

```bash
# Build production image
docker build -f Dockerfile.prod -t python-ai-editor:prod .

# Run production container
docker run -p 5000:5000 python-ai-editor:prod
```

## Troubleshooting

### Common Issues

1. **Port already in use**

   - Change the port in `docker-compose.yml` or use `-p 8080:5000` when running docker

2. **Build failures**

   - Ensure you have enough disk space
   - Check that all files are present in the repository

3. **Code execution errors**
   - Check the browser console for JavaScript errors
   - Verify the Flask application is running correctly

### Health Checks

The application includes health checks that verify the service is running correctly. You can check the health status:

```bash
# Check container health
docker ps

# View health check logs
docker inspect <container_id> | grep -A 10 Health
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
