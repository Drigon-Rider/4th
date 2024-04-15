#include <iostream>
#include <string>

using namespace std;

class Person {
private:
    string name;
    string country;
    string dateOfBirth;
    int height;
    int weight;

public:
    Person(const string& n, const string& c, const string& dob, int h, int w)
        : name(n), country(c), dateOfBirth(dob), height(h), weight(w) {}

    void displayInformation() const {
        cout << "+------------------------------------------+" << endl;
        cout << "| Person |" << endl;
        cout << "|------------------------------------------|" << endl;
        cout << "| Name: " << name << endl;
        cout << "| Country: " << country << endl;
        cout << "| Date of Birth: " << dateOfBirth << endl;
        cout << "| Height: " << height << " Feet" << endl;
        cout << "| Weight: " << weight << " kg" << endl;
        cout << "+------------------------------------------+" << endl;
    }
};

class Employee {
private:
    string occupation;
    double salary;
    string company;
    string location;

public:
    Employee(const string& occ, double sal, const string& comp, const string& loc)
        : occupation(occ), salary(sal), company(comp), location(loc) {}

    void displayInformation() const {
        cout << "+------------------------------------------+" << endl;
        cout << "| Employee |" << endl;
        cout << "|------------------------------------------|" << endl;
        cout << "| Occupation: " << occupation << endl;
        cout << "| Salary: " << salary << " lakhs per month" << endl;
        cout << "| Company: " << company << endl;
        cout << "| Location: " << location << endl;
        cout << "+------------------------------------------+" << endl;
    }
};

int main() {
    Person* ram = new Person("Ram", "Nepal", "15th December 1999", 6, 80);
    Employee* ramJob = new Employee("AI Researcher", 1.5, "info company", "Kathmandu");

    ram->displayInformation();
    ramJob->displayInformation();

    delete ram;
    delete ramJob;

    return 0;
}
