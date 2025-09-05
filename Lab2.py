# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    """
    Calculate the height of a ball dropped from inital height of a ball dropped from inital height h0 after time t.
    h0: initial height (meters)
    t: time elapsed (seconds)
    returns: height of ball at time t (meters)
    """
    g = 9.8
    height = h0 - 0.5 * g * (t ** 2)
    return round(height, 1)
if __name__ == "__main__":
    h0 = 50
    for time in [1, 2, 3]:
        print(f"Height of the ball at time {time} second = {calculate_height(h0, time)} meters")
    

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    """
    Calculate the distance traveled by a car moving at 20 m/s after time t.
    t: time in seconds
    returns: distance in meters
    """
    speed = 20
    distance = speed * t
    return round(distance, 1)
if __name__ == "__main__":
    for time in [1, 2, 3]:
        print(f"The car will travel {calculate_car_distance(time)} meters in {time} second(s).")
