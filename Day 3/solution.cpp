#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void main(){
    string line;
    vector<string> map;
    int x = 0;
    int trees = 0;
    ifstream input ("input.txt");
    if (input.is_open()){
        while (getline(input,line)){
            int width = line.size();
            if (line[x] == '#'){
                trees++;
            }
            x=(x+3)%width;
        }
        input.close();
    }
    cout << trees;
}