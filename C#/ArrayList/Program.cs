using System;

namespace ArrayList
{
    class Program
    {
        static void Main(string[] args)
        {
            int size;
            string data;
            Console.Write("Enter size ArrayList : ");
            size = int.Parse(Console.ReadLine());
            ArrayList arrList = new ArrayList(size);
            while (!arrList.isFull())
            {
                Console.Write("Enter data to list : ");
                data = Console.ReadLine();
                arrList.insert(data);
                Console.WriteLine("Insert {0}",data);
            }

            Console.WriteLine("Remove array list");
            Console.WriteLine("Last Data {0}",arrList.peek(2));



        }
    }
}
