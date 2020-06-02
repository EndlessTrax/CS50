#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"


#define ALPHABET_SIZE (27)
int dictionarysize = 0;

typedef struct trienode
{
    struct trienode *children[ALPHABET_SIZE];
    bool isEnd;
}
trienode;

trienode *makenode(void); // Prototype
void freeup(trienode *ptree);
trienode *root;

// Returns true if the word is in dictionary
bool check(const char *checkword)
{
    trienode *cursor;
    int len, index;

    cursor = root;
    len = strlen(checkword);
    for (int level = 0; level < len; level++)
    {

        index = (int) tolower(checkword[level]) - 'a';
        if (index < 0)
        {
            index = ALPHABET_SIZE - 1;
        }
        if (!cursor->children[index])
        {
            return false;
        }
        cursor = cursor->children[index];
    }
    if (!cursor)
    {
        return false;
    }
    else
    {
        return cursor->isEnd;
    }
}


// Loads dictionary into memory. Return true if successful
bool load(const char *dictionary)
{
    FILE *pdictionary;
    char newword[LENGTH + 1];
    trienode *newnode, *cursor;

    dictionarysize = 0;

    root = makenode();

    pdictionary = fopen(dictionary, "r");
    if (pdictionary == NULL)
    {
        return false;
    }

    while (fscanf(pdictionary, "%s", newword) != EOF)
    {
        cursor = root;
        int len = strlen(newword);
        for (int level = 0; level < len; level++)
        {
            int index = (int) newword[level] - 'a';
            if (index < 0)
            {
                index = ALPHABET_SIZE - 1;
            }
            if (!cursor->children[index])
            {
                cursor->children[index] = makenode();
                if (!cursor->children[index])
                {
                    return false; // malloc failed
                }
            }
            cursor = cursor->children[index];
        }
        // Final node is the end of word
        cursor->isEnd = true;
        dictionarysize++;
    }
    printf("   *** loaded %i words\n", dictionarysize);
    fclose(pdictionary);
    return true;
}

trienode *makenode(void)
{
    trienode *newnode;

    newnode = (trienode *) malloc(sizeof(trienode));
    if (newnode)
    {
        newnode->isEnd = false;
        for (int i = 0; i < ALPHABET_SIZE; i++)
        {
            newnode->children[i] = NULL;
        }
    }
    return newnode;
}


// Returns number of words in dictionary if loaded
unsigned int size(void)
{
    return dictionarysize;
}

// Unloads dictionary from memory
bool unload(void)
{
    freeup(root);
    return true;
}

// Recursive called by unload
void freeup(trienode *ptree)
{
    if (!ptree)
    {
        return;
    }
    for (int index = 0; index < ALPHABET_SIZE; index++)
    {
        if (ptree->children[index])
        {
            freeup(ptree->children[index]);
        }
    }
    free(ptree);
    return;
}