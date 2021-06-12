# python3
import sys

def determine_farthest_reachable_station(distance, current_spot, tank, stops):
    # 1500, 0, 400, [100,200,600,800,1000,1400]
    current_farthest_reachable_station = current_spot
    while tank>0:
        try:
            if stops[0]<=current_farthest_reachable_station + tank:
                tank -= stops[0] - current_farthest_reachable_station
                current_farthest_reachable_station = stops.pop(0)
            else:
                return current_farthest_reachable_station
        except IndexError:
            return distance if current_farthest_reachable_station + tank >= distance else current_farthest_reachable_station
    
    return current_farthest_reachable_station

def compute_min_refills(distance, tank, stops):
    # 1500, 400, [100,200,600,800,1000,1400]
    num_stops = 0
    current_spot = 0
    while distance>current_spot:
        farthest_reachable_station = determine_farthest_reachable_station(distance, current_spot, tank, stops)

        if farthest_reachable_station==current_spot:
            return -1
        else:
            current_spot = farthest_reachable_station
            num_stops += 0 if farthest_reachable_station == distance else 1
    return num_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
