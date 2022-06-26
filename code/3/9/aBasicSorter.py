with open("./aFileToSort.MKTI") as f:
    contents = f.read()
    input("loaded")
    print(sorted(contents))