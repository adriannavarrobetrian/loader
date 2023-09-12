FROM python:3.8
LABEL MAINTAINER adriannavarro

ENV AWS_REGION=eu-west-1
ENV SQS_URL=https://sqs.eu-west-1.amazonaws.com/646390474080/movies_to_parse
WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY movies.json main.py ./

CMD python main.py