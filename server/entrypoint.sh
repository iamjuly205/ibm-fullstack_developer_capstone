#!/bin/sh

set -e

# Build React frontend
echo "Building React frontend..."
cd frontend
npm install
CI=false npm run build
if [ ! -d "build" ]; then
    echo "React build failed - build directory not created"
    exit 1
fi
cd ..

echo "React build completed successfully"

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Setup completed successfully"
exec "$@"