# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
FROM python:3.7

RUN useradd -ms /bin/bash plateaubio
WORKDIR /opt/plateaubio
RUN chown plateaubio:plateaubio /opt/plateaubio -R 
USER plateaubio

COPY --chown=plateaubio:plateaubio requirements.txt .

RUN pip install --user -r requirements.txt

COPY --chown=plateaubio:plateaubio . .

ENV PATH="/home/plateaubio/.local/bin/:$PATH"

RUN pip install --user gunicorn

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]