#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool check_signature(unsigned char *buffer);

int main(int argc, char *argv[])
{
    // Must only take one commandline arg
    if (argc != 2)
    {
        printf("Please include file in argument");
        return 1;
    }

    // Main buffer
    unsigned char *buffer = (unsigned char *)malloc(512 * sizeof(unsigned char));

    int jpegs = 0, blocks = 0;

    // OPen file and init
    FILE *file = fopen(argv[1], "r");
    FILE *img;

    // Init output file
    char *outfile = malloc(7 * sizeof(char));

    while (fread(buffer, 1, 512, file) == 512)
    {
        blocks++;

        if (check_signature(buffer) == true)
        {
            // if it's the first image, create new image and write
            if (jpegs < 1)
            {
                sprintf(outfile, "%03i.jpg", jpegs);
                jpegs++;
                img = fopen(outfile, "w");
                fwrite(buffer, 512, 1, img);
            }
            // else, close previous file before creating new jpg
            else
            {
                fclose(img);
                sprintf(outfile, "%03i.jpg", jpegs);
                jpegs++;
                img = fopen(outfile, "w");
                fwrite(buffer, 512, 1, img);
            }
        }
        else
        {
            // Check to see if there is curently a file being written
            if (jpegs > 0)
            {
                fwrite(buffer, 512, 1, img);
            }
        }

        // Go to next block in file
        fseek(file, 512 * blocks, SEEK_SET);
    }

    // Clear memory
    free(buffer);
    free(outfile);
}

// Checks if JPEG signature is found at the start of the array
bool check_signature(unsigned char *buffer)
{
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        return true;
    }
    return false;
}
