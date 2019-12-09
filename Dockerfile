# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
FROM python:3.7


WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENV VIRTUAL_ENV=/app
ENV PATH="$VIRTUAL_ENV/plateaubio/bin:$PATH"
RUN pip install gunicorn

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]