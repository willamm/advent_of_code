def parse_input(filename):
    sensors = set()
    beacons = set()
    with open(filename, "r") as f:
        for line in f.read().strip().split("\n"):
            sensor, beacon = line.split(': ')
            sensor_x, sensor_y = int(sensor.split("x=")[1].split(',')[0]), int(sensor.split("y=")[1])
            beacon_x, beacon_y = int(beacon.split("x=")[1].split(',')[0]), int(beacon.split("y=")[1])
            d = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors.add((sensor_x, sensor_y, d))
            beacons.add((beacon_x, beacon_y))
    return sensors, beacons

def possible(sensors, beacons, x, y):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True

def p1(sensors, beacons):
    count = 0
    y = 10
    for x in range(min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)):
        if not possible(sensors, beacons, x, y) and (x, y) not in beacons:
            count += 1
    return count

def main():
    sensors, beacons = parse_input("input.txt")
    print(p1(sensors, beacons))

main()