FROM python:3.12.1-stretch

ENV PYTHONUNBUFFERED 1

WORKDIR /Users/livia/Downloads/InstaDjango/

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "/insta_clone/django-sh" ]