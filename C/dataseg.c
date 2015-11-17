/* Copyright 2015 */
#include <stdio.h>
int w;             /* in bss segment */
static int c;      /* in bss segment */
static int z = 97;  /* scope within this compilation unit */
int a = 21;  /* scope beyond this compilation unit */
extern int b = 20;  /* scope beyond this compilation unit */
int func() {
  static int x = 1;  /* Static local variable x: Scope is only inside func */
  static int q;
  int y;             /* Extent of lifetime of the x is whole program */
  y = x + 1;

  return q;
}

int main() {
  // printf("Value is %d", func());
  printf("Value in func %c", z);

  return 0;
}
