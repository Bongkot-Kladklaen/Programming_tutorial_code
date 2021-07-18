using System;

namespace PassByValue
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 1;
            int y = 0;
            Console.WriteLine("This coordinate first point is {0},{1}",x,y);
            AddPoint(x,y);
            Console.WriteLine("After call addpoint method, the point is {0},{1}",x,y);
        }

        static void AddPoint(int x1, int y1){
            Console.WriteLine("Receive point from main method is {0},{1}",x1,y1);
            x1+=10;
            y1+=5;
            Console.WriteLine("Now the ne point is {0},{1} in Addpoint Method",x1,y1);

        }
    }
}
