// C program to implement
// the above approach
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *loadfile()
{
    FILE* fp = fopen("D:/EAI/CFiles/Subscription.csv", "r");
    long lSize;
    char *buffer;

    
        if (fp == NULL)
    {
        printf("Could not open file ");
        return 0;
    }

    fseek( fp , 0L , SEEK_END);
    lSize = ftell( fp );
    rewind( fp );

    /* allocate memory for entire content */
    buffer = calloc( 1, lSize+1 );
    if( !buffer ) fclose(fp),fputs("memory alloc fails",stderr),exit(1);

    /* copy the file into the buffer */
    if( 1!=fread( buffer , lSize, 1 , fp) )
      fclose(fp),free(buffer),fputs("entire read fails",stderr),exit(1);

    /* do your work here, buffer is a string contains the whole text */
    
    fclose(fp);
    return buffer;
}