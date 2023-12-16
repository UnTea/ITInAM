container_port = 5000
docker_port = 5000
image_name = web_server_image
container_name = web_server
is_debug = 1

build:
	docker build . -t $(image_name)

run:
	docker run --name $(container_name) -p $(docker_port):$(container_port) -e DEBUG=$(is_debug) $(image_name)

start:
	docker start $(container_name)

stop:
	docker stop $(container_name)


.PHONY: start build run stop
