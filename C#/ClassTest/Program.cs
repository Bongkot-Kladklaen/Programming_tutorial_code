using System;

namespace ClassTest
{
    class Program
    {
        static void Main(string[] args)
        {
            MyDatabase mdb = new MyDatabase();
            mdb.ShowCustomer();

            MyDatabase mdb2 = new MyDatabase(101,"Bongkot","555 55Rd.");
            mdb2.ShowCustomer();
        }
    }
}
