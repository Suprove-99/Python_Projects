import datetime

print("\n=====================================================")
print("           Hospital Management System                ")
print("=====================================================")
print("")

patients = {}

# ----------------------------- doctors according to department --------------------------------------
# id, name, age, sex, designation, chamber_day,chamber_time, fees
Cardiologists = {'d-1': ['d-1', "Dr. AAA", 45, "M", 'Cardiologist', 'Sun,Mon', '4pm-8pm', 1000],
                 'd-2': ['d-2', "Dr. BBB", 38, "M", 'Cardiologist', 'Sat,Fri', '6pm-10pm', 1000], }
Gynecologists = {'d-3': ['d-3', "Dr. CCC", 37, "F", 'Gynecologist', 'Sun,Fri', '10am-1pm', 800],
                 'd-4': ['d-4', "Dr. DDD", 35, "F", 'Gynecologist', 'Mon,Tue', '4pm-6pm', 800], }
Gastroenterologists = {'d-5': ['d-5', "Dr. EEE", 50, "M", 'Gastroenterologist', 'Sun,Fri', '10am-1pm', 900],
                       'd-6': ['d-6', "Dr. FFF", 42, "F", 'Gastroenterologist', 'Mon,Tue', '4pm-6pm', 900], }
Neurologists = {'d-7': ['d-7', "Dr. GGG", 37, "M", 'Neurologist', 'Sun,Mon', '5pm-9pm', 800],
                'd-8': ['d-8', "Dr. HHH", 40, "M", 'Neurologist', 'Wed,Thu', '4pm-6pm', 900], }
Psychiatrists = {'d-9': ['d-9', "Dr. III", 47, "M", 'Psychiatrist', 'Sat,Sun', '5pm-9pm', 1000],
                 'd-10': ['d-10', "Dr. JJJ", 52, "F", 'Psychiatrist', 'Thu,Fri', '4pm-6pm', 1000], }

lst = [Cardiologists, Gynecologists, Gastroenterologists, Neurologists, Psychiatrists]

while True:
    print("---------------------------------")
    print("|         Main Menu             |\n"
          "|     ----------------          |\n"
          "|   1. Patients' Corner         |\n"
          "|   2. Doctors' Corner          |\n"
          "|                               | \n"
          "|(Press 'E' to exit the program)|")
    print("---------------------------------")
    choice1 = input("Enter your choice:..")

    # --------------------------------------- patient ----------------------------------------------
    if choice1 == '1':
        while True:
            print("\n---------------------")
            print("* Patient's Corner *")
            print("---------------------")
            print("1.Add New Patient\n2.Patient Details\n3.Back")
            print("-------------------")
            choice2 = int(input("Enter your choice:"))

            # ---------------- Add Patient -------------------
            if choice2 == 1:
                # Taking patient info
                print("Enter patient details:-->")
                p_id = int(input("ID:"))
                p_name = input("Name: ")
                p_age = int(input("Age: "))
                p_sex = input("Sex(M/F): ").upper()
                p_blood_group = input("Blood Group(e.g, B +ve): ")
                p_address = input("Address: ")

                # appointed_doctor
                print("List of Departments: ", '\n1.Cardiology', '\n2.Gynecology', '\n3.Gastroenterology',
                      '\n4.Neurology', '\n5.Psychiatrists')
                dept_choice = int(input('\nEnter your choice: '))
                print("\nDoctor's list: ")
                print("------------------")
                # doctor choice
                dept = lst[dept_choice - 1]
                for k in dept:
                    id, name, age, sex, designation, chamber_day, chamber_time, fees = dept[k]
                    print('Doctor ID:', id, '\nDoctor Name:', name, '\nAge:', age, '\nSex:', sex, '\nDesignation:',
                          designation,
                          '\nChamber Day:', chamber_day, '\nChamber Time:', chamber_time, "\nFees:", fees)
                    print("\n")
                print("------------------------")
                doc_choice = input('Enter your choice: ')
                appointed_doctor = dept[doc_choice][1]
                # date
                d, m, y = map(int, input("Appointment date(dd-mm-yy): ").split("-"))
                appointment_date = datetime.date(y, m, d)

                # adding to patient dictionary
                patients[p_id] = [p_id, p_name, p_age, p_sex, p_blood_group, p_address, appointed_doctor,
                                  appointment_date]
                print("\nPatient added successfully!!\n")
                input("(Press any key to go back.)\n")
                break

            # -------- print patient details ----------
            elif choice2 == 2:
                if not patients:
                    print("Opps!!! The patient queue is empty. Please add patients first.")
                else:
                    key = int(input("Patient ID:"))
                    id, name, age, sex, p_blood_group, address, appointed_doctor, appointment_date = patients.__getitem__(
                        key)
                    print('\nDetails of Patient ID-', key)
                    print("-------------------------")
                    print("Patient Name:", name, "\nAge:", age, "\nSex:", sex, '\nBlood group:', p_blood_group,
                          "\nAddress:",
                          address, "\nAppointed Doctor:",
                          appointed_doctor, "\nAppoinment Date:", appointment_date)
                    print("\n")
                    input("(Press any key to go back.)\n")
                    break

            elif choice2 == 3:
                break
            else:
                print("Enter a valid choice.")

            # ------------------------------------------Doctor-------------------------------------------------
    elif choice1 == '2':
        while True:
            print("\nDoctor's Corner")
            print("-----------------")
            print("1.Department-wise doctor list\n2.Back")
            choice3 = input("\nEnter your choice:\n")

            if choice3 == '1':
                print("List of Departments: ", "\n--------------------"'\n1.Cardiology', '\n2.Gynecology',
                      '\n3.Gastroenterology',
                      '\n4.Neurology', '\n5.Psychiatrists')
                print("--------------------")
                d = int(input("Enter your choice: "))
                dept = lst[d - 1]
                print("\nDoctor's list: ")
                print("--------------")
                for k in dept:
                    id, name, age, sex, designation, chamber_day, chamber_time, fees = dept[k]
                    print('Doctor ID:', id, '\nName:', name, '\nAge:', age, '\nSex:', sex, '\nDesignation:',
                          designation,
                          '\nChamber Day:', chamber_day, '\nChamber Time:', chamber_time, "\nFees:", fees)
                    print("\n")
                input("Press any key to go back..")
                break
            elif choice3 == '2':
                break
            else:
                print("Please Enter a valid choice..")

    elif choice1.upper() == 'E':
        break
    else:
        print("Enter a valid choice:..")
