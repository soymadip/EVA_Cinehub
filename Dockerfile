# Use an official Python image
FROM python:3.8-slim


# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Use start.sh to run the bot
CMD ["/bin/bash", "/start.sh"]
