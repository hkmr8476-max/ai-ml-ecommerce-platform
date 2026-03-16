FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir pandas numpy
COPY . .
CMD ["python", "training_pipeline.py"]
