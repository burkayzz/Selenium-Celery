FROM python:3.12.2
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libappindicator1 \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    gnupg2 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxtst6 \
    libxinerama1 \
    libcups2 \
    libdbus-1-3 \
    libfontconfig1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libasound2



RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable=126.0.6478.126-1


RUN wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chromedriver-win64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver-win64/ \
    && rm /tmp/chromedriver.zip

RUN google-chrome --version
RUN wget -q -O /usr/bin/xvfb-chrome https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip \
      && chmod +x /usr/bin/xvfb-chrome


WORKDIR /app
COPY requirements.txt /app/
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
ENV DJANGO_SETTINGS_MODULE=otonom.settings
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["python", "manage.py", ,"runserver","0.0.0.0:8000", "otonom.wsgi:application"]