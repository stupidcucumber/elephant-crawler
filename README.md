# elephant-crowler
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fstupidcucumber%2Felephant-crowler%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)

![Logotype](./assets/logo.png)


## Development
To start contributing this repository:

1. Install requirements:
```
python -m pip install -r requirements.dev.txt
```

2. Install pre-commit hook:
```
pre-commit install
```

You're good to go!

### Architecture
![Architecture](./assets/architecture.png)

1. DB stores all data from the texts.
2. Core-API provides access to the database for the external services.
3. Crawler-SVC starts all


## Deployment

Only thing you need to do is:
```
docker-compose up --build
```

Then all scrapped texts are available on the endpoint:
```
http://localhost:8081/scrapped-texts
```
