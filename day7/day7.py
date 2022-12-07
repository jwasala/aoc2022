from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    name: str
    _size: int
    children: list["Node"]
    parent: Optional["Node"]
    is_dir: bool

    @property
    def size(self):
        if not self.is_dir:
            return self._size
        else:
            return sum([node.size for node in self.children])


def find_or_create_child_node(
    parent: Node, name: str, size: int, is_dir: bool
) -> (Node, bool):
    lookup_list = [
        node for node in parent.children if node.name == f"{parent.name}/{name}"
    ]
    if lookup_list:
        return lookup_list[0], False
    else:
        new_node = Node(
            name=f"{parent.name}/{name}",
            _size=size,
            children=[],
            parent=parent,
            is_dir=is_dir,
        )
        parent.children.append(new_node)
        return new_node, True


with open("input.txt") as file:
    root_node = Node(name="", _size=0, children=[], parent=None, is_dir=True)
    current_node = root_node
    dir_section = False

    file.readline()
    for line in file:
        line = line.strip()

        if line.startswith("$") and dir_section:
            dir_section = False

        if not line.startswith("$") and dir_section:
            line_split = line.split(" ")
            child, created = find_or_create_child_node(
                current_node,
                line_split[1],
                int(line_split[0]) if line_split[0] != "dir" else 0,
                line_split[0] == "dir",
            )

        if line == "$ ls":
            dir_section = True

        if line.startswith("$ cd"):
            arg = line.split(" ")[2]
            if arg == "..":
                current_node = current_node.parent
            else:
                current_node = [
                    node
                    for node in current_node.children
                    if node.name == f"{current_node.name}/{arg}"
                ][0]


def part1():
    s = 0

    def _rec(node: Node):
        nonlocal s
        if node.is_dir and node.size <= 100000:
            s += node.size
        for child in node.children:
            _rec(child)

    _rec(root_node)
    return s


def part2():
    sizes = []
    total_size = root_node.size
    space_needed = total_size - 40000000

    def _rec(node: Node):
        nonlocal sizes
        if node.is_dir:
            sizes.append(node.size)
        for child in node.children:
            _rec(child)

    _rec(root_node)
    for size in sorted(sizes):
        if size >= space_needed:
            return size


print(part1())
print(part2())
