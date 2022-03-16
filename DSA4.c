#include<stdio.h>
#include<stdlib.h>
struct queue{
    int f;
    int b;
    int *arr;
    int size;
};
void enqueue(struct queue* s,int val){
     if(s->b==(s->size-1)){
        printf("queue is full ");
    }else {
        if(s->f==-1 && s->b==-1){
            s->f=0;s->b=0;
            s->arr[s->b]=val;
        }
        else{
            s->b++;
            s->arr[s->b]=val;
        }
    }
}
int dequeue(struct queue* s){
    if(s->f==s->b){
        printf("queue is empty");}
    else{
        s->f++;
    }
}
void printqueue(struct queue* s)
{
    while((s->f)<=(s->b)){
        printf("elememts are %d ",s->arr[s->f]);
        s->f++;
    }
}
int main()
{
    struct queue* s=(struct queue* )malloc(sizeof(struct queue));
    s->f=-1;s->b=-1;s->size=10;s->arr=(int *)malloc(s->size*sizeof(int));
enqueue(s,10);
enqueue(s,20);enqueue(s,30);enqueue(s,13);enqueue(s,100);dequeue(s);dequeue(s);
printqueue(s);
}