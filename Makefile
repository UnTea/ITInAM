docker:
	docker build . -t flask_app_dev

run:
	docker run -p 5000:5000 -e DEBUG=1 flask_app_dev

.PHONY: docker
