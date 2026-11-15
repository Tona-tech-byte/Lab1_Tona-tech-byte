SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20

START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road", "road",
    "60", "road", "road", "road", "road", "80", "road",
    "road", "zebra", "road", "road", "road", "road",
]

# TODO 1
def is_valid_sign(sign):
    if not isinstance(sign, str):
        return False

    if sign == "bus" or sign == "zebra":
        return True

    if sign.isdigit():
        number = int(sign)
        if 20 <= number <= 100:
            return True

    return False


# TODO 2
def get_sign_type(sign):
    if sign == "bus":
        return "bus"
    elif sign == "zebra":
        return "zebra"
    elif is_valid_sign(sign) and sign.isdigit():
        return "speed"
    else:
        return "road"


# TODO 3
def get_speed_limit(sign, current_limit):
    if get_sign_type(sign) == "speed":
        return int(sign)

    return current_limit


# TODO 4
def get_target_speed(limit, stop_timer):
    if stop_timer > 0:
        return 0

    return limit


# TODO 5
def adjust_speed(speed, target):
    if speed < target:
        speed = speed + ACCELERATION

        if speed > target:
            speed = target

    elif speed > target:
        speed = speed - BRAKING

        if speed < target:
            speed = target

    return speed


# TODO 6
def count_signs(road_list):
    speed_signs = 0
    zebras = 0
    buses = 0

    for sign in road_list:
        sign_type = get_sign_type(sign)

        if sign_type == "speed":
            speed_signs += 1
        elif sign_type == "zebra":
            zebras += 1
        elif sign_type == "bus":
            buses += 1

    return speed_signs, zebras, buses


# TODO 7
def ask_for_number(question, low, high):
    while True:
        try:
            number = int(input(question))

            if low <= number <= high:
                return number
            else:
                print(f"Please enter a number between {low} and {high}.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# TODO 8
def insert_sign(road_list, sign, position):
    if not is_valid_sign(sign):
        return False

    if not isinstance(position, int):
        return False

    if position < 0 or position > len(road_list):
        return False

    road_list.insert(position, sign)
    return True


# TODO 9
def replace_sign(road_list, sign, index):
    if not is_valid_sign(sign):
        return False

    if not isinstance(index, int):
        return False

    if index < 0 or index >= len(road_list):
        return False

    road_list[index] = sign
    return True


# TODO 10
def get_journey_summary(road_list):
    signs_passed = 0

    for sign in road_list:
        if get_sign_type(sign) != "road":
            signs_passed += 1

    length_m = len(road_list) * SEGMENT_M

    return signs_passed, length_m, START_NAME, END_NAME

if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
