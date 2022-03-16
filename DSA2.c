#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node * next;
};

struct node *create_list()
{

struct node *head, *tmp;
int i,n;

printf("How many elements you want to create:");
scanf("%d",&n);

   for(i=0; i<n; i++){
	if(i==0){
	head=malloc(sizeof(struct node));
        tmp = head;
	}
        else {
	tmp->next = malloc(sizeof(struct node));
 	tmp = tmp->next;
	}
    printf("Enter Node %d:",i+1);
    scanf("%d", &tmp->data);
   }
tmp->next = NULL;
return(head);

}

struct node *front(struct node *head, int value){
	struct node *tmp;

	tmp = malloc(sizeof(struct node));
	tmp ->data = value;
    tmp ->next = head;
	return (tmp);
}


struct node *end(struct node *head, int value){
	struct node *tmp, *prev;

	tmp = malloc(sizeof(struct node));
	tmp ->data = value;
        tmp ->next = NULL;

	prev=head;
	while(prev->next != NULL)
	{
	prev = prev -> next;
	}
	prev->next = tmp;
}

struct node *middle(struct node *a, int value)
{
	if(a->next != NULL)
	{
	struct node *tmp;
	tmp = malloc(sizeof(struct node));
	tmp ->data = value;
	tmp -> next= a->next;
	a->next = tmp;
	}

}

void delete_front(struct node *head)
{
	struct node *tmp;
	tmp = head;
	head = head -> next;
	free(tmp);

}

void delete_end(struct node *head)
{
	struct node *tmp, *prev_node;
        if(head->next == NULL){
	  free(head);
	  head = NULL;
	}
	tmp = head;
	while(tmp->next != NULL){
	prev_node = tmp;
	tmp = tmp ->next;
	}
	free(tmp);
	prev_node->next = NULL;
	
}
void print(struct node* p)
{
while(p!=NULL)
{
    printf("elements are %d ",p->data);
    p=p->next;
}
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
	struct node *head, *temp;
	head=create_list();
	head = front(head,10);
	end(head, 50);
	middle(head->next->next, 40);

	

	temp = head;int i=0;
	while(temp !=NULL){
	  printf("%d\t", temp -> data);
	  temp = temp->next;
      i++;
	}
        printf("\n");int k;
        if(i%2!=0)
       k=i/2+1;
        else
        k=i/2;
delete_middle(head,k);
print(head);
     	delete_front(head);
	delete_end(head);

	temp = head;
	while(temp !=NULL){
	  printf("%d\t", temp -> data);
	  temp = temp->next;
	}
        printf("\n");
	return 0;
        
}