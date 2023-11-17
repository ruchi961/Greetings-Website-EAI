#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char *main()
{
    FILE* fp = fopen("D:/EAI/CFiles/Subscription.csv", "r");
    char *code;
    size_t n = 0;
    int c;
  char t;
    if (fp== NULL) return NULL; //could not open file
    fseek(fp, 0, SEEK_END);
    int f_size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    code = malloc(f_size);
    printf("%ld",f_size);
    code[n++]=(char)f_size;
    while ((c = fgetc(fp)) != EOF) {
        code[n++] = (char)c;
    }

    code[n] = '\0'; 
    return code;
}