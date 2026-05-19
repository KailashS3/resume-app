FROM python:3.11-slim

WORKDIR /app

# Install build tools and libraries needed for pycairo/xhtml2pdf
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libcairo2 \
    libcairo2-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install flask xhtml2pdf

EXPOSE 8080

CMD ["python", "app.py"]

