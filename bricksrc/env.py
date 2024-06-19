from ontoenv import OntoEnv, Config
cfg = Config(["support/", "extensions/"], strict=False, offline=True)
env = OntoEnv(cfg)
