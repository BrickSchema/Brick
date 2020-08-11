import docker

client = docker.from_env(version="auto")

print(client.version())
