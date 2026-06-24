#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node* next;
};

void insertLast(struct Node* head_ref, int value){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if(newNode == NULL){
        printf("Memory is not allocated\n");
        return;
    }
    
    newNode -> data = value;
    newNode -> next = NULL;
    head_ref = newNode;
}

void insertBeggining(struct Node** head_ref, int value){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if(newNode == NULL){
        printf("Memory is not allocated\n");
        return;
    }
    newNode -> data = value;
    newNode -> next = *head_ref;
    *head_ref = newNode;
}

void display_list(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main(){
    struct Node* head = NULL;
    insertBeggining(&head, 10);
    display_list(head); 
    insertLast(head,20);
    return 0;
}