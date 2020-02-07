// This is the answer file to the `mario (more comfortable)` portion of the problem set: https://cs50.harvard.edu/x/2020/psets/1/

#include <stdio.h>

int main(void)
{
    // int height = get_int("How tall should the pyramid be?\n");
    // Unable to use the above line as it uses a custom library function that is inbuilt to the CS50 IDE.
    // `height` is hardcoded instead for when running ourside of the CS50 environment

    int height = 5;
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
        printf(" ");

        // print right side
        for (int rh = 0; rh < hashes; rh++)
        {
            printf("#");
        }
        for (int rs = 0; rs < spaces; rs++)
        {
            printf(" ");
        }

        // Move to next level
        printf("\n");
        hashes++;
    }
}
