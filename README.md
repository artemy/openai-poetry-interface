# OpenAI Poetry generator

OpenAI Poetry generates poetry from specified prompts

# Prerequisites

- [Docker Desktop](https://docker.com)

# Usage

- Get API Key from [OpenAI Beta](https://beta.openai.com/account/api-keys) website.
- Put API Key in [.env](.env) file in the project folder
- Start the docker image by running the following command from the project folder:
  ```shell
  docker-compose up -d
  ```
- Once the docker image is successfully running, you should be able to access OpenAI Poetry Generator web interface at [http://localhost:8000/](http://localhost:8000/)
- To stop the docker image, run the following command from the project folder:
  ```shell
  docker-compose stop
  ```

# Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI API](https://beta.openai.com)
- [Docker Desktop](https://docker.com)
