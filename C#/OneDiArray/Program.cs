using System;

namespace OneDiArray
{
    class Program
    {
        static void Main(string[] args)
        {
            float[] floatArr = new float[] {11,12,13,14,15};
            Console.WriteLine("Use for");
            for (int i = 0; i < floatArr.Length; i++)
            {
                Console.WriteLine(floatArr[i]);
            }
            Console.WriteLine("Use foreach");
            foreach (float i in floatArr)
            {
                Console.WriteLine(i);
            }
        }
    }
}
