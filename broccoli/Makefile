build:
	docker build -t appimage .
run:
	docker run -d --name appcontainer -p 80:80 appimage
stop:
	docker stop appcontainer
cleanup: data
	docker rmi -f appimage &&\
	docker rm appcontainer
localf:
	cd app &&\
	export FLASK_APP=main &&\
	export FLASK_RUN_PORT=8000 &&\
	export FLASK_ENV=development &&\
	flask run
locald:
	docker run -d --name appcontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 appimage flask run --host=0.0.0.0 --port=80
data:
	-mv broccoli.db broccoli.`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 8`.db
	-docker cp appcontainer:/app/data/broccoli.db .
	-docker cp appcontainer:/app/data/json/ .
