#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100000

typedef struct snowflake_node {
    int snowflake[6];
    struct snowflake_node *next;
} snowflake_node;

int code(int snowflake[]){
    return (snowflake[0] + snowflake[1] + snowflake[2] + snowflake[3] + snowflake[4] + snowflake[5]) % SIZE;
}

void identify_identical(snowflake_node *snowflakes[]){
    snowflake_node *node1, *node2;
    int i;
    for (i = 0; i < SIZE; i++){
        node1 = snowflakes[i];
        while (node1 != NULL){
            node2 = node1->next;
            while (node2 != NULL){
                if (memcmp(node1->snowflake, node2->snowflake, sizeof(int) * 6) == 0){
                    printf("Twin snowflakes found.\n");
                    return;
                }
                node2 = node2->next;
            }
            node1 = node1->next;
        }
    }
    printf("No two snowflakes are alike.\n");
}


int main(void){
    static snowflake_node *snowflakes[SIZE] = {NULL};
    snowflake_node *snow;
    int n, i, j, snowflake[6];
    scanf("%d", &n);
    for (i = 0; i < n; i++){
        snow = (snowflake_node *)malloc(sizeof(snowflake_node));
        for (j = 0; j < 6; j++)
            scanf("%d", &snow->snowflake[j]);
        j = code(snow->snowflake);
        snow->next = snowflakes[j];
        snowflakes[j] = snow;
    }
    identify_identical(snowflakes);
    
    for(i = 0; i < SIZE; i++){
        snow = snowflakes[i];
        while(snow != NULL){
            snowflake_node *temp = snow;
            snow = snow->next;
            free(temp);
        }
    }

    return 0;
}