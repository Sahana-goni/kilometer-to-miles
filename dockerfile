FROM python:3.13.7
WORKDIR / kmtom
COPY . .
RUN pip install
CMD ["python","dockerstu.py"]