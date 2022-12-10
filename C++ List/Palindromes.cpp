/*
--EN--
The program that checks whether the given string is the same as the inverted string.

--LV--
Programma, kura pārbauda vai dotais string ir tas pats kā apgriezts string.
*/
#include <iostream>
using namespace std;

bool isMirrored(string s){

    for(int i=0, j=s.length()-1; i<j; i++, j--){
        if(s[i]!=s[j]) return false;
    }
    return true;
}

int main(){
    string s1 = "abcba";
    string s2 = "abcdba";
    cout << (isMirrored(s1)) << endl;   // 1
    cout << (isMirrored(s2)) << endl;   // 0
}