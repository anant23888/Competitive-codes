#include<stdio.h>
#include<stdlib.h>
struct stack{
int size;
int top;
int *arr;
};
int isempty(struct stack* s)
{
    if(s->top==-1)
    return 1;
    return 0;
}
int isfull(struct stack* s){
    if(s->top==s->size-1)
    return 1;
    return 0;
}
void push(struct stack* s,int e){
    if(isfull(s))
    printf("stack is full ");
    else{
        s->top++;
        s->arr[s->top]=e;
    }
}
void pop(struct stack* s)
{
    if(isempty(s))
    printf("Stack underflow ");
    else{
        s->arr[s->top--];
    }
}
void display(struct stack* s)
{
    printf("elements are ");
    while(s->top>=0)
    {
        printf("%d ",s->arr[s->top]);
        s->top--;
    }
}
int peek(struct stack* s,int i)
{
    int arp=s->top-i+1;
    if(arp<0){printf("Invalid positon ");return -1;}
    else{
        return s->arr[arp];
    }
}
int main()
{
    struct stack *s=(struct stack* )malloc(sizeof(struct stack));
    s->size=10;
    s->top=-1;
    s->arr=(int *)malloc(s->size* sizeof(int));
    push(s,10);
     push(s,30); push(s,40); push(s,100);push(s,90); pop(s);pop(s);
     push(s,50);push(s,100);push(s,400);push(s,10);
     for(int j=1;j<=s->top+1;j++)
     {
         printf("position is %d of %d \n",j,peek(s, j));
     }
      printf("position is %d of %d \n",3,peek(s,3));
    return 0;
}