using System;

namespace PassByOut
{
    class Program
    {
        static void Main(string[] args)
        {
            int radius = 3;
            int height = 10;
            double surfaceCurve;
            double volume;
            Computer(radius,height,out surfaceCurve, out volume);
            Console.WriteLine("Radius and Height of cylinder is {0} and {1} respectively.",radius,height);
            Console.WriteLine("Surface area is {0}",surfaceCurve);
            Console.WriteLine("Volume is {0}",volume);
        }

        static void Computer(int r,int h, out double sC, out double vol){
            sC = 2 * 3.142857 * r * h;
            vol = 3.142857 * r * r * h;
        }
    }
}
