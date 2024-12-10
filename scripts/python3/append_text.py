def run(**args):
    path = args.get("path")
    text = args.get("text")
    with open(path, "a") as f:
        f.write(text)
    print(f"Appended text {text} to {path}")
