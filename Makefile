##########
## vars ##
##########
VERSION = 1.0
UID = $(shell id -u)
GID = $(shell id -g)
.DEFAULT_GOAL = _tasks
.PHONY: _tasks tf tf-create-backend tf-create-bucket

#############
## version ##
#############

.SILENT: _tasks
EDITOR=:


sha := $(shell git rev-parse --short HEAD)

###########
## tasks ##
###########

_tasks:
	@grep '^[a-z\-]*:' Makefile

tf-init:
	@echo "Terraform Init - sha:$(sha)"
	terraform -chdir=./terraform/assignment init -backend-config "profile=personal"

tf:
	@echo "Terraform Instructure Build - sha:$(sha)"
	terraform -chdir=./terraform/assignment $(filter-out $@,$(MAKECMDGOALS))

# tf-create-bucket -e BUCKET=nmd-training-tf-states-706146613458 -e REGION=us-west-2
create-bucket:
	aws --profile=$(PROFILE) s3api create-bucket \
	  --bucket $(BUCKET) \
	  --create-bucket-configuration LocationConstraint=$(REGION) \
	  --region $(REGION) \
	  --output=json

# make create-terraform-backend -e BUCKET=nmd-training-tf-states -e PROFILE=${AWS_PROFILE_NAME} -e DYNAMO_TABLE_NAME=jr-nmd-training-tf-state-lock-table -e REGION=us-west-2
create-terraform-backend:
	#$(MAKE) create-bucket -e REGION=$(REGION) -e BUCKET=$(BUCKET) #THIS CAN BE SET TO BE ENV SPECIFIC WITH A SUFFIX
	aws dynamodb create-table \
	  --profile=$(PROFILE) \
      --table-name $(DYNAMO_TABLE_NAME) \
      --attribute-definitions AttributeName=LockID,AttributeType=S \
      --key-schema AttributeName=LockID,KeyType=HASH \
      --billing-mode PAY_PER_REQUEST \
      --region $(REGION) \
      --output=json \
      --tags Key=Project,Value=nmd-training Key=Environment,Value=dev


