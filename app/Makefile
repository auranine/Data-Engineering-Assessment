##########
## vars ##
##########
VERSION = 1.0
UID = $(shell id -u)
GID = $(shell id -g)
.DEFAULT_GOAL = _tasks

#############
## version ##
#############

#.SILENT: these will not be listed under tasks
.SILENT: _tasks

sha := $(shell git rev-parse --short HEAD)

##########
## VARS ##
##########
REPO := $(if $(DOCKER_REPO),$(DOCKER_REPO)/,)

###########
## tasks ##
###########

_tasks:
	@grep '^[a-z\-]*:' Makefile

build-container:
	docker build -t $(REPO)order-analytics:$(sha) .
	docker tag $(REPO)order-analytics:$(sha) $(REPO)order-analytics:latest
	docker tag $(REPO)order-analytics:$(sha) $(REPO)order-analytics:qa
