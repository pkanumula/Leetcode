int chalkReplacer(int* chalk, int chalkSize, int k) {
    // Calculate the total chalk needed in one complete round
    long long totalChalk = 0;
    for (int i = 0; i < chalkSize; i++) {
        totalChalk += chalk[i];
    }
    
    // Reduce k by the total chalk needed for complete rounds
    k = k % totalChalk;
    
    // Find the student who needs to replace the chalk
    for (int i = 0; i < chalkSize; i++) {
        if (k < chalk[i]) {
            return i;
        }
        k -= chalk[i];
    }
    
    return -1; // This line is never reached
}
