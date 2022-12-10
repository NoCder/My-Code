/*
--EN--
The program that reads a sequence of integers from the standard input and outputs 
the integers in sorted order (i.e., in non-descending order). Use with sort();

--LV--
Programma, kas nolasa veselu skaitļu secību no standarta ievades un 
izvada veselus skaitļus sakārtotā secībā (t.i., nedilstošā secībā). Izmantojiet sort();
*/
#include <iostream>
#include <algorithm> //For sort();
#include <vector>
using namespace std;

int main()
{
    cout << "Enter a sequence of integers: ";
    vector<int> seq;
    int num;
    while (cin >> num)  //Stops when User inputs other than whole numbers
    {
        seq.push_back(num); //Pushs input's number inside vector
    }
    sort(seq.begin(), seq.end());   //Sorts vector's numbers

    cout << "Sorted sequence: ";
    for (int n : seq)
    {
        cout << n << " ";
    }
    cout << endl;
}