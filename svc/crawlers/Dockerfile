FROM python:3.12-bullseye

WORKDIR /app

COPY libs /app/libs

ADD svc/crawlers/requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY svc/crawlers /app/

CMD [ "scrapy", "crawl", "tsn.ua", "-s", "JOBDIR=crawls/tsn_spider" ]
