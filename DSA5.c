#include<stdio.h>
#include<stdlib.h>
struct cirqueue{
    int size;int f;int b;int *arr;
};
int isempty(struct cirqueue *s){
    if(s->f==s->b)return 1;
    return 0;
}
int isfull(struct cirqueue *s){
    if((s->b+1)%s->size==s->f)return 1;
    return 0;
}
void enqueue(struct cirqueue *s,int val){
    if(isfull(s)){
        printf("queue is overflowed ");
    }else{
        if(s->f==-1 && s->b==-1){
            s->f=0;s->b=0;
        }else {
     s->b=(s->b+1)%s->size;
     s->arr[s->b]=val;
    }}
}
void dequeue(struct cirqueue *s){
    if(isempty(s))printf("queue is full ");
    else{
        s->f=(s->f+1)%s->size;
    }
}
void printlist(struct cirqueue *s){
while(s->f!=(s->b+1)){
    printf("elements are %d \n",s->arr[s->f]);
    s->f=(s->f+1)%s->size;
}
}
int main()
{
struct cirqueue* s=(struct cirqueue *)malloc(sizeof(struct cirqueue));
s->size=5;
s->f=-1;s->b=-1;s->arr=(int*)malloc(s->size*sizeof(int));
enqueue(s,10);enqueue(s,11);enqueue(s,7);enqueue(s,12);enqueue(s,100);dequeue(s);dequeue(s);dequeue(s);enqueue(s,90);enqueue(s,16);printlist(s);
}