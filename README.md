![ci](https://github.com/Fiufit-Grupo-10/python-template/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/Fiufit-Grupo-10/python-template/branch/main/graph/badge.svg?token=0QRZ6NO0R1)](https://codecov.io/gh/Fiufit-Grupo-10/python-template)

# FiuFit-Users
Template for python services

Build the image and spin up the container:

```bash
docker-compose up -d --build
```

To run tests or other commands on the container

```bash
sudo docker-compose exec <command>
```

```bash
Commands:
	web pytest -v
```
