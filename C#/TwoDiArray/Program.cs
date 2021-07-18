using System;

namespace TwoDiArray
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            int[,] intArr = new int[,]{
                {10,30,40,20},
                {10,30,40,20},
                {10,30,40,20},
                {10,30,40,20},
                {10,30,40,20}
            };

            Console.WriteLine("Student1 + Student2 + Student3 + Student4 + Student5");
            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    sum += intArr[i,j];
                }
            }
            Console.WriteLine("Total {0}",sum);
        }
    }
}
