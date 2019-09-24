from .logger import Logger

log = Logger()

def read_yaml(yaml_path):
    import yaml
    try:
        with open(yaml_path) as f:
            param = yaml.load(f)
    except Exception as e:
        log.error(msg="can't read yaml file.", errmsg=str(e))
        return e
    return param