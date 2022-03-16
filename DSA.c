#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
};
void linkedlist(struct node* head)
{
    struct node* p=head;
    printf("element are %d ",p->data);p=p->next;
    while(p!=head)
    {
        printf("elements are %d ",p->data);
        p=p->next;
    }
}
int main()
{
    struct node* head=(struct node*)malloc(sizeof(struct node));
    struct node* second=(struct node*)malloc(sizeof(struct node));
    struct node* third=(struct node*)malloc(sizeof(struct node));
head->data=4;
head->next=second;
second->data=66;
second->next=third;
third->data=89;
third->next=head;
linkedlist(head);
return 0;
}