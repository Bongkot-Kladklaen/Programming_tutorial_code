using System;
using System.Linq;
namespace tutorial
{
    class Program
    {
        static void Main(string[] args)
        {
            // TestSelectManyLinq();
            // TestWhereLinq();
            // TestAny();
            // TestGroupJoin();
            // TestExcept();
            // TestZip();
            TestAggregate();
        }
        public static void TestSelectManyLinq(){
            var customers = new[]{
                new Customer{
                    Invoices = new[]{
                        new Invoice {Id=1},
                        new Invoice {Id=2},
                    }
                },
                new Customer{
                    Invoices = new[]{
                        new Invoice {Id=3},
                        new Invoice {Id=4},
                    }
                },
                new Customer{
                    Invoices = new[]{
                        new Invoice {Id=5},
                        new Invoice {Id=6},
                    }
                }
            };

            var allInvoicesFromAllCustomers = customers.SelectMany(c => c.Invoices);
            Console.WriteLine(
                string.Join(",", allInvoicesFromAllCustomers.Select(i => i.Id).ToArray())
            );

        }
        public static void TestWhereLinq(){
            var personnames = new[]{
                "Foo","Bar","Fizz","Buzz"
            };

            var nameStartingWithF = personnames.Where(p => p.StartsWith("F"));
            Console.WriteLine(string.Join(",", nameStartingWithF));
        }
        public static void TestAny(){
            int[] number = {1,2,3,4,5};
            Console.WriteLine(number.Any());
            Console.WriteLine(number.Any(i => i == 1));
        }
        public static void TestGroupJoin(){
            var deverlopers = new[]{
                new Developer{
                    Id=1,
                    Name="Foobuzz"
                },
                new Developer{
                    Id=2,
                    Name="Barfizz"
                }
            };

            var projects = new[]{
                new Project {
                    DeveloperId = 1,
                    Name = "Hello World 3D"
                },
                new Project {
                    DeveloperId = 1,
                    Name = "Super Fizzbuzz Maker"
                },
                new Project {
                    DeveloperId = 2,
                    Name = "Citizen Kane - The action game"
                },
                new Project {
                    DeveloperId = 2,
                    Name = "Pro Pong 2016"
                }
            };

            var grouped = deverlopers.GroupJoin(
                inner: projects,
                outerKeySelector: dev => dev.Id,
                innerKeySelector: proj => proj.DeveloperId,
                resultSelector:(dev,proj) => new{
                    DeverloperName = dev.Name,
                    ProjectName = proj.Select(p => p.Name).ToArray()
                }
            );

            foreach (var item in grouped)
            {
                Console.WriteLine("{0}'s projects: {1}", item.DeverloperName, string.Join(", ", item.ProjectName));
            }

        }

        public static void TestExcept(){
            var numbers = new[]{1,2,3,4,5,6,7,8,9,10};
            var evenNumbersBetweenSixAndFourteen = new[]{6,8,10,12};

            var result = numbers.Except(evenNumbersBetweenSixAndFourteen);
            Console.WriteLine(string.Join(",",result));
        }
        public static void TestZip(){
            var tens = new[]{10,20,30,40,50};
            var units = new[]{1,2,3,4,5};
            var sums = tens.Zip(units, (first, second) => first+second);
            Console.WriteLine(string.Join(",", sums));
        }
        public static void TestAggregate(){
            var elements = new[] {1,2,3,4,5};
            var commaSeparatedElements = elements.Aggregate(seed: "",func:(aggregate, element) => $"{aggregate}{element},");
            Console.WriteLine(commaSeparatedElements);
        }
    }

}
