#include<stdio.h>
#include<stdlib.h>
struct stud_record
{
int roll_no;
char name[20];
float marks[3];
};
void swap(struct stud_record **p,struct stud_record **q){
   struct stud_record **temp=p;
    **p=**q;**q=**temp;
}
struct stud_record ** sorted(struct stud_record * record_array[],int n){
for(int i=0;i<n-1;i++){
    if(record_array[i]>record_array[i+1])
    swap(&record_array[i],&record_array[i+1]);
}
return record_array;
}
 struct stud_record ** record_search(struct stud_record * record_array[], int n, int roll){
for(int i=0;i<n;i++){
if((record_array[i])==roll)
return record_array;
}
return NULL;
 }
int main(){
    struct stud_record* record_array;
    int n,a;
    printf("enter size of record :");
    scanf("%d",&n);
     record_array=malloc(n*sizeof(struct stud_record));
     for(int i=0;i<n;i++){
         printf("enter roll_no,name,marks of student :");
         scanf("%d ",&record_array->roll_no);
          scanf("%s ",&record_array->name);
           scanf("%f",&record_array->marks);
     }
     record_array=sorted(&record_array,n);
     printf("enter rollno. to be searched :");
     scanf("%d",&a);
     record_array=record_search(&record_array,n,a);
     printf("%d",&record_array->roll_no);
          printf("%s",&record_array->name);
           printf("%f",&record_array->marks);
     return 0;
}
