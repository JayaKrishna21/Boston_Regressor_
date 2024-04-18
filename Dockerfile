FROM python:3.11.7-bullseye

WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN pip install -r reqs.txt
CMD ["python3","app.py"]