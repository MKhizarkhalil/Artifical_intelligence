def tower_of_hanoi(n, source, destination, aux):
    if n == 1:
        print("Move disk", n, "from", source, "to", destination)
        return

    tower_of_hanoi(n-1, source, aux, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, aux, destination, source)

num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')
