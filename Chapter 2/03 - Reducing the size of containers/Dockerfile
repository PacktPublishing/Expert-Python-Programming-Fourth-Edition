FROM alpine:3.12
WORKDIR /app/

RUN apk add python3

COPY requirements.txt .
RUN apk add py3-pip && \
    pip3 install -r requirements.txt && \
    apk del py3-pip

COPY echo.py .
ENTRYPOINT ["python", "echo.py"]
