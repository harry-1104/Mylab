#include <stdio.h>

int main(){
    printf("Enter name: ");
    char name[50];
    fgets(name, 50, stdin);
    printf("Hello %s", name);
    return 0;
}