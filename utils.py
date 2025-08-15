import pandas as pd

def load_dat_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split()
            label = int(parts[0])
            features = {f"f{int(kv.split(':')[0])}": float(kv.split(':')[1]) for kv in parts[1:]}
            features["label"] = label
            data.append(features)
    return pd.DataFrame(data)