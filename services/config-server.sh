# Activate virtual environment
source .venv/bin/activate
 
# Move to backend directory
cd backend

# Set environment variable
export APP_ENV=dev
 
# Stop any existing Django processes (optional)
pkill -f "gunicorn --bind 0.0.0.0:8000"
 
# Start Django server in the background
echo "Deployment completed!"

gunicorn --workers=1 --timeout=120 --max-requests=500 --max-requests-jitter=50 --bind 0.0.0.0:8000 backend.wsgi:application


