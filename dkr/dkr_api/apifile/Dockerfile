# FROM python:3.8
# COPY . .
# RUN ls -a && pip install -r requirements.txt

# ARG ROOT_PASSWORD
# ARG USR_NAME

# ENV USER_NAME=$USR_NAME 
# ENV MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD 

# ENTRYPOINT [ "python", "app.py" ]

FROM python:3.8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY nginx.conf /etc/nginx/
COPY flask-site-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/

COPY . /app

WORKDIR /app

CMD ["/usr/bin/supervisord"]