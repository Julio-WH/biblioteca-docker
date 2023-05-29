FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "Biblioteca", "Biblioteca.wsgi:application"]