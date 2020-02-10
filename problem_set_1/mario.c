// This is the answer file to the `mario (more comfortable)` portion of the problem set: https://cs50.harvard.edu/x/2020/psets/1/

// #include <cs50.h> 
// Custom CS50 library with helper methods. Not available outside of CS50 IDE

#include <stdio.h>
#include <ctype.h>

void make_pyramid(int height)
{
    int hashes = 1;
    
    // each level of the pyramid
    for (int i = height; i > 0; i--)
    {
        // calculate spaces needed
        int spaces = height - hashes;

        // print the correct number of hashes and spaces on left side
        for (int s = 0; s < spaces; s++)
        {
            printf(" ");
        }
        for (int h = 0; h < hashes; h++)
        {
            printf("#");
        }

        // print middle seperator
        printf("  ");

        // print right side
        for (int rh = 0; rh < hashes; rh++)
        {
            printf("#");
        }
 
        // Move to next level
        printf("\n");
        hashes++;
    }    
}

int main(void)
{   
    int answer;

    do 
    {
        // answer = get_int("How tall should the pyramid be? (Enter 1-8)\n");

        // Unable to use the above line as it uses a custom library function that is inbuilt to the CS50 IDE.
        // `answer` is hardcoded instead for when running ourside of the CS50 environment.

        answer = 5

    } 
    while (answer > 8 || answer < 1); 

    make_pyramid(answer);
}
