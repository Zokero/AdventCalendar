import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "x: {0}, y: {1}".format(self.x, self.y)


class Section:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self) -> str:
        return "Section: start: {0}, end: {1}".format(self.point1, self.point2)


def get_input_data():
    file = open('/03.12.2019 (done)/dataInput.txt', 'r')
    return file.read().split('\n')


def get_list_of_all_points(wire):
    list_of_points = wire.split(',')
    list_of_each_points = list()
    x = 0
    y = 0
    sum_of_steps = 0

    for i in list_of_points:
        if i.startswith("R"):
            # print("turning RIGHT")
            temp_value_of_coordinate = i.replace("R", "")
            coordinate_value = int(temp_value_of_coordinate)
            sum_of_steps = sum_of_steps + abs(coordinate_value)
            x = x + coordinate_value
        elif i.startswith("L"):
            # print("turning LEFT")
            temp_value_of_coordinate = i.replace("L", "")
            coordinate_value = int(temp_value_of_coordinate)
            sum_of_steps = sum_of_steps + abs(coordinate_value)
            x = x - coordinate_value
        elif i.startswith("U"):
            # print("turning UP")
            temp_value_of_coordinate = i.replace("U", "")
            coordinate_value = int(temp_value_of_coordinate)
            sum_of_steps = sum_of_steps + abs(coordinate_value)
            y = y + coordinate_value
        elif i.startswith("D"):
            # print("turning DOWN")
            temp_value_of_coordinate = i.replace("D", "")
            coordinate_value = int(temp_value_of_coordinate)
            sum_of_steps = sum_of_steps + abs(coordinate_value)
            y = y - coordinate_value
        list_of_each_points.append(Point(x, y))

    # print(sum_of_steps)
    return list_of_each_points


