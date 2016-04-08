#include <stdio.h>

int main(void) {
  unsigned short a = 0x1234;

  printf("%x, size : %lu\n", a & 0xFF00, sizeof(a));

  return 0;
}
