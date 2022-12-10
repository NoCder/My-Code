/*
--EN--
A program that lets you see how many times a specific symbol appears on a line of text.
Both text lines and symbols are entered by the user. The text line must be saved as a string of low-level symbols in the program.
[You must be able to repeat the program without leaving the program.]

--LV--
Programma, kas ļauj noskaidrot, cik reizes teksta rindiņā ir sastopams konkrēts simbols. 
Gan teksta rindiņu, gan simbolu ievada lietotājs. Teksta rindiņa jāsaglabā programmā kā zema līmeņa simbolu virkne. 
[Jābūt iespējai programmu izpildīt atkārtoti, neizejot no programmas.]
*/
#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int ok=1;
    do{

        //Variables declaration
        char str[81];
        char simb;
        int counter=0;
        //User's inputs
        cout << "Enter a string, that are no longer than 80 characters: \n";
        cin.getline(str, 81);
        cout << "Enter a finding symbol: \n";
        cin.get(simb);
        //Find a matching symbol and count.
        for(int i=0; i<strlen(str); i++){
            if(str[i]==simb){
                counter++;
            }
        }
        //Prints answers
        cout << "In text there are " << counter << " matching symbols - " << simb << endl;

        //Repeatable program
        cout << "Do you want continue? If yes (1), no (0) \n";
        cin >> ok;
        cin.ignore();
    }while(ok==1);
}