def calculate_dist_between_points(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def intersection(s1, s2):
    segment_endpoints = []
    left = max(min(s1.point1.x, s1.point2.x), min(s2.point1.x, s2.point2.x))
    right = max(min(s1.point1.x, s1.point2.x), min(s2.point1.x, s2.point2.x))
    top = max(min(s1.point1.y, s1.point2.y), min(s2.point1.y, s2.point2.y))
    bottom = max(min(s1.point1.y, s1.point2.y), min(s2.point1.y, s2.point2.y))

    if top > bottom or left > right:
        segment_endpoints = []
        print('NO INTERSECTION')
        print(segment_endpoints)

    elif top == bottom and left == right:
        segment_endpoints.append(left)
        segment_endpoints.append(top)
        # print('POINT INTERSECTION')
        print(segment_endpoints)
        return Point(segment_endpoints[0], segment_endpoints[1])

    else:
        segment_endpoints.append(left)
        segment_endpoints.append(bottom)
        segment_endpoints.append(top)
        segment_endpoints.append(right)
        print('SEGMENT INTERSECTION')
        print(segment_endpoints)


def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if val == 0:
        return 0
    elif val < 0:
        return 2
    return 1


def on_line(l1, p):
    if (p.x <= max(l1.point1.x, l1.point2.x) and p.x <= min(l1.point1.x, l1.point2.x) and
            (p.y <= max(l1.point1.y, l1.point2.y) and p.y <= min(l1.point1.y, l1.point2.y))):
        return 1  # true

    return 2  # false


def is_intersect(l1, l2):
    dir1 = direction(l1.point1, l1.point2, l2.point1)
    dir2 = direction(l1.point1, l1.point2, l2.point2)
    dir3 = direction(l2.point1, l2.point2, l1.point1)
    dir4 = direction(l2.point1, l2.point2, l1.point2)

    if dir1 != dir2 and dir3 != dir4:
        return 1

    if dir1 == 0 and on_line(l1, l2.point1):
        return 1

    if dir2 == 0 and on_line(l1, l2.point2):
        return 1

    if dir3 == 0 and on_line(l2, l1.point1):
        return 1

    if dir4 == 0 and on_line(l2, l1.point2):
        return 1  # true

    return 2  # false


def create_sections_list(list_of_points):
    list_of_sections = list()
    for i in range(len(list_of_points)):
        if (i + 2) > len(list_of_points):
            break
        else:
            list_of_sections.append(Section(list_of_points[i], list_of_points[i + 1]))

    return list_of_sections


def get_list_of_intersect_points(sections1, sections2):
    list_of_intersect_points = list()
    for i in range(len(sections1)):
        for j in range(len(sections2)):
            result = is_intersect(sections1[i], sections2[j])
            if result == 1:
                print("intersect sections: " + str(sections1[i]) + " " + str(sections2[j]))
                list_of_intersect_points.append(intersection(sections1[i], sections2[j]))

    return list_of_intersect_points


def get_min_distance(sections1, sections2):
    list_of_intersect_pointss = get_list_of_intersect_points(sections1, sections2)
    list_of_distances = list()
    for i in list_of_intersect_pointss:
        # print(i)
        list_of_distances.append(calculate_dist_between_points(Point(0, 0), i))
    final_result = min(list_of_distances)
    # print(final_result)
    return final_result


def get_list_of_distances_to_intersection_point_for_one(all_points_list, all_intersections_list):
    list_of_sums = list()
    for t in all_intersections_list:
        distance_sum = 0
        temp_point = Point(0, 0)
        for g in all_points_list:
            if t.x == temp_point.x or t.y == temp_point.y:
                dist = math.sqrt((temp_point.x - t.x) ** 2 + (temp_point.y - t.y) ** 2)
                distance_sum = distance_sum + int(dist)
                break
            else:
                dist = math.sqrt((temp_point.x - g.x) ** 2 + (temp_point.y - g.y) ** 2)
                distance_sum = distance_sum + int(dist)
            temp_point = Point(g.x, g.y)

        list_of_sums.append(distance_sum)
    return list_of_sums


def sum_distance(l1, l2):
    result_list = list()
    for g in range(len(l1)):
        current_sum = l1[g] + l2[g]
        if current_sum == 610:
            print("OK")
        result_list.append(current_sum)
        print(current_sum)
    return result_list


test_list_one = get_input_data()[2]
test_list_two = get_input_data()[3]

test_list_three = get_input_data()[4]
test_list_four = get_input_data()[5]

proper_list_one = get_input_data()[0]
proper_list_two = get_input_data()[1]

all_points_from_test_list_one = get_list_of_all_points(test_list_one)
all_points_from_test_list_two = get_list_of_all_points(test_list_two)
all_points_from_test_list_three = get_list_of_all_points(test_list_three)
all_points_from_test_list_four = get_list_of_all_points(test_list_four)

all_points_from_proper_list1 = get_list_of_all_points(proper_list_one)
all_points_from_proper_list2 = get_list_of_all_points(proper_list_two)


section_list_one = create_sections_list(all_points_from_test_list_one)
section_list_two = create_sections_list(all_points_from_test_list_two)
section_list_three = create_sections_list(all_points_from_test_list_three)
section_list_four = create_sections_list(all_points_from_test_list_four)

section_proper_list1 = create_sections_list(all_points_from_proper_list1)
section_proper_list2 = create_sections_list(all_points_from_proper_list2)

# assert get_min_distance(section_list_one, section_list_two) == 159
# print("etstset")
# assert get_min_distance(section_list_three, section_list_four) == 135

# get_min_distance(section_proper_list1, section_proper_list2)
list_of_intersect_points = get_list_of_intersect_points(section_proper_list1, section_proper_list2)
# get_min_distance(section_list_one, section_list_two)

a = get_list_of_distances_to_intersection_point_for_one(all_points_from_proper_list1, list_of_intersect_points)
print(a)
print("^^^^^^")
b = get_list_of_distances_to_intersection_point_for_one(all_points_from_proper_list2, list_of_intersect_points)
print(b)
print("///")
print(min(sum_distance(a, b)))

# assert get_closest_intersection() == 610
# assert get_closest_intersection() == 410
