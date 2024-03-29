FROM python:3.10.5-alpine
WORKDIR /VALORANT_TRACKER

COPY requirements.txt requirements.txt

COPY ./code/discordUI.py /VALORANT_TRACKER/discordUI.py
COPY ./code/matchhistory.py /VALORANT_TRACKER/matchhistory.py

ARG Token

ENV TOKEN = ${Token}

RUN pip install -r requirements.txt

CMD ["python", "discordUI.py"]
