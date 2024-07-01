FROM python:3.12

WORKDIR /app

# Copying actuall application
COPY . /app
# RUN chmod +x /app/src/run.sh

RUN pip install poetry==1.4.2

# Installing requirements
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN poetry install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
