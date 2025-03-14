// C program for counting minimum character to be
// added at front to make string palindrome
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Function to check if the substring s[i...j] is a palindrome
bool isPalindrome(char s[], int i, int j) {
    while (i < j) {
        
        // If characters at the ends are not the same, it's not a palindrome
        if (s[i] != s[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int minChar(char s[]) {
    int cnt = 0;
    int i = strlen(s) - 1;
    
    // Iterate from the end of the string, checking for the 
    // longest palindrome starting from the beginning
    while (i >= 0 && !isPalindrome(s, 0, i)) {
        
        i--;
        cnt++;
    }
    
    return cnt;
}

int main() {
    char s[] = "AACECAAAA";    
    printf("%d", minChar(s));
    return 0;
}

