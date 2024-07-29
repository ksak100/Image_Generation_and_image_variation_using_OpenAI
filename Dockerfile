FROM python:3.9.18

WORKDIR /app/

COPY . ./

RUN pip install -r requirements.txt

RUN pip install python-dotenv

EXPOSE 8080

CMD python main.py