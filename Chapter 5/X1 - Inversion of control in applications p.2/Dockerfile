FROM python:3.9-slim
WORKDIR app

RUN pip install \
 Flask==1.1.2 \
 redis==3.5.3


ADD *.py ./
CMD python3 tracking.py --reload