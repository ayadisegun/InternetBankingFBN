import yaml

class Config:
    _data = None

    @classmethod
    def load(cls, path="config/config.yaml"):
        if cls._data is None:   # Load only once = very efficient!!
            with open(path, "r") as file:
                cls._data = yaml.safe_load(file)
        return cls._data

    @classmethod
    def get(cls, *keys):
        data = cls.load()
        for key in keys:
            data = data[key]
        return data
