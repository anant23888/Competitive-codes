#include <stdio.h>
#include<stdlib.h>
void riffle(int *a,int n){int k=0;int l=n/2;
int *b;
b=(int *)malloc(n*sizeof(int));
for(int i=0;i<n;i++)
b[i]=a[i];
for(int i=0;i<n;i++){
    if(i%2==0)
    a[k++]=b[i];
    else
    a[l++]=b[i];
    
}
}
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n,k;
	    scanf("%d",&n);
	    scanf("%d",&k);
	    int *a;
	    a=(int *)malloc(n*sizeof(int));
	    for(int i=0;i<n;i++)
	    a[i]=i+1;
	    while(k>0){
	    riffle(a,n);
	    k--;}
	     for(int i=0;i<n;i++)
	     printf("%d ",a[i]);
		 printf("\n");
	    t--;
	}
	return 0;
}

