
#include<stdio.h>
#include<stdlib.h>
#define bool int
 
// Data structure to store a binary tree node
struct tNode
{
    int data;
    struct tNode *left, *right;
};

struct sNode
{
    struct tNode *t;
    struct sNode *next;
};
 
void push(struct sNode **top_ref, struct tNode *t)
{
  /* allocate tNode */
  struct sNode* new_tNode = malloc(sizeof(struct sNode));
 
  if(new_tNode == NULL)
  {
     printf("Stack Overflow \n");
     exit(0);
  }
 
  /* put in the data  */
  new_tNode->t  = t;
 
  /* link the old list off the new tNode */
  new_tNode->next = (*top_ref);
 
  /* move the head to point to the new tNode */
  (*top_ref)    = new_tNode;
}

bool isEmpty(struct sNode *top)
{
   return (top == NULL)? 1 : 0;
}
 
/* Function to pop an item from stack*/
struct tNode *pop(struct sNode** top_ref)
{
  struct tNode *res;
  struct sNode *top;
 
  /*If sNode is empty then error */
  if(isEmpty(*top_ref))
  {
     printf("Stack Underflow \n");
     exit(0);
  }
  else
  {
     top = *top_ref;
     res = top->t;
     *top_ref = top->next;
     free(top);
     return res;
  }
}

void inorderIterative(struct tNode *root)
{
    // create an empty stack
    struct sNode *s = NULL;
    struct tNode *curr = root;
 
    // if the current node is null and the stack is also empty, we are done
    while (!isEmpty(s) || curr != NULL)
    {
        // if the current node exists, push it into the stack (defer it)
        // and move to its left child
        if (curr != NULL)
        {
            push(&s, curr);
            curr = curr->left;
        }
        else {
            // otherwise, if the current node is null, pop an element from the stack,
            // print it, and finally set the current node to its right child
            curr = pop(&s);
            printf("%d ", curr->data);
            curr = curr->right;
        }
    }
}

void preorderIterative(struct tNode *root)
{
    if (root == NULL)
        return;
 
    struct sNode *s = NULL;
    struct tNode *curr = root;
    
    if (curr != NULL) {
        push(&s, curr);}
    
    while (!isEmpty(s))
        {
            // pop a node from the stack and print it
            curr = pop(&s);
            printf("%d ", curr->data);
     
            // push the right child of the popped node into the stack
            if (curr->right) {
                push(&s, curr->right);
            }
     
            // push the left child of the popped node into the stack
            if (curr->left) {
                push(&s, curr->left);
            }
        }
    
}


struct tNode* newNode(int data)
{
  struct tNode *tmp = malloc(sizeof(struct tNode));
  tmp->data = data;
  tmp->left = NULL;
  tmp->right = NULL;
 
  return(tmp);
}
void postorderiterative(struct tNode* root)
{
if(root!=NULL){
    postorderiterative(root->left);
    postorderiterative(root->right);
    printf("%d ",root->data);
}
}

 
int main()
{
    /* Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    */
 
    struct tNode *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->right->left = newNode(5);
    root->right->right = newNode(6);
    root->right->left->left = newNode(7);
    root->right->left->right = newNode(8);
 
    preorderIterative(root);
    printf("\n");
    inorderIterative(root);
    printf("\n");
    postorderiterative(root);
    
 
    return 0;
}