def run(**args):
    path = args.get("path")
    text = args.get("text", "")
    with open(path, "w") as f:
        f.write(text)
    print(f"Created file {path} with text {text}")
