FROM python:3.10.0 as dependecies

COPY requirements.txt /requirements.txt
COPY entry_point.sh /entry_point.sh

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt


FROM dependecies

COPY . /KefirTestCase

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /KefirTestCase

WORKDIR /KefirTestCase

ENTRYPOINT ["./entry_point.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]