using System;

namespace ArrayQueueTest
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayQueue queue = new ArrayQueue(10);
            for (int i = 0; i < 10; i++)
            {
                string objQueue = "obj" + i;
                Console.WriteLine("enqueue: {0}",objQueue);
                queue.enqueue(objQueue);
            }
            Console.WriteLine("---------------");
            while (!queue.isEmpty())
            {
                string objFromQueue = (string)queue.dequeue();
                Console.WriteLine("dequeue: {0}",objFromQueue);
            }
        }
    }
}
