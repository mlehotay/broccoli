FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install --upgrade pip
RUN pip install flask gunicorn pandas scikit-learn
