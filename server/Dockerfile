FROM python:3.8-buster
RUN apt-get update && \
  apt-get -y install binutils libproj-dev gdal-bin && \
  rm -rf /var/lib/apt/lists/* && \
  apt-get clean
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /app
CMD ["python3", "manage.py", "runserver", "8000"]