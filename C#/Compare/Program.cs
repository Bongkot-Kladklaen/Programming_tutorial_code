using System;

namespace Compare
{
    class Program
    {
        static void Main(string[] args)
        {
            CompareNumber();
        }

        static void CompareNumber(){
            int num1,num2;
            Console.WriteLine("Enter number1: ");
            num1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter number2: ");
            num2 = int.Parse(Console.ReadLine());

            if (num1 > num2)
            {
                Console.WriteLine("Number1 is more than number2");
            }else{
                Console.WriteLine("Number1 is lass than number2");
            }
            
        }
    }
}
