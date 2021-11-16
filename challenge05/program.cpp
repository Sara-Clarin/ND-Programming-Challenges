#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<cstring>

using namespace std;

#define ll long long




void find_max_cycle( ll i, ll j){
    map<int, int> collatz;
    ll n, count, start, end;

    if (i > j){
        start = j; end = i;
    } else {
        start = i; end = j;
        } 

    for ( int a = start; a <= end; a++){
        n = a;
        count = 1;
        while ( n > 1){

            if (n % 2)      // if n is odd
                n = 3*n + 1;

            else{           // n is even
                n = n/2;
            }
         
            count += 1;
        }

        if ( !collatz[count]){      // don't overwrite collisions
             collatz[count] = a;
        }
    }    

    // Find and report max count and argmax count
    auto m = std::max_element(
        std::begin(collatz), std::end(collatz) 
    );

    cout << i<< " " << j<< " " <<  m->second << " " << m->first << endl;
    collatz.clear();
}


int main(int argc, char * argv[]){

    int i; int j;
    char* buf1; 
    char buffer[BUFSIZ];
    
    while (fgets(buffer, BUFSIZ, stdin)){
        buf1 = strtok( buffer, " ");
        i = atoi( buf1);
        buf1 = strtok(NULL, " ");
        j = atoi(buf1);

        find_max_cycle( i, j);

    }

return 0;
}
