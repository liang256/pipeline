def run(**args):
    path = args.get("path")
    with open(path, "r") as f:
        print(f.read())
