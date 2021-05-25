FROM python:3.9-slim
WORKDIR app

RUN pip install \
 Flask==1.1.2 \
 redis==3.5.3 \
 Flask_Injector==0.12.3 \
 'Werkzeug<2.0.0' \
 prometheus-client==0.10.1


ADD *.py ./
CMD python3 tracking.py --reload
