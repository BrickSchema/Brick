from ontoenv import OntoEnv, Config
cfg = Config(["support/", "extensions/", "examples/", "rec/Source/SHACL/RealEstateCore"], strict=False, offline=True)
env = OntoEnv(cfg)
