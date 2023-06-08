#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_properties = dir(hidden_4)
    for item in sorted(all_properties):
        if not item.startswith("__"):
            print(item)
