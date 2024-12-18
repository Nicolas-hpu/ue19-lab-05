
FROM python:3.10


WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]