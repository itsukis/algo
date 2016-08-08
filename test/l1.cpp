#include<stdio.h>
#include<string.h>
char MorseCode[26][5]={".-","-...","-.-.","-..",".","..-.","--.","....","..",
                   ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-","-.--","--.." }; //모스 부호
int main(){
   int N, n, l, i;
   char Morse[5];
   char Decode, temp;

   scanf("%d", &N); // 단어 수 입력
    for(n=0; n<N; n++){ //단어 수 만큼 반복
      printf("Case %d: ", n+1); //"Case n: " 출력
        for(l = 0; l<5; l++){     //한 단어 내에서 모스부호를 알파벳으로 변환
         scanf("%s", Morse);
         Decode = 'A';
         for(i=0; i<26; i++){
            if(!strcmp(Morse, MorseCode[i])){
               Decode +=i;
               break;
            }
         }
            temp = Decode-3;  //카이사르 암호 복호화
            if(temp<'A'){
                temp='Z'-3+(Decode-'A'+1);
            }
         printf("%c", temp); //변환된 한 글자 출력
        }
      printf("\n");
    }
   return 0;
}