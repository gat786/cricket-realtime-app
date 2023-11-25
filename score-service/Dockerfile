# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Run the application using Poetry
CMD ["poetry", "run", "start"]
