import hospital01
def test_add_patient(monkeypatch):
    inputs = iter([
        "01",
        "khushi",
        "30",
        "female",
        "Fever",
        "Dr. Smith"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    hospital01.hospital_records.clear()
    hospital01.add_patient()

    assert len(hospital01.hospital_records) == 1
    assert hospital01.hospital_records[0]["Patient ID"] == "P001"
    assert hospital01.hospital_records[0]["Name"] == "John"


def test_display_patients(capsys):
    hospital01.hospital_records.clear()

    hospital01.hospital_records.append({
        "Patient ID": "015",
        "Name": "bhavana",
        "Age": "20",
        "Gender": "Female",
        "Disease": "fever",
        "Doctor": "Dr.preethi"
    })

    hospital01.display_patients()

    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "Dr. Brown" in captured.out


def test_display_no_patients(capsys):
    hospital01.hospital_records.clear()

    hospital01.display_patients()
    captured = capsys.readouterr()

    assert "No patient records found" in captured.out
