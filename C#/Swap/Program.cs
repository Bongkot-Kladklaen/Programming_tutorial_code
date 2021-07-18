using System;

namespace Swap
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1 = 100;
            int num2 = 200;
            Console.WriteLine("Before");
            Console.WriteLine("Number 1: {0}, Number 2: {1}",num1,num2);
            Swap<int>(ref num1,ref num2);
            Console.WriteLine("Number 1: {0}, Number 2: {1}",num1,num2);
        }

        static void Swap<T>(ref T num1, ref T num2){
            T temp;
            temp = num1;
            num1 = num2;
            num2 = temp; 
        }

    }
}
