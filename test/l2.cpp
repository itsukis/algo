#include<stdio.h>
#include<stdlib.h>
int main(){
   int w, h, p, q, t;
   int x, y;
   int N, i;

   scanf("%d", &N);

   for(i=0; i<N; i++){
      scanf("%d %d", &w, &h); //w, h입력
      scanf("%d %d", &p, &q); //p, q입력
      scanf("%d", &t);        //t 입력

      x = t%(2*w);
      y = t%(2*h);

      if(x <= p)   p -= x;
      else if (x<=(w+p)) p = abs(x-p);
      else p = 2*w - (x - p);

      if(y <= q) q -= y;
      else if(y<=(h+q)) q = abs(y-q);
      else q = 2*h - (y - q);


      printf("%d %d\n", p, q); // 결과 출력
   }
   return 0;
}