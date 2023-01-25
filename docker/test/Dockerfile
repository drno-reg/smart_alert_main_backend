    # pull official base image
FROM python:3.9.4-alpine

# set work directory
COPY . /app

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#change timezone on Moskow
#ENV TZ=Europe/Moscow
#RUN apk update && apk add --no-cache --virtual tzdata
#RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#change timezone on Moskow
#ENV TZ=Europe/Moscow
#RUN apk update add tzdata && cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && apk del tzdata

RUN apk update && apk add tzdata
ENV TZ=Europe/Moscow

# copy requirements file

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
        busybox-extras iputils \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements-test.txt \
    && rm -rf /root/.cache/pip

RUN chmod a+x ./docker/test/entrypoint.sh
COPY ./docker/test/entrypoint.sh /app

ENTRYPOINT ["/app/entrypoint.sh"]