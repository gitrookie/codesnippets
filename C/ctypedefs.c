/* COPYRIGHT 2016 */

#include "helper.h"

typedef int (*fp)(int x);  /* defines a type fp-> int (*)(int) */

int square(int x) {
  return x * x;
}

int cube(int x) {
  return x * x * x;
}

int calroot(int x, fp func) {
  return func(x);
}



int main() {
  extern int x;
  printf("%d", calroot(x, cube));
}
