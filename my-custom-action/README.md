### About

---

This directory defines a custom GitHub Action, `my-custom-action`, that can be used in a GitHub Action workflow file.

An example using this custom action in a workflow file is found in `.github/workflows/my-custom-action-workflow.yml` in the root of this repo.

- action.yml

  - This defines the action and contains some extra information about the action (_name_, _description_, _author_). It also defines any variables that should be passed to the action (_MY_NAME_) and describes how the action should be run (_using_, _image_).

- Dockerfile

  - Defines an environment for the action to be run in. This is needed to guarantee that the test runs the same every time.

- entrypoint.sh
  - The code that is actually executed inside of the Docker container. In this case, it just outputs a string with a variable substituted.
