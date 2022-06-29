FROM python:3-alpine

RUN python -m pip install --upgrade pip

COPY opt/app.py /

ENTRYPOINT ["python", "/app.py"]