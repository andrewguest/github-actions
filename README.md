[![A workflow for my Hello world file](https://github.com/andrewguest/github-actions/actions/workflows/my-custom-action-workflow.yml/badge.svg)](https://github.com/andrewguest/github-actions/actions/workflows/my-custom-action-workflow.yml)
[![Code formatting checks](https://github.com/andrewguest/github-actions/actions/workflows/code-quality.yaml/badge.svg)](https://github.com/andrewguest/github-actions/actions/workflows/code-quality.yaml)
[![Deploy to AWS Lambda](https://github.com/andrewguest/github-actions/actions/workflows/deploy_to_aws_lambda.yml/badge.svg)](https://github.com/andrewguest/github-actions/actions/workflows/deploy_to_aws_lambda.yml)
[![Python workflow](https://github.com/andrewguest/github-actions/actions/workflows/python-example-workflow.yml/badge.svg)](https://github.com/andrewguest/github-actions/actions/workflows/python-example-workflow.yml)


| File/Directory                                    | Description                                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `aws-auto-deploy/`                                | Directory that contains a simple Python function that runs on AWS Lambda.                                   |
| `my-custom-action/`                               | Directory that contains everything for a custom GitHub Action.                                              |
| `python-example/`                                 | Directory that contains a simple Python script with a test using PyTest.                                    |
| `.github/workflows/deploy_to_aws_lambda.yml`      | Workflow to run the PyTest tests and then, automatically, deploy the Python code to an AWS Lambda function. |
| `.github/workflows/my-custom-action-workflow.yml` | File describing a workflow using our, custom, my-custom-example action.                                     |
| `.github/workflows/python-example-workflow.yml`   | File describing a workflow to run the tests found in `python-example/tests`                                 |
| `.github/workflows/code-quality.yaml` | File describing a workflow to run Black formatter checks. |
