/*
--EN--
A program that allows you to enter whole numbers and calculates the amount of negative numbers.
The input must be stopped when the number 0 is entered.
[You must be able to repeat the program without leaving the program.]

--LV--
Programma, kura ļauj ievadīt veselus skaitļus un aprēķina negatīvo skaitļu summu. 
Ievade jābeidz tad, kad ievadīts skaitlis 0.
[Jābūt iespējai programmu izpildīt atkārtoti, neizejot no programmas.]
*/
#include <iostream>
using namespace std;

int main(){
    int ok;
    do {
        int sum, digit;
        cout << "Enter a whole numbers: \n";
        cin >> digit;

        while (digit != 0){
            if(digit<0) sum+=digit;
            cin >> digit;
        }
        cin.ignore(10000, '\n');
        
        if(sum<0){
            cout << "Sum of negative numbers is " << sum << endl;
        }else{
            cout << "There is no negative number" << endl;
        }

        cout << "Do you want continue? If yes (1), no (0) \n";
        cin >> ok;
        cin.ignore(10000, '\n');
    }while(ok==1);
}