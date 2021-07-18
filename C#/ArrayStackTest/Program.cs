using System;

namespace ArrayStackTest
{
    class Program
    {
        static void Main(string[] args)
        {
            // ArrayStackTest();
            int Number;
            Console.Write("Enter Decimal: ");
            Number = int.Parse(Console.ReadLine());
            DecToBin objDecToBin = new DecToBin(Number);
            objDecToBin.ConvertDecToBin();

        }
        static void ArrayStackTest(){
            ArrayStack stack = new ArrayStack(10);
            for (int i = 0; i < 10; i++)
            {
                string objToPush = "obj" + i;
                Console.WriteLine("pushing: {0}",objToPush);
                stack.push(objToPush);
            }

            Console.WriteLine("-----------------");
            while (!stack.isEmpty())
            {
                string objPoped = (string)stack.pop();
                Console.WriteLine("poping: {0}",objPoped);
            }
        }
    }
}
