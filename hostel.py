def hostel_details(hostel_id, hostel_name, rooms, fee):
    result = (
        f"Hostel ID   : {hostel_id}\n"
        f"Hostel Name : {hostel_name}\n"
        f"Rooms       : {rooms}\n"
        f"Fee         : {fee}\n"
    )
    return result


if __name__ == "__main__":
    hostel_id = "H101"
    hostel_name = "Sai Hostel"
    rooms = 50
    fee = 45000

    print(hostel_details(hostel_id, hostel_name, rooms, fee))