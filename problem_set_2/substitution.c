// Problem set instructions: https://cs50.harvard.edu/x/2020/psets/2/substitution/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


int alphabet_indices(char letter)
{
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    int indices = 1000; // Arbitary number to outside of a real alphabet array length.

    for (int i = 0; i < strlen(alphabet); i++)
    {
        if (tolower(letter) == alphabet[i])
        {
            indices = i;
            break;
        }
    }

    return indices;
}


int main(int argc, string argv[])
{
    // Get Key from commandline arg
    if (argc == 2)
    {
        string KEY = argv[1];
        int key_length = strlen(KEY);

        if (key_length == 26)
        {
            // Check KEY is alphanumeric
            for (int i = 0; i < key_length; i++)
            {
                if (isalpha(KEY[i]))
                {
                    for (int j = i + 1; j < key_length; j++)
                    {
                        if (KEY[i] == KEY[j])
                        {
                            return 1;
                        }
                    }
                }
                else
                {
                    printf("The KEY can only contain alphabetical characters.\n");
                    return 1;
                }
            }
        }
        else
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }

        // Get plaintext
        string plain_text = get_string("plaintext: ");
        printf("ciphertext: ");

        // Encipher text
        for (int i = 0; i < strlen(plain_text); i++)
        {
            if (isalpha(plain_text[i]))
            {
                int index = alphabet_indices(plain_text[i]);

                if (isupper(plain_text[i]))
                {
                    printf("%c", toupper(KEY[index]));
                }
                
                if (islower(plain_text[i]))
                {
                    printf("%c", tolower(KEY[index]));
                }

            }
            else
            {
                // Add non-alphanumeric chars to encipher text
                printf("%c", plain_text[i]);
            }
        }
        
        printf("\n");

    }
    else
    {
        printf("Please provide a KEY.\n");
        return 1;
    }
}