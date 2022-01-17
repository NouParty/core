FROM python:3.9

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
