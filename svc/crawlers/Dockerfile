FROM python3.12:bullseye

WORKDIR /app

COPY svc/crawlers /app/
COPY libs /app/
ADD svc/crawlers/requirements.txt /app/


RUN python -m pip install requirements.txt

CMD [ "python" , "main.py" ]
