# Konrad Kolber 4/22/26

class EmployeeClass:
    def __init__(self, employeename, employeesalary):
        self.employeename = employeename
        self.employeesalary = employeesalary

    def calculatebonus(self, bonusratevalue):
        bonusamountvalue = self.employeesalary * bonusratevalue
        return bonusamountvalue


class StudentClass:
    def __init__(self, firstnamevalue, lastnamevalue, districtcodevalue, creditsvalue):
        self.firstnamevalue = firstnamevalue
        self.lastnamevalue = lastnamevalue
        self.districtcodevalue = districtcodevalue
        self.creditsvalue = creditsvalue

    def calculatetuition(self):
        if self.districtcodevalue == "I":
            tuitionamountvalue = self.creditsvalue * 250
        else:
            tuitionamountvalue = self.creditsvalue * 500
        return tuitionamountvalue


def main():
    print("EMPLOYEE PART")
    employeenamevalue = input("Enter employee name: ")
    employeesalaryvalue = float(input("Enter employee salary: "))
    bonusratevalue = float(input("Enter bonus rate (like 0.10): "))

    employeeobject = EmployeeClass(employeenamevalue, employeesalaryvalue)
    bonusresultvalue = employeeobject.calculatebonus(bonusratevalue)

    print("Employee bonus is", bonusresultvalue)

    print("")
    print("STUDENT PART")

    studentfirstnamevalue = input("Enter student first name: ")
    studentlastnamevalue = input("Enter student last name: ")
    districtcodevalue = input("Enter district code (I or O): ")
    creditsvalue = float(input("Enter credits: "))

    studentobject = StudentClass(studentfirstnamevalue, studentlastnamevalue, districtcodevalue, creditsvalue)
    tuitionresultvalue = studentobject.calculatetuition()

    print("Tuition owed is", tuitionresultvalue)


main()