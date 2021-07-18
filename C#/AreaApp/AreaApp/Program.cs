using System;

namespace AreaApp
{
    class Program
    {
        static void Main(string[] args)
        {
            double w, h;
            Console.Write("width: ");
            w = Convert.ToDouble(Console.ReadLine());
            Console.Write("height: ");
            h = Convert.ToDouble(Console.ReadLine());
            Console.Write("rectangle area = {0}", w * h);
        }
    }
}
