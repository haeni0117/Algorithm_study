#include <stdio.h>

int main(void){
  int i,j;
  int n;
  scanf("%d",&n);
  char matrix[n][n];
  for(int i =0;i<n;i++){
    for(int j=0;j<n;j++){ 
      if(i==n/2&&j==n/2)
      matrix[j][i]='0';
      else if(i==n/2){
        matrix[j][i]='+';
      }
      else if(j==n/2){  
        matrix[j][i]='I';
      }
     
      else if(i==n-j-1){
        matrix[j][i]='*';
      }
      else matrix[j][i]='.';
  }
}
    


for(int i =0;i<n;i++){
  printf("\n");
    for(int j=0;j<n;j++){ 
      printf("%c ",matrix[j][i]);}}
return 0;
}