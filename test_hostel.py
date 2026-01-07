from hostel import hostel_details
def test_hostel_details():
    expected_output = (
        "Hostel ID   : H101\n"
        "Hostel Name : Sai Hostel\n"
        "Rooms       : 50\n"
        "Fee         : 45000\n"
    )

    assert hostel_details("H101", "Sai Hostel", 50, 45000) == expected_output