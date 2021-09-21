#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
#include<string>
#include<numeric>

using namespace std;

void print_triplet( vector<int> &s){
    vector<int> v = s;
    //sort(v.begin(), v.end());
    int n = v.size();
    for (size_t i = 0; i < n -1; i++){
        cout << v[i] << " + ";
    }
    cout << v[n -1] << endl;

}

void get_triplets( vector<int> &s, vector<int> &d, size_t k){
        /* s: current elements
            d: set of elements
            k: current element to consider
        */
        // base case
        if (k == d.size()){
            int sum = accumulate(s.begin(), s.end(), 0);
            if (sum == 0 && s.size() == 3){
                /*for (auto a: s){
                    cout << a << " + ";
                        }
                cout << endl;
                */
                print_triplet(s);
            }
    
        }
        else{
            // don't take current element
            get_triplets(s, d, k+1);
            // take current element
            s.push_back( d[k]);
            get_triplets( s, d, k+1);
            s.pop_back( );
        }

}

void find_triplets_iterative( vector<int> &s){

    for (int i = 0; i < s.size(); i++){
        int mid = i + 1;
        int end = s.size() -1;

        if (i > 0 && s[i] == s[i-1]){
            continue;
        }

        // start from second index and iterate all other options
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
    char * buf;
    char buffer[BUFSIZ];
    string line;
    int i;   
    vector<int> s;
 
    while ( getline(cin, line)){
        istringstream ss(line);
        vector<int> d;
        while( ss >> i){
            d.push_back(i);
        }

        sort(d.begin(), d.end());
        /*
        for (auto e: d){
            cout << e << " ";
        } cout << endl; */

        find_triplets_iterative(d );
        s.clear();
        d.clear();
     
    }


return 0;

}
