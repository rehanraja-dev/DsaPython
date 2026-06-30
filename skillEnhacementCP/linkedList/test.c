#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node* next;
};

void delete(struct Node** head_ref){
    struct Node* temp;
    int trash;

    if(*head_ref==NULL){
        printf("Empty List");
        exit(0);
    }
    else{
        temp = *head_ref;
        trash = temp -> data;
        *head_ref = temp -> next;

    }
}

void deleteAtPosition(struct Node** head_ref, int posi) {
    if (*head_ref == NULL) {
        printf("List is empty, nothing to delete.\n");
        return;
    }

    if (posi < 1) {
        printf("Invalid position!\n");
        return;
    }

    struct Node* temp = *head_ref;

    if (posi == 1) {
        *head_ref = temp->next; 
        free(temp);      
        return;
    }

    for (int i = 1; temp != NULL && i < posi - 1; i++) {
        temp = temp->next;
    }

    if (temp == NULL || temp->next == NULL) {
        printf("Position out of bounds!\n");
        return;
    }

    struct Node* next_node = temp->next->next; 
    free(temp->next);                          
    temp->next = next_node;                    
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

void insertAtAnyPosition(struct Node** head_ref, int value, int posi){
    if (posi < 1) {
        printf("Invalid position!\n");
        return;
    }

    if (posi == 1) {
        insertBeggining(head_ref, value);
        return;
    }

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory is not allocated\n");
        return;
    }
    newNode->data = value;

    struct Node* temp = *head_ref;
    for (int i = 1; temp != NULL && i < posi - 1; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Position out of bounds! Maximum available position was exceeded.\n");
        free(newNode); 
        return;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}


void insertLast(struct Node** head_ref, int value){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if(newNode == NULL){
        printf("Memory is not allocated\n");
        return;
    }
    
    newNode -> data = value;
    newNode -> next = NULL;
    if (*head_ref == NULL)
    {
        *head_ref = newNode;
    }
    else{
        struct Node* temp = *head_ref;
        while (temp -> next != NULL)
        {
            temp = temp -> next; 
        }
        temp -> next = newNode;
    }
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
    insertBeggining(&head, 15);
    insertBeggining(&head, 20);
    insertBeggining(&head, 30);
    insertBeggining(&head, 40);
    display_list(head); 
    insertLast(&head,20);
    insertAtAnyPosition(&head, 100,2);
    display_list(head); 
    delete(&head);
    display_list(head); 
    deleteAtPosition(&head,3);
    display_list(head); 
    return 0;
}