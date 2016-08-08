
#include<stdio.h>
#include<stdlib.h>
int M, N;
int flag;
int aggregate(int arr[][50], int i, int j);
int isOpen(int arr[][50], int i, int j);
int main(){
    int map1[50][50];
    int map2[50][50];
    int numCar;
    int numSnow;
    int numHour;
    int numWall;
    int i, j, a, b;
    int trial;
    scanf("%d", &trial);
    while(trial > 0)
    {
       numCar=0;  //초기화
       numSnow=0;
       numHour = 0;
        for(i = 0; i<50; i++){
            for(j=0;j<50;j++){
                map1[i][j] = 0;
                map2[i][j] = 0;
            }
        }

       scanf("%d %d", &M, &N);  // 입력
      for(i=0;i<N; i++){
         for(j = 0; j<M; j++){
            scanf("%d", &map1[i][j]);
            map2[i][j] = map1[i][j];
            if(map1[i][j] == 1)
            {
               numSnow++;
            }
         }
      }

      while(numSnow > 0){  // 눈 녹는데 걸리는 시간 산출
         numHour++;  //increase time stamp
         for(i=1;i<(N-1); i++){
            for(j = 1; j<(M-1); j++){
               if(map2[i][j] == 1){ // isSnow
                  numWall=0;
                  if(map2[i-1][j] == 0){ // up
                     flag = 0;
                     if(isOpen(map2, i-1, j))
                        numWall++;
                     for(a=0;a<(N); a++){
                        for(b = 0; b<(M); b++){
                           if(map2[a][b] == 2)
                              map2[a][b] = 0;
                        }
                     }
                  }
                  if(map2[i][j-1] == 0) // left
                  {
                     flag = 0;
                     if(isOpen(map2, i, j-1))
                        numWall++;
                     for(a=0;a<(N); a++){
                        for(b = 0; b<(M); b++){
                           if(map2[a][b] == 2)
                              map2[a][b] = 0;
                        }
                     }
                  }
                  if(map2[i+1][j] == 0) // down
                  {
                     flag = 0;
                     if(isOpen(map2, i+1, j))
                        numWall++;
                     for(a=0;a<(N); a++){
                        for(b = 0; b<(M); b++){
                           if(map2[a][b] == 2)
                              map2[a][b] = 0;
                        }
                     }
                  }
                  if(map2[i][j+1] == 0) // right
                  {
                     flag = 0;
                     if(isOpen(map2, i, j+1))
                        numWall++;
                     for(a=0;a<(N); a++){
                        for(b = 0; b<(M); b++){
                           if(map2[a][b] == 2)
                              map2[a][b] = 0;
                        }
                     }
                  }
                  if(numWall >= 2)
                  {
                     map2[i][j] = 3;
                     numSnow --;  // count down.
                  }
               }
            }
         }
         for(i=0;i<(N); i++){
            for(j = 0; j<(M); j++){
               if(map2[i][j] == 3)
                  map2[i][j] = 0;
            }
         }
      }

        for(i = 0; i<N; i++){  // 제설차량 대수
            for(j=0;j<M;j++){
                if(map1[i][j] == 1)
                {
                    aggregate(map1, i, j);
                    numCar++;
                }
            }
        }

        printf("%d %d\n", numHour, numCar);
        trial--;
    }
    return 0;
}

int aggregate(int arr[][50], int i, int j)
{
    arr[i][j] = 0;
    if(((i+1)<N) && (arr[i+1][j] == 1))
        aggregate(arr, i+1, j);
    if(((i-1)>=0) && (arr[i-1][j] == 1))
        aggregate(arr, i-1, j);
    if(((j+1)<M) && (arr[i][j+1] == 1))
        aggregate(arr, i, j+1);
    if(((j-1)>=0) && (arr[i][j-1] == 1))
        aggregate(arr, i, j-1);

    return 0;
}

int isOpen(int arr[][50], int i, int j)
{
    arr[i][j] = 2;
    if((i == 0) || (i == (N-1)) || (j == 0) || (j == (M-1)))
    {
        //if(arr[i][j] == 0)
        {
            flag = 1;
        }
        return flag;
    }
    if(!flag){
        if(arr[i-1][j] == 0)
            isOpen(arr, i-1, j);
        if(arr[i+1][j] == 0)
            isOpen(arr, i+1, j);
        if(arr[i][j-1] == 0)
            isOpen(arr, i, j-1);
        if(arr[i][j+1] == 0)
            isOpen(arr, i, j+1);

    }
    return flag;
}