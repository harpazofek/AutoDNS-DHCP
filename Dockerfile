FROM python:3.9
WORKDIR /AutuDNS
COPY . .
RUN pip install -r requirement.txt
CMD [ "python3", "main.py" ]
