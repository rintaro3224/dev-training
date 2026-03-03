FROM python:3.9-bullseye

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY ./docker/python/requirements.txt requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

WORKDIR /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]