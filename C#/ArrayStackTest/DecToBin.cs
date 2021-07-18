using System;
namespace ArrayStackTest
{
    public class DecToBin
    {
        static int Decimal;
        static string Bin;
        ArrayStack stack = new ArrayStack(10);
        public DecToBin(int dec){
            Decimal = dec;
        }

        public void ConvertDecToBin(){
            while (Decimal != 0)
            {
                if(Decimal % 2 == 0){
                    stack.push("0");
                }else{
                    stack.push("1");
                }
                Decimal = Decimal/2;
            }

            while (!stack.isEmpty())
            {
                Bin += (string)stack.pop();
            }
            Console.WriteLine("Binary: {0}",Bin);
        }
    }
}