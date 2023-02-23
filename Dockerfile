FROM python:3.9
WORKDIR /var/www/html
ADD requirements.txt /var/www/html
RUN pip install -r /var/www/html/requirements.txt

EXPOSE 8082