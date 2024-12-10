def run(**args):
    path = args.get("path")
    old_text = args.get("old_text")
    new_text = args.get("new_text")
    with open(path, "r") as f:
        text = f.read()
    text = text.replace(old_text, new_text)
    with open(path, "w") as f:
        f.write(text)
    print(f"Replaced {old_text} with {new_text} in {path}")
