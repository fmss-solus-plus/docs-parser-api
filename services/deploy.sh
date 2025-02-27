cd ~/docs-parser-api
 
# Fetch latest changes from GitHub
git fetch origin dev-server
git reset --hard origin/dev-server
 
# Activate virtual environment
source .venv/bin/activate
 
# Move to backend directory
cd backend
 
# Set environment variable
export APP_ENV=dev
 
# Apply database migrations
python manage.py makemigrations
python manage.py migrate
 






