FROM python:3.9.20-slim

ARG TZ=UTC
ENV TZ ${TZ}

WORKDIR /src
COPY ./requirements.txt .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]