# gpt4all-api

Welcome to the GPT4All API repository. This project integrates the powerful GPT4All language models with a FastAPI framework, adhering to the OpenAI OpenAPI specification. It's designed to offer a seamless and scalable way to deploy GPT4All models in a web environment.

## Features

- FastAPI Framework: Leverages the speed and simplicity of FastAPI.
- GPT4All Integration: Utilizes the locally deployable, privacy-aware capabilities of GPT4All.
- OpenAI OpenAPI Compliance: Ensures compatibility and standardization according to OpenAI's API specifications.
- Scalable Deployment: Ready for deployment in various environments, from small-scale local setups to large-scale cloud deployments.
- Privacy-Centric: Local deployment ensures data privacy and security.

## Installation

### Docker:

```bash
docker pull iverly/gpt4all-api
docker run -d --name gpt4all-api -p 8000:8000 iverly/gpt4all-api
```

### Building from source:

```bash
git clone https://github.com/iverly/gpt4all-api
cd gpt4all-api
pip install -r requirements.txt
uvicorn main:app
```

The API will be available at http://127.0.0.1:8000.
Utilize Swagger UI for easy interaction with the API endpoints. (at /docs)

## Contributing

Contributions to the GPT4All API project are welcome. Please read our contributing guidelines for more information on how to get involved.

## License

This project is licensed under Apache 2.0. See the LICENSE file for more information.
