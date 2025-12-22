# Base image - python + os
FROM python:3.10-slim
# Creating a directory
WORKDIR /app
# Copying requirements file into the container directory
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app.py .
COPY xgb_car_price_model.pkl .

EXPOSE 5000

CMD ["python", "flask_app.py"]










