#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int tree_count(int slope[2]){
    int slope_x = slope[0];
    int slope_y = slope[1];
    string line;
    vector<string> map;
    int x = 0;
    int y = 0;
    int trees = 0;
    ifstream input ("input.txt");
    if (input.is_open()){
        while (getline(input,line)){
            int width = line.size();
            if (y%slope_y == 0){
                if (line[x] == '#'){
                    trees++;
                }
                x=(x+slope_x)%width;
            }
            y++;
        }
        input.close();
    }
    return trees;
}


void main(){
    int p1[2] = {3,1};
    int p2[5][2] = {{1,1},{3,1},{5,1},{7,1},{1,2}};
    int acc = 1;
    for (int i=0; i<5; i++){
        acc *= tree_count(p2[i]);
    }
    cout << tree_count(p1) << endl;
    cout << acc << endl;
}