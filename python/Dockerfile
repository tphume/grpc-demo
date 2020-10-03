FROM python:3.8.3

RUN mkdir server
WORKDIR server

COPY . .
RUN pip install -r requirements.txt

EXPOSE 50051
CMD ["python", "counter_server.py"]
