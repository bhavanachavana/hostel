hospital_records = []
def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")

    patient = {
        "Patient ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Doctor": doctor
    }

    hospital_records.append(patient)
    print("Patient details added successfully!\n")

def display_patients():
    if not hospital_records:
        print("No patient records found.\n")
        return

    print("\n--- Hospital Patient Records ---")
    for p in hospital_records:
        print("-----------------------------")
        for key, value in p.items():
            print(f"{key}: {value}")
    print()

def main():
    while True:
        print("===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            display_patients()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

main()