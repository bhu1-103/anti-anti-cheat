#include<stdio.h>
int main()
{
    int arr[4][4] = {{2,0,0,0},{2,0,0,0},{0,0,0,0},{0,0,0,0}};
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    
    while(1>0)
    {
    printf("\n\n\n");
    printf("Enter a key\n");
    printf("A -> LEFT\n");
    printf("D -> RIGHT\n");
    printf("W -> UP\n");
    printf("S -> DOWN\n");
    char choice;

    scanf(" %c", &choice);
    printf("%c has been pressed", choice);
    
    }
    return 0;
}
