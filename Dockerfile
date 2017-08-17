FROM python:alpine3.6
COPY . .
CMD ["python", "yow.py"]
EXPOSE 8080
