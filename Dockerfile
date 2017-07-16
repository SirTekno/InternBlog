# This container is based off of the fantastic work of Jackie Lan which can be found here: https://github.com/JackieLan/djangocms-container

FROM ubuntu

MAINTAINER David Newswanger

# install build-essential, git
RUN apt-get update
RUN apt-get install -y build-essential git

# install python environment, pip, etc
RUN apt-get install -y python python-dev python-setuptools
RUN easy_install pip

# install nginx, supervisor
RUN apt-get install -y nginx
RUN apt-get install -y supervisor

# optional install for Pillow
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

# install uwsgi
RUN pip install uwsgi

RUN mkdir /django && mkdir /django/data && mkdir /django/app

ADD app/requirements.txt /django/app
RUN pip install -r /django/app/requirements.txt

ADD conf/* /django/
ADD app/ /django/app
ADD deployment/settings.py /django/app/newswangers

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /django/app.conf /etc/nginx/sites-enabled/
RUN ln -s /django/supervisord.conf /etc/supervisor/conf.d/

VOLUME ["/var/log/nginx"]
EXPOSE 80
CMD ["sh", "/django/run.sh"]
