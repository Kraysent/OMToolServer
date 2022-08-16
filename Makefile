DOCKERHUB_NAME=kraysent/omtool-server
YC_NAME=cr.yandex/crpb148a4o4b32kam70i/omtool-server

build-docker:
	docker build --tag $(DOCKERHUB_NAME) --tag $(YC_NAME) .

push-dockerhub:
	docker push $(DOCKERHUB_NAME)

push-yc:
	docker push $(YC_NAME)

run-docker:
	docker run --publish 3456:3456 $(DOCKERHUB_NAME)
