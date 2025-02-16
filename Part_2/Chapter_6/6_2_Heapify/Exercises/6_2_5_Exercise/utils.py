def left(ind: int) -> int:
    return (ind + 1) * 2 - 1


def right(ind: int) -> int:
    return (ind + 1) * 2


def parent(ind: int) -> int:
    if ind <= 0:
        return -1
    return (ind - 1) // 2