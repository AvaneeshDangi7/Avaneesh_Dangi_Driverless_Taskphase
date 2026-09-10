def sort_by_proximity(coords, reference):
    def getdistance(point):
        return (point[0] - reference[0]) ** 2 + (point[1] - reference[1]) ** 2

    return sorted(coords, key=getdistance)


def inp_coordinates():
    user_input = input("Enter coordinates separated by a space: ")


    x_str, y_str = user_input.split()
    x = int(x_str.strip())
    y = int(y_str.strip())
    return x, y

points = [(0, 3), (0, 1), (1, 2)]

ref = inp_coordinates()
print(ref)

print(sort_by_proximity(points, ref))