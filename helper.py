import pandas as pd

def load_data(path: str):
    import pandas as pd

    df = pd.read_csv(path)

    data = []
    for _, row in df.iterrows():
        data.append(row.to_dict())

    return data

def to_dict(data: dict):
    r = {}
    def _to_dict(data: dict, r: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                _to_dict(data=value, r=r)
            else:
                r[key] = value
    _to_dict(data, r)
    return r