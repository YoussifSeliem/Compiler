int main() {
    // This is a single-line comment
    if (x == 42) {
        /* This is
           a block
           comment */
        for (int i = 0; i < 10; i++) {
            y = y + i;
        }
    } else {
        y = 3.1; // Another comment
    }

    int z;
    while(x>y) {
        y++;
        x--;
    }
    
    if(x==5&&y>z) x=4;
    return 0;
}