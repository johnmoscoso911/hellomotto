FROM python:3.7

RUN pip install --upgrade pip
RUN pip install email-validator python-multipart pyjwt
RUN pip install fastapi uvicorn pytz passlib pydantic

EXPOSE 7001

COPY ./app /app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7001" ]