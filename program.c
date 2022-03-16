#include <stdio.h>
#include<stdlib.h>
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t-->0){
	    int n,x,y;
	    scanf("%d %d %d",&n,&x,&y);
	 int *a=(int *)malloc(n*sizeof(int));  
	  int *b=(int *)malloc(n*sizeof(int));  
	  for(int i=0;i<n;i++)
	  scanf("%d ",&a[i]);
	  for(int i=0;i<n;i++)
	  scanf("%d ",&b[i]);int j;
	  for( j=0;j<n;j++){
	     int l= b[j]-a[j];
	      if((l!=x)||(l!=y))
	      break;
	  }
	  if(j!=n)
	  printf("No\n");
	  else
	  printf("Yes\n");
	}
	return 0;
}

