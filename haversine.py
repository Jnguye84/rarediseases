from math import radians, sin, cos, sqrt, atan2

def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Compute differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

# Example usage:
coord1 = (-13.3, 65.78)  # San Francisco, CA
coord2 = (-14.18, 68.17)  # Los Angeles, CA

distance = haversine_distance(coord1, coord2)
print(f"Distance between the coordinates: {distance:.2f} km")
