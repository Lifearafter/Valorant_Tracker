FROM python:3.10.5-alpine
WORKDIR /VALORANT_TRACKER

COPY requirements.txt requirements.txt

COPY ./code/discordUI.py /VALORANT_TRACKER/discordUI.pyhttps://github.com/Lifearafter/Valorant_Tracker/tree/master/Docker
COPY ./code/matchhistory.py /VALORANT_TRACKER/matchhistory.py

ENV TOKEN=

RUN pip install -r requirements.txt

CMD ["python", "discordUI.py"]
