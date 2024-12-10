import os


def run(**args):
    path = args.get("path")
    os.remove(path)
    print(f"Removed file {path}")
