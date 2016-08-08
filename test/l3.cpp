#include <stdio.h>

int t,casenum,n,m;
long long  ans;
long long  dp[10][2000] = {0,};
void pre()
{
    int sum, i, k, j, v;
    for ( i=0; i<2000; ++i)
        dp[0][i]=1;
    for ( k=1; k<10; ++k){
        for ( j=1; j<=2000; ++j){
            if ( dp[k-1][j-1]!=0 ){
                for ( v=j*2; (v<=2000)&&(v<=j*3); ++v){
                    dp[k][v-1]+=dp[k-1][j-1];
                }
            }
        }
    }
}
int main(int argc, char *argv[])
{
   int i, j;
    pre();
    scanf("%d", &t);
    casenum=0;
    while (t-- ){
        ++casenum;
        scanf("%d %d", &n, &m);
        ans=0;
        for (i=0; i<m; ++i)
           ans+=dp[n-1][i];
        printf("%lld\n", ans );
    }
    return 0;
}