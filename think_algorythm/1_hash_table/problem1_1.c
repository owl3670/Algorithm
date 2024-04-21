#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100000

int identical_right(int snow1[], int snow2[], int start)
{
    int offset;
    for (offset = 0; offset < 6; offset++)
    {
        if (snow1[offset] != snow2[(start + offset) % 6])
            return 0;
    }
    return 1;
}

int identical_left(int snow1[], int snow2[], int start)
{
    int offset, snow2_index;
    for (offset = 0; offset < 6; offset++)
    {
        snow2_index = start - offset;
        if (snow2_index < 0)
            snow2_index = snow2_index + 6;
        if (snow1[offset] != snow2[snow2_index])
        {
            return 0;
        }
    }
    return 1;
}

int are_identical(int snow1[], int snow2[])
{
    int start;
    for (start = 0; start < 6; start++)
    {
        if (identical_right(snow1, snow2, start))
            return 1;
        if (identical_left(snow1, snow2, start))
            return 1;
    }
    return 0;
}

int compare(const void *first, const void *second) { 
    int i;
    const int *snowflake1 = first;
    const int *snowflake2 = second;
    if (are_identical(snowflake1, snowflake2))
        return 0;
    for (i = 0; i < 6; i++)
        if (snowflake1[i] < snowflake2[i])
            return -1;
    return 1;
}

void identify_identical(int snowflakes[][6], int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 1 + 1; j < n; j++) {
            if (are_identical(snowflakes[i], snowflakes[j])) {
                printf("Twin snowflakes found. \n");
                return;
            }
        }
    }
    printf("No wto snowflakes are alike.\n");
}


int main(void){
    static int snowflakes[SIZE][6];
    int n, i, j;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < 6; j++) {
            scanf("%d", &snowflakes[i][j]);
        }
    }
    identify_identical(snowflakes, n);
    return 0;
}