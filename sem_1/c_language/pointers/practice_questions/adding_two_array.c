#include<stdio.h>

void add_array(){
    int arr1[5]={4,5,6,7,8};
    int arr2[5]={1,2,3,9,10};

    int add[5];

    for(int i=0;i<5;i++){
        add[i]=arr1[i]+arr2[i];
    }

    // printong sum

    for(int i=0; i<5;i++){
        printf("%d ", add[i]);
    }
}

int main(){

    add_array();

    return 0;
}

// ---------------------- with user input

#include <stdio.h>

int main() {
    int n, i;

    printf("Enter size of arrays: ");
    scanf("%d", &n);

    int a[n], b[n], sum[n];

    printf("Enter elements of first array:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter elements of second array:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &b[i]);

    for (i = 0; i < n; i++)
        sum[i] = a[i] + b[i];

    printf("Sum Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", sum[i]);

    return 0;
}
