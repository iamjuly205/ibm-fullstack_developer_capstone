# Stage 1: Build React frontend
FROM node:18-alpine AS react-builder

WORKDIR /build

COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps

COPY frontend/public public
COPY frontend/src src

RUN npm run build

# Stage 2: Python Django application  
FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP=/app

WORKDIR $APP

# Install the requirements
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy Django app and all other necessary files
COPY djangoproj djangoproj
COPY djangoapp djangoapp
COPY database database
COPY manage.py .
COPY entrypoint.sh .

# Copy the built React app from the first stage
COPY --from=react-builder /build/build frontend/build
COPY --from=react-builder /build/public frontend/public

# Copy frontend static files
COPY frontend/static frontend/static

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]