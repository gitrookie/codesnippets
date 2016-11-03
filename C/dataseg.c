/* Copyright 2015 */
#include <stdio.h>

int w;             /* in bss segment */
static int c;      /* in bss segment */
static int z = 97;  /* scope within this compilation unit */
int a = 21;  /* scope beyond this compilation unit */
extern int b;  /* scope beyond this compilation unit */
int func() {
  static int x = 1;  /* Static local variable x: Scope is only inside func */
  static int q;
  int y;             /* Extent or lifetime of the x is whole program */
  y = x + 1;

  return q;
}

/* Declaring Structure */
typedef struct st {
  int x;
  char z;
} st;

/* Function Pointers */
int (*fp)(int x);


/* Function Definition */
int square_num(int x) {
  return x * x;
}

int main() {
  // printf("Value is %d", func());
  printf("Value in func %c\n", z);
  /* Structure Initilization */
  st new_struct = {.x = 20, .z = 'a'};
  printf("Struct Value is: %d\n", new_struct.x);

  /* Structure to Pointer */
  st *pstruct = &(st) {  /* Initilization */
    .x = 34,
    .z = 'k'
  };
  printf("Pointer to Structure %c\n", pstruct->z);

  /* Assigning to structure using pointers */
  pstruct->x = 100;
  printf("After assignment the value is %d\n", pstruct->x);

  /* Function Pointers */
  fp = square_num;
  printf("Square of number is %d\n", (*fp)(6));
  printf("Square of number is %d\n", fp(5));

  return 0;
}
