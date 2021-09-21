#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
#include<string>
#include<numeric>

/*
Challenge07: finding unique subsets of sum 0 with size 3

*/
using namespace std;


void find_triplets_iterative( vector<int> &s){

    for (int i = 0; i < s.size(); i++){
        int mid = i + 1;
        int end = s.size() -1;

        if (i > 0 && s[i] == s[i-1]){
            continue;
        }

        //  iterate all other options after current index
        while (mid < end){
            if ( end < s.size() -1 && s[end] == s[end +1]){  // duplicates adjacents
                end --;
                continue;
            }

            if ( s[i] + s[mid] + s[end] > 0){ // sum too large: go backwards
                end --;
            }else if ( s[i] + s[mid] + s[end] < 0){ // sum to small: go forwards
                mid ++;
            }else {                                 // sum = 0

                cout << s[i] << " + " << s[mid] << " + " << s[end] << endl;
                mid++;
                end--;
            }
         }
    }
}

int main( int argc, char **argv){
    string line;
    int i;
    int  co = 0; 
    vector<int> s;

    while( getline(cin, line) ){
       if (co != 0){              // ensure correct formatting
         cout << endl; 
         }

        istringstream ss(line);
        vector<int> d;
        while( ss >> i){
            d.push_back(i);
        }

        sort(d.begin(), d.end());

        find_triplets_iterative(d );
        s.clear();                  // space efficiency
        d.clear();
        co++;
    }


return 0;

}
