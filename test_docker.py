import docker

client = docker.from_env()

print(client.version())
