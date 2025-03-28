#include <stdio.h>
#include <string.h>

// Function to compute the LPS array for KMP algorithm
void computeLPSArray(char *str, int M, int *lps) {
    int length = 0;
    lps[0] = 0;
    int i = 1;
    
    while (i < M) {
        if (str[i] == str[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// Function to find minimum characters to add at the front
int minCharsToAdd(char *str) {
    int n = strlen(str);
    
    // Create a new string: str + "$" + reverse(str)
    char temp[2 * n + 2];
    strcpy(temp, str);
    strcat(temp, "$");
    
    // Reverse the string and append
    for (int i = 0; i < n; i++) {
        temp[n + 1 + i] = str[n - 1 - i];
    }
    temp[2 * n + 1] = '\0';
    
    // Compute LPS array for the concatenated string
    int lps[2 * n + 1];
    computeLPSArray(temp, 2 * n + 1, lps);
    
    // Minimum characters to add at front = length of original string - LPS last value
    return n - lps[2 * n];
}

// Driver code
int main() {
    char str[] = "AACECAAAA";
    printf("Minimum characters to add: %d\n", minCharsToAdd(str));
    return 0;
}

