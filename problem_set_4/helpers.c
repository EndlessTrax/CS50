#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    int h = height;
    int w = width;

    for (int i = 0; i < h; i++) // Loop through the rows of image
    {
        for (int j = 0; j < w; j++) // Loop through columns within the rows
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            int avg = round((r + g + b) * 0.33333333); // Get the average RGB number

            // set rgb values to the average
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Algo to use
    // sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    // sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    // sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue

    int h = height;
    int w = width;

    for (int i = 0; i < h; i++) // Loop through rows of image
    {
        for (int j = 0; j < w; j++) // Loop through the columns within the row
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Use the algo above to calc new values
            int sepiaRed = round(.393 * r + .769 * g + .189 * b);
            int sepiaGreen = round(.349 * r + .686 * g + .168 * b);
            int sepiaBlue = round(.272 * r + .534 * g + .131 * b);

            // If the sepia value is above 255, max it out at 255.
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Assign new values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    int h = height;

    for (int i = 0; i < h; i++)
    {
        int w = width;

        int hw = round(w / 2); // Find the middle of the image

        for (int j = 0; j < hw; j++)
        {
            // Get values from the left side of the image
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Swap Red value from left and right sides
            image[i][j].rgbtRed = image[i][w - j - 1].rgbtRed;
            image[i][w - j - 1].rgbtRed = r;

            // Swap Green value from left and right sides
            image[i][j].rgbtGreen = image[i][w - j - 1].rgbtGreen;
            image[i][w - j - 1].rgbtGreen = g;

            // Swap Blue value from left and right sides
            image[i][j].rgbtBlue = image[i][w - j - 1].rgbtBlue;
            image[i][w - j - 1].rgbtBlue = b;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    int h = height;
    int w = width;

    // Make a copy of the image to change.
    // This ensures that the original pixel values are used as blurred pixels will change the original values as the program loops.
    // This enusres the orignal pixel values are always available.
    RGBTRIPLE image_copy[height][width];

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    // Take a pixel, and check the average RGB values of the each surrounding pixel.
    // Then apply the average values of surrounding pixels to the current pixel.
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            float r = 0;
            float g = 0;
            float b = 0;
            int c = 0;

            for (int a = -1; a < 2; a++)
            {
                for (int s = -1; s < 2; s++)
                {
                    int x = i + a;
                    int y = j + s;

                    // Check if surrounding pixels are present, incase the pixel is on the edge of the img
                    if (x < 0 || y < 0 || x == h || y == w)
                    {
                        continue;
                    }

                    r += image[x][y].rgbtRed;
                    g += image[x][y].rgbtGreen;
                    b += image[x][y].rgbtBlue;
                    c++;
                }
            }

            float ravg = round(r / c);
            float gavg = round(g / c);
            float bavg = round(b / c);

            image_copy[i][j].rgbtRed = ravg;
            image_copy[i][j].rgbtGreen = gavg;
            image_copy[i][j].rgbtBlue = bavg;

        }
    }

    // Copy the new values from copy to image
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            image[i][j] = image_copy[i][j];
        }
    }
}
