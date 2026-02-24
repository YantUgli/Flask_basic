FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# sama kaya CD
WORKDIR /app

# install pipenv
RUN pip install --no-cache-dir pipenv

# copy dependency dulu (biar caching)
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

# copy source
COPY . .

EXPOSE 5000

# jalankan gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]