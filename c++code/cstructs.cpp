// #include <stdio.h>

struct Bad
{
    int i1;
    bool b1;
    int i2;
    bool b2;
    int i3;
    bool b3;
    bool b4;
    bool b5;
    bool b6;
    bool b7;
    int i4;
};

struct Better
{
    int i1;
    int i2;
    int i3;
    int i4;
    bool b1;
    bool b2;
    bool b3;
    bool b4;
    bool b5;
    bool b6;
    bool b7;
};

struct Good
{
    int i1;
    int i2;
    int i3;
    int i4;
    
    union
    {
        struct
        {
            bool b1 : 1;
            bool b2 : 1;
            bool b3 : 1;
            bool b4 : 1;
            bool b5 : 1;
            bool b6 : 1;
            bool b7 : 1;
        };
      
        unsigned char flags;
    };
};

int main( int, char** )
{
  //  printf( "%d %d %d\r\n", sizeof( Bad ), sizeof( Better ), sizeof( Good ));
  return sizeof(Good);
}

