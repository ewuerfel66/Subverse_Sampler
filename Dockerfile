FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1

### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Copy test.py from the local directory
RUN mkdir c:\home
RUN mkdir c:\home\data
COPY scraper.py /home
COPY scrapers.py /home
COPY sections.py /home

### Import Data
### COPY Data /home/data

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv && \
  pip3 install pandas && \
  pip3 install bs4