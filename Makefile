DOCKER_NAME=omtool-server-docker

build-docker:
	docker build --tag $(DOCKER_NAME) .

run-docker:
	docker run --publish 3456:3456 $(DOCKER_NAME)