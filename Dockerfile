# Base image (Python 3.9 slim)
FROM python:3.9-slim

# System dependencies install karein
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome install karein
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# ChromeDriver install karein (yahan CHROMEDRIVER_VERSION ko apne Chrome version ke hisaab se update karein)
ARG CHROMEDRIVER_VERSION=114.0.5735.90
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

# Python dependencies install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Apni script copy karein
COPY update_nicknames.py .

# Environment variable (optional)
ENV CHROME_OPTS="--headless --disable-gpu --no-sandbox"

# Container start hone par script run ho
CMD ["python", "update_nicknames.py"]

