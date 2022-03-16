FROM python:latest
COPY . /opt/app
WORKDIR /opt/app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]