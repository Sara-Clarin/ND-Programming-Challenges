#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<cstring>

using namespace std;

#define ll long long

void find_max_cycle( ll i, ll j){
    map<int, int> collatz;
    int  max_length, max_key;
    ll n, count, start, end;
    //printf("i is: %d, j is %d", i, j);
    if (i > j){
        start = j; end = i;
    } else {
        start = i; end = j;
    }
    for ( int a = start; a <= end; a++){
        n = a;
        count = 1;
        while ( n > 1){
            //count += 1;

            if (n % 2)      // if n is odd
                n = 3*n + 1;

            else{           // n is even
                n = n/2;
            }
         
            count += 1;
        }
        
         collatz[count] = a;
    }    

   /*
    for (auto e: collatz){
        cout << e.first << " , " << e.second << endl;
    } */


    // Find and report max count and argmax count
    auto m = std::max_element(
        std::begin(collatz), std::end(collatz) 
    );

    //cout << "maximum: ";
    cout << i<< " " << j<< " " <<  m->second << " " << m->first << endl;
    collatz.clear();

}
int main(int argc, char * argv[]){

    int i; int j;
    char* buf1; char* buf2;
    char buffer[BUFSIZ];
    
    while (fgets(buffer, BUFSIZ, stdin)){
     /* while( cin >> buf1 ){
        //cin >> buf1;
        cin >> buf2;
        i = stoi(buf1);
        j = stoi(buf2);
        //printf(" i is: %d, j is %d", i, j);
       */
        buf1 = strtok( buffer, " ");
        i = atoi( buf1);
        buf1 = strtok(NULL, " ");
        j = atoi(buf1);

        find_max_cycle( i, j);

    }

return 0;
}
