#include<bits/stdc++.h>
using namespace std;
#include<string>

string reverseParentheses(const string& inputString) {
    stack<char> stk;
    
    for (char ch : inputString) {
        if (ch == ')') {
            string temp;
            //pop
            while (!stk.empty() && stk.top() != '(') {
                temp += stk.top();
                stk.pop();
            }
            //remove (
            if (!stk.empty()) stk.pop();

            for (char revCh : temp) {
                stk.push(revCh);
            }
        } else{
            stk.push(ch);
        }
    }
    
    string result;
    while (!stk.empty()) {
        result += stk.top();
        stk.pop();
    }
    reverse(result.begin(), result.end());
    
    return result;
}

int main() {
    string input1 = "(bar)";
    string input2 = "foo(bar)baz";
    string input3 = "foo(bar)baz(blim)";
    string input4 = "foo(bar(baz))blim";
    
    cout << "1: " << input1 << " output: " << reverseParentheses(input1) << endl;
    cout << "2: " << input2 << " output: " << reverseParentheses(input2) << endl;
    cout << "3: " << input3 << " output: " << reverseParentheses(input3) << endl;
    cout << "4: " << input4 << " output: " << reverseParentheses(input4) << endl;
    
    return 0;
}
