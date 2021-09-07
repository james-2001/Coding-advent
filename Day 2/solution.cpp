#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

void main () {
    int p1acc = 0;
    string line;
    vector<vector<string>> input; 
    ifstream myfile ("input.txt");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            replace(line.begin(), line.end(), '-', ' ');
            string token[4];
            int i = 0;
            stringstream ssin(line);
            while (ssin.good() && i<4){
                ssin >> token[i];
                ++i;
            }
            int lower = stoi(token[0]);
            int upper = stoi(token[1]);
            string p = token[2];
            size_t n = count(token[3].begin(), token[3].end(), token[2][0]); 
            if (n<=upper && n>=lower){
                p1acc++;
            }

        }
        myfile.close();
    }
    else cout << "Unable to open file \n";
    cout << p1acc;
}
