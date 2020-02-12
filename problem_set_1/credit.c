// This is the answer file to the `credit` portion of the problem set: https://cs50.harvard.edu/x/2020/psets/1/
// Sample CC numbers -- https://developer.paypal.com/docs/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_sum(long card_num)
{
    int count = 0;
    int odd_total = 0;
    int even_total = 0;

    while (card_num > 0) // do till num greater than 0
    {
        int digit = card_num % 10; // split last digit from number
        card_num = card_num / 10; // divide num by 10. num /= 10 also a valid one

        count++;

        if (count % 2 == 0)
        {
            int num = digit * 2;

            if (num > 9)
            {
                int d2 = num % 10;
                num = 1 + d2; // 1 added as the first digit will always be 1 after % 10 on num.
            }
            even_total += num;
        }
        else
        {
            odd_total += digit;
        }
    }
    return odd_total + even_total;
}

int main(void)
{
    long credit_card = get_long("Credit card number: ");

    if (check_sum(credit_card) % 10 == 0)
    {
        char buf[1024];
        memset(buf, '\0', sizeof(buf));
        sprintf(buf, "%ld", credit_card);

        int card_length = strlen(buf);
        int first = (buf[0] - '0');
        int second = (buf[1] - '0');

        if (card_length == 13)
        {
            printf("VISA\n");
        }
        else if (card_length == 15)
        {
            if (first == 3 && second == 4)
            {
                printf("AMEX\n");
            }
            else if (first == 3 && second == 7)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (card_length == 16)
        {
            if (first == 4)
            {
                printf("VISA\n");
            }
            else if (first == 5 && second < 6)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
