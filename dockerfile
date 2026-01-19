FROM python:3.13.7
WORKDIR / kmtom
COPY . .
CMD ["python","dockerstu.py"]