/*
--EN--
A program that converts Fahrenheit to temperature in degrees Celsius.
Formula for conversion: C = 5/9(F-32)

--LV--
Programma, kura pārvērš Fārenheita grādos uzdotu temperatūru par temperatūru Celsija grādos. 
Formula pārvēršanai: C = 5/9(F-32)
*/
#include <iostream>
using namespace std;

int main(){
    int ok;
    do
    {
        double F, C;
        cout << "Enter a fahrenheit: ";
        cin >> F;
        C = 5.0/9*(F-32);

        cout << "In Celsius is " << C << endl;

        cout << "Do you want continue? If yes (1), no (0) \n";
        cin >> ok;

    } while (ok==1);
}