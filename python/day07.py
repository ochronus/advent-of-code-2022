commands = open("../input/day07.txt", mode="r").read().splitlines()


file_sizes = dict()
subdirs = set()
current_path = []

for command in commands:
    cmdline = command.split(" ")
    if cmdline[0] == "$":
        if cmdline[1] == "ls":
            pass
        if cmdline[1] == "cd":
            if cmdline[2] == "..":
                current_path.pop()
            else:
                current_path.append(cmdline[2])
    else:
        path = (
            *current_path,
            cmdline[1],
        )
        if cmdline[0] == "dir":
            subdirs.add(path)
        else:
            file_sizes[path] = int(cmdline[0])

dir_sizes = {
    dir_path: sum(
        size
        for fpath, size in file_sizes.items()
        if "/".join(fpath).startswith("/".join(dir_path))
    )  # Look Ma, no recursion!
    for dir_path in subdirs
}


part1 = sum(dirsize for dirsize in dir_sizes.values() if dirsize < 100000)

limit = sum(file_sizes.values()) - 40000000
part2 = min(dirsize for dirsize in dir_sizes.values() if limit <= dirsize)

print(part1)
print(part2)
