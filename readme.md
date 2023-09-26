# Python Fast API Microsevice
API for JIRA Microservice project

# Tools used
- uvicorn - to start fastapi
- AWS SAM - for AWS deployment

# How to test locally
- Run:
    - `cd src`
    - `python -m uvicorn main:app`
- endpoint base: `http://localhost:8000/`

# Deployment
- gitlab-ci.yaml file defined the deployment via pipeline
- if it is merged to master the deploy-prod pipeline definition will run else deploy-dev
