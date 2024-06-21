from ontoenv import OntoEnv, Config
cfg = Config(["support/", "extensions/", "examples/"], strict=False, offline=True)
env = OntoEnv(cfg)
