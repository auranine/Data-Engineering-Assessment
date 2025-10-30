# You will need to modify the key value in the backend block to a unique value for your assignment.

provider "aws" {
  region = var.region_name
  profile = var.aws_profile
}
data "aws_caller_identity" "current" {}


terraform {
  backend "s3" {
    # bucket         = "REPLACED VIA PARTIAL BACKEND CONFIG -backend-config=configfile.tfvars"
    ## update the key value to a unique value for your assignment
    # key            = "assignment/johnny-rivera.tfstate"
    region         = "us-west-2"
    # dynamodb_table = "REPLACED VIA PARTIAL BACKEND CONFIG -backend-config=configfile.tfvars"
    encrypt        = true                   # Encrypts the state file at rest
  }
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.18.0"
    }
  }
}
