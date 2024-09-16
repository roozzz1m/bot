# Используем базовый образ Python
FROM python:latest

WORKDIR /root/bot/

COPY . .

RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps 

CMD [ "bash", "-c", "python bot.py" ]
