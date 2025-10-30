# Infra

## Prerequisites*

-------------

- brew
- tfenv

__* Note:__ This project configuration and development instructions here have been tested on Mac OS.
Linux and Windows specific and changes are welcome contributions!

---------------

## Initital IAM Setup (this can be setup many ways - for assessment, assuming these are created outside of this project)
1. Create IAM user for terraform (e.g. tf-user)
2. Create IAM Roles to assume with the appropriate permissions (e.g. tf-admin-role, tf-deploy-role)
   1. one for admin (create infrastructure for application) - least privileges needed to create infra for app
   2. one for deploy, ci/cd which only deploys the latest function - least privileges needed to deploy app
3. Ensure all roles can be assumed by user (e.g. tf-user) via trust policy
4. Ensure user (e.g. tf-user) has ability to assume roles
5. Configure ~/.aws/config
   
        # EXAMPLE
        [profile tf-deploy]
        role_arn = arn:aws:iam::225108271077:role/tf-deploy-role
        source_profile = personal
        
        [profile tf-admin]
        role_arn = arn:aws:iam::225108271077:role/tf-admin-role
        source_profile = personal
6. Testing Roles

        ➜  Data-Engineering-Assessment git:(main) ✗ aws sts get-caller-identity --profile tf-admin
        ➜  Data-Engineering-Assessment git:(main) ✗ aws sts get-caller-identity --profile tf-deploy


## Setup 

[AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

From this directory `${PROJECT_DIRECTORY}/terraform` directory
1. install tfenv `brew install tfenv`
2. install terraform `tfenv install`

## Provision 

From ${PROJECT_DIRECTORY}
1. Setup terraform backend (s3, dynamodb) for state and locks
   1. `make create-terraform-backend -e PROFILE=${YOUR_AWS_PROFILE} -e BUCKET=${BUCKET_NAME} -e DYNAMO_TABLE=${DYNAMO_TABLE}`
   2. 

From app directory `${PROJECT_DIRECTORY}/terraform/assignment` directory
1. Setup aws profile `aws configure --profile <YOUR_AWS_PROFILE>` using key id and secret (TODO: Use role assume?)
2. Set vars `candidate_name and aws_profile` - Ensure aws_profile matches the above (step 1 value)
3. Init Terraform `terraform init -backend-config "profile=YOUR_AWS_PROFILE"`
