# Use a slim Python image
FROM python:3.13-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install Poetry
RUN pip install --upgrade pip setuptools poetry


# Set work directory
WORKDIR /app

# Install system dependencies for building packages (optional but useful)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
# RUN poetry install --only main
# No prompts, no color CLI, API; so no package
RUN poetry install --no-interaction --no-ansi --no-root



# Copy the rest of the code
COPY dashApi/ /app/dashApi/

# Expose port
EXPOSE 8000

# Run the application with Uvicorn
CMD ["uvicorn", "dashApi.main:app", "--host", "0.0.0.0", "--port", "8000"]
