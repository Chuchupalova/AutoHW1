FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pytest psycopg2-binary requests flask allure-pytest
CMD ["pytest", "-v", "--alluredir=allure-results"]

