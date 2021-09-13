#include<iostream>
#include<string>
#include<map>
#include<algorithm>

using namespace std;

void find_max_cycle( int i, int j){
    map<int, int> collatz;
    int n, count, max_length, max_key;
    //printf("i is: %d, j is %d", i, j);

    for ( int a = i; a <= j; a++){
        n = a;
        count = 1;
        while ( n > 1){
            count += 1;

            if (n % 2)
                n = 3*n + 1;

            else
                n = n/2;
        }
        
         collatz[count] = a;
    }    


    /*for (auto e: collatz){
        cout << e.first << " , " << e.second << endl;
    } */


    // Find and report max count and argmax count
    auto m = std::max_element(
        std::begin(collatz), std::end(collatz)
    );

    //cout << "maximum: ";
    cout << i<< " " << j<< " " <<  m->second << " " << m->first << endl;


}
int main(int argc, char * argv[]){

    int i; int j;
    char* buf1;
    char buffer[BUFSIZ];
    
    while (fgets(buffer, BUFSIZ, stdin)){
         buf1  = strtok( buffer, " " );
         i = atoi( buf1);
         buf1 = strtok(NULL, " ");
         j = atoi(buf1);

        //printf(" i is: %d, j is %d", i, j);
       
        find_max_cycle( i, j);


    }




return 0;
}
