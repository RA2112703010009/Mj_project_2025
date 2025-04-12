FROM python:alpine AS stage

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose HTTPS port
EXPOSE 443

# Use Gunicorn in container by default
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:443", "--certfile=certs/cert.pem", "--keyfile=certs/key.pem"]
