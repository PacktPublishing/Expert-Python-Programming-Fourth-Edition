# The "slim" versions are sensible starting
# points for other lightweight Python-based images
FROM python:3.9-slim
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY echo.py .
CMD ["python", "echo.py"]
