#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<iostream>
#include<unistd.h>
#include<vector>
#include<iterator>

using namespace std;


int main(int argc, char * argv[]){
    
    char buffer[BUFSIZ];
    int M = -1;
    int N = -1;
    int matrixNumber = 1;
    cin >> N;
    cin >> M;

/*  Continuously read stdin line-by-line    */
    while (fgets(buffer, BUFSIZ, stdin)){
        if (M == 0 && N == 0){              // use sentinel
            break;
        }
        
        int arr[N][M], temp;

/*  Store the input in a 2D array  */

        for (int i = 0; i < N; i++){    
            for (int j = 0; j < M; j++){
                cin >> temp;
                arr[i][j] = temp;
                }
        }

/*  Calculate minimum four square  */
        int min = 1000; 
        int sum = 0;
        for (int row = 0; row < N -1 ; row++){
            for (int col = 0; col < M - 1; col++){
                sum = arr[row][col] + arr[row][col+1] + arr[row+1][col] + arr[row+1][col+1];
                if (sum < min){
                    min = sum;
                    }
             }
         }
       
        cout << matrixNumber << ". Minimum four square is: " << min << endl;
        matrixNumber++;
        cin >> N;
        cin >> M;
    }

    return 0;
}
