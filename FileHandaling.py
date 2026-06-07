import os
path_dir = os.path.dirname(__file__)
data_path = os.path.join(path_dir, "journal.txt")
entries = [
    "Day 1: Started learning Python",
    "Day 2: Went for a run",
    "Day 3: Built my first Python script"
]
with open(data_path, "at") as f:
    for line in entries:
        f.write(f"{line}"+"\n")
with open(data_path, "r") as f:
    split = f.read().split("\n")
    for line in split:
        print(line)


new_entries = [
    "Day 4: Had coffee with a friend",
    "Day 5: Completed a Python project",
    "Day 6: Read a book"
]
with open(data_path, "a") as f:
    for line in new_entries:
        f.write(line+"\n")
with open(data_path, "rt") as f:
    split = f.read().split("\n")
    for line in split:
        print(line)
