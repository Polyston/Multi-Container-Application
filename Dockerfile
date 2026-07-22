# A 3.12 python runtime is used as a parent image
FROM python:3.12-slim

# Sets the working directory in the Docker container
WORKDIR /app

# requirements.txt is copied into the working directory
COPY requirements.txt .

# The dependencies listed in requirements.txt are downloaded
RUN pip install --no-cache-dir -r requirements.txt

# The current directory is copied into the working directory
COPY . .

# Sets the port used by the container
EXPOSE 8000

# Starts the uvicorn server for the todo list 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]