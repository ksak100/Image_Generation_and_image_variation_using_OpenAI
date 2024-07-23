FROM python:3.9.18

WORKDIR /app/

COPY . ./

RUN pip install -r requirements.txt

RUN pip install python-dotenv

EXPOSE 5000

CMD python app.py