FROM python:3.10.4  

WORKDIR /PROJECT

ADD . /PROJECT

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]

