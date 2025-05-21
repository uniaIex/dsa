/*

basic linked list implementation in C

 */

#include <stdio.h>
#include <stdlib.h>

// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void printList(Node* node)
{
    while (node)
    {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("null\n");
}

int main()
{
    Node* node1 = createNode(1);
    Node* node2 = createNode(2);
    Node* node3 = createNode(3);
    Node* node4 = createNode(4);
    Node* node5 = createNode(5);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    printList(node1);

    // Free the allocated memory

    free(node5);
    free(node4);
    free(node3);
    free(node2);
    free(node1);

    return 0;

}