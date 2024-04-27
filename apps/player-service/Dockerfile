# Use an official Python runtime as a parent image
FROM --platform=$BUILDPLATFORM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATA_ROOT /usr/src/app/data
ENV SERVER_PORT 8000

EXPOSE 8000

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Run the application using Poetry
CMD ["poetry", "run", "start"]
