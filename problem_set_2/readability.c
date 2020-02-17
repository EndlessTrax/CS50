// Problem set instructions: https://cs50.harvard.edu/x/2020/psets/2/readability/

#import <stdio.h>
#import <cs50.h>
#import <string.h>
#import <math.h>


int count_letters(string str)
{
    int letter_count = 0;

    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] != ' ')
        {
            letter_count++;
        }
    }

    return letter_count - 1;
}


int count_sentences(string str)
{
    int sentence_count = 0;

    for (int i = 0; i < strlen(str); i++)
    {
        if (str[i] == '.' || str[i] == '?' || str[i] == '!')
        {
            sentence_count++;
        }
    }

    return sentence_count;
}


int main(void)
{
    // Take input
    string input = get_string("Text: ");

    // Count the length of the string (words)
    int string_length = strlen(input);

    // Calc word count
    int word_count = 1;
    for (int i = 0; i < string_length; i++)
    {
        if (input[i] == ' ')
        {
            word_count++;
        }
    }

    // Count sentences and letters
    float L = count_letters(input);
    float S = count_sentences(input);

    // Find the index value
    float index = (0.0588 * (100.0 * L / word_count) - 0.296 * (100.0 * S / word_count)) - 15.8;

    // Round the index to get grade level and print to stdout.
    int grade_level = floor(index);

    if (grade_level < 1)
    {
        printf("Before Grade 1\n");

    }
    else if (grade_level >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_level);
    }
}