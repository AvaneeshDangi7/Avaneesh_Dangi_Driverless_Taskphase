import csv
import math


def process_cones():

    with open('cones.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)


    for row in rows:
        row['x'] = float(row['x'])
        row['y'] = float(row['y'])
        row['dist'] = math.sqrt(row['x'] ** 2 + row['y'] ** 2)

    def get_distance(row):
        return row['dist']

    rows.sort(key=get_distance)

    blue_cones = [r for r in rows if r['colour'].lower() == 'blue']
    yellow_cones = [r for r in rows if r['colour'].lower() == 'yellow']


    with open('blue.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["cone_id", "x", "y", "colour"])
        writer.writeheader()
        for r in blue_cones:
            writer.writerow({"cone_id": r['cone_id'], "x": r['x'], "y": r['y'], "colour": r['colour']})


    with open('yellow.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["cone_id", "x", "y", "colour"])
        writer.writeheader()
        for r in yellow_cones:
            writer.writerow({"cone_id": r['cone_id'], "x": r['x'], "y": r['y'], "colour": r['colour']})


    midpoints = []
    for b in blue_cones:
        min_dist =0.0
        nearest_yellow = None


        for y in yellow_cones:
            d = math.sqrt((b['x'] - y['x']) ** 2 + (b['y'] - y['y']) ** 2)
            if d < min_dist:
                min_dist = d
                nearest_yellow = y


        if nearest_yellow:
            mx = (b['x'] + nearest_yellow['x']) / 2.0
            my = (b['y'] + nearest_yellow['y']) / 2.0
            midpoints.append({
                "blue_id": b['cone_id'],
                "yellow_id": nearest_yellow['cone_id'],
                "x": mx,
                "y": my })


    with open('centreline.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["blue_id", "yellow_id", "x", "y"])
        writer.writeheader()
        writer.writerows(midpoints)


#main
    process_cones()
print("Task terminated")