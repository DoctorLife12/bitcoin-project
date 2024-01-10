# Use a base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy source code to working directory
COPY serviceA.py /app

# Install Flask and requests module (used for HTTP requests)
RUN pip install flask requests

# Command to run the application
CMD ["python", "serviceA.py"]
