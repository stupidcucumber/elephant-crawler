FROM python:3.12-bullseye

WORKDIR /app

COPY libs /app/libs

ADD svc/core-api/requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY svc/core-api /app/

CMD [ "uvicorn" , "main:app" , "--host" , "0.0.0.0" , "--port" , "80" ]
