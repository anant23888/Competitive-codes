#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
};
void print(struct node* p)
{
while(p!=NULL)
{
    printf("elements are %d ",p->data);
    p=p->next;
}
}
struct node* insertf(struct node* head,int d)
{
    struct node* p=(struct node*)malloc(sizeof(struct node));
    p->next=head;
p->data=d;
return p;
}
struct node* insertb(struct node* head,int d,int index)
{
struct node* p=(struct node*)malloc(sizeof(struct node));
struct node* ptr=head;
int i=0;
while(i!=(index-1)){
i++;
ptr=ptr->next;
}
p->data=d;
p->next=ptr->next;
ptr->next=p;
return head;
}
void delete_middle(struct node *head,int k)
{
	struct node *tmp, *prev_node;
        if(head->next == NULL){
	  free(head);
	  head = NULL;
	}
	tmp = head;int i=0;
	while(i!= (k-1)){
        i++;
	prev_node = tmp;
	tmp = tmp ->next;
	}
    prev_node->next = tmp->next;
	free(tmp);
	
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
third->next=NULL;
print(head);
head=insertf(head,9);
printf("\n");
print(head);
head=insertb(head,100,2);
printf("\n");
print(head);
delete_middle(head,3);
printf("\n");
print(head);
    return 0;
}
