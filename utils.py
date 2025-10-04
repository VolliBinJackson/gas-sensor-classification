import pandas as pd

# For loading only one batch
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

# For loading all batches
def load_all_batches(folderpath, batches=10):
    dfs = []
    for i in range(1, batches+1):
        filepath = fr"{folderpath}\batch{i}.dat"
        df_temp = load_dat_file(filepath)
        df_temp["batch"] = f"batch{i}"
        dfs.append(df_temp)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df