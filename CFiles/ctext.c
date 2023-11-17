#include <conio.h>
#include <stdio.h>
#include <string.h>

int main_fun(){
    char string[] = "abc/qwe/jkh/SDD/dF";
char *array[10];
int i = 0;


array[i] = strtok(string, "/");

while(array[i] != NULL)
   array[++i] = strtok(NULL, "/");
for (i = 0; i < 10; ++i) 
        printf("%s\n", array[i]);
printf("value of num = %d\n", **array);
return 0;
}