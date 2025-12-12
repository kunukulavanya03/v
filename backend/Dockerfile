FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port 8000 for the web interface
EXPOSE 8000

# Run the command to start the development server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]