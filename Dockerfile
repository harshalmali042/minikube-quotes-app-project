# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy app code
COPY app/ /app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
