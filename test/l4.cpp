#include<stdio.h>
int main(){
    int T, i, j, p, q;
    int a, b, c, S, x, y, z, Sum;
    scanf("%d", &T);
    for(i = 0; i<T; i++){
        scanf("%d %d %d %d", &a, &b, &c, &S);
        Sum = -1;
      p = S/c;
      while(p >=0){
         q = (S-p*c)/b;
         while(q >= 0){
            if((S-p*c-b*q)%a == 0){
               if((Sum == -1) || (p + q + (S-p*c-b*q)/a) < Sum){
                  x = (S-p*c-b*q)/a;
                  y = q;
                  z = p;
                  Sum=x+y+z;
                  break;
               }
            }
            q--;
         }
         p--;
      }
      if(Sum == -1)
         printf("Impossible\n");
      else
         printf("%d %d %d\n", x, y, z);
    }
    return 0;
}