FROM python3.12:bullseye

WORKDIR /app

COPY svc/core-api /app/
COPY libs /app/
ADD svc/core-api/requirements.txt /app/


RUN python -m pip install requirements.txt

CMD [ "uvicorn" , "main:app" , "--host" , "0.0.0.0" , "--port" , "80" ]
