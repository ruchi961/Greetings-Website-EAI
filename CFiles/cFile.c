#include <conio.h>
#include <stdio.h>
#include <string.h>

int coutnLines(){
    FILE* fp = fopen("D:/EAI/CFiles/Subscription.csv", "r");
    int count = 0; // Line counter (result)
    char c; // To store a character read from file

 
    // Check if file exists
    if (fp == NULL)
    {
        printf("Could not open file ");
        return 0;
    }
 
    // Extract characters from file and store in character c
    for (c = getc(fp); c != EOF; c = getc(fp))
        if (c == '\n') {// Increment count if this character is newline
            count = count + 1;
        }
 
    // Close the file
    fclose(fp);
    printf("The file has %d lines\n ",count);
    return count;
}
// Driver Code
int main()
{
	// Substitute the full file path
	// for the string file_path
	FILE* fp = fopen("D:/EAI/CFiles/Subscription.csv", "r");
   int Rows = coutnLines();
   printf("%d",Rows);
   int arrayDim = (Rows-1)*4;
   char *returnArray[arrayDim];
   int j=0;
	if (!fp)
		printf("Can't open file\n");

	else {
		// Here we have taken size of
		// array 1024 you can modify it
		char buffer[1024];

		int row = 0;
		int column = 0;

		while (fgets(buffer,1024, fp)) {
			column = 0;
			row++;

			// To avoid printing of column
			// names in file can be changed
			// according to need
			if (row == 1)
				continue;

			// Splitting the data
			char* value = strtok(buffer, ", ");
         //printf("\tYearly Subscription :");
         //printf("%s", value);
         printf("\n");
			while (value) {
				// Column 1
				if (column == 0) {
					printf("\tPlan Name:");
            
               //returnArray[j++] = value;
               
				}

				// Column 2
				if (column == 1) {
					printf("\tMonthly Subscription  :");
               //returnArray[j++] = value;
				}

				// Column 3
				if (column == 2) {
					printf("\tYearly Subscription :");
               //returnArray[j++] = value;
				}
            if (column == 3) {
					printf("\tBenefits :");
               //returnArray[j++] = value;
               
               /*char* valueBenefits = strtok(Buffer, "-");
               while (valueBenefits){
               printf("%s", valueBenefits);
               valueBenefits = strtok(NULL, "-");
               //printf("%s", valueBenefits);
               }*/
				}
				printf("%s", value);
             returnArray[j++] = value;
				value = strtok(NULL, ", ");
            
				
               column++;
            
			

			
		}
      printf("\n");
      }
		// Close the file
		fclose(fp);
	}
int k;
   for(k=0;k<arrayDim;k++){    
printf("%s", returnArray[k]);    
}   
	return 0;
}

