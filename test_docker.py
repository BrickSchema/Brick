import docker

client = docker.from_env(version="1.38")

print(client.version())
