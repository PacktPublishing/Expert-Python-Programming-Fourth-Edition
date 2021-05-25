FROM python:3.9-slim
WORKDIR app

RUN pip install \
 Flask==1.1.2 \
 redis==3.5.3 \
 Flask_Injector==0.12.3 \
 prometheus-client==0.10.1 \
 jaeger-client==4.4.0 \
 opentracing==2.4.0 \
 'Werkzeug<2.0.0' \
 Flask-OpenTracing==1.1.0

RUN pip install --no-deps redis_opentracing==1.0.0


ADD *.py ./
CMD python3 tracking.py --reload
