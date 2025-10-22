# storage.py
def save_master_hash(hash_str: str):
    with open("master.key", "w") as f:
        f.write(hash_str)


def load_master_hash() -> str:
    try:
        with open("master.key", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
