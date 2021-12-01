#include <iostream>
#include <fstream>
#include <deque>
#include <string>

using namespace std;

string shunting_yard_1(string expression){
    expression.erase(remove_if(expression.begin(), expression.end(), isspace), 
                    expression.end());
    string output = "";
    string op = "";
    for (int i=0; i < expression.size(); i++){
        char token = expression[i];
        if (isdigit(token)){
            output.push_back(token);
        }
        else{
            switch (token){
                case '(':
                    op.push_back(token);
                    break;
                case ')':
                    while (op.back()!= '('){
                        output.push_back(op.back());
                        op.pop_back();
                    }
                    op.pop_back();
                    break;
                default:
                    while (!op.empty() && op.back() != '('){
                        output.push_back(op.back());
                        op.pop_back();
                    }
                    op.push_back(token);
            }
        }
    }
    return output + op;
}

string shunting_yard_2(string expression){
    expression.erase(remove_if(expression.begin(), expression.end(), isspace), 
                    expression.end());
    string output = "";
    string op = "";
    for (int i=0; i < expression.size(); i++){
        char token = expression[i];
        if (isdigit(token)){
            output.push_back(token);
        }
        else{
            switch (token){
                case '*':
                    while (!op.empty()&&op.back()!='('){
                        output.push_back(op.back());
                        op.pop_back();
                    };
                    op.push_back(token);
                    break;
                case ')':
                    while (op.back()!= '('){
                        output.push_back(op.back());
                        op.pop_back();
                    }
                    op.pop_back();
                    break;
                default:
                    op.push_back(token);
            }
        }
    }
    while (!op.empty()){
        output.push_back(op.back());
        op.pop_back();
    }
    return output;
}


int64_t rpn(string expression){
    deque<int64_t> output;
    for (int i=0; i<expression.size(); i++){
        char token = expression[i];
        if (isdigit(token)){
            int t = token - '0';
            output.push_back(t);
        }
        else{
            int64_t x = output.back();
            output.pop_back();
            int64_t y = output.back();
            output.pop_back();
            switch (token)
            {
            case '+':
                output.push_back(x+y);
                break;
            case '*':
                output.push_back(x*y);
                break;
            }
        }
    }
    return output.back();
}

int64_t evaluate1 (string expression){
    int64_t x = rpn(shunting_yard_1(expression));
    return x;
}

int64_t evaluate2 (string expression){
    int64_t x = rpn(shunting_yard_2(expression));
    return x;
}

void main() {
    string line;
    int64_t acc1 = 0;
    int64_t acc2 = 0;
    ifstream input("input.txt");
    if (input.is_open()){
        while (getline(input, line))
        {
            acc1 += evaluate1(line);
            acc2 += evaluate2(line);
        }
    cout << acc1 << endl << acc2 << endl;   
    }
    else {cout << "input error";}
}