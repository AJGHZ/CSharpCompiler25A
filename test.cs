using System;

class test
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
        suma(5, 6);
        result(suma);

        if (true)
        {
            Console.WriteLine("This is true");
        }
        else
        {
            Console.WriteLine("This is false");
        }

        while (true)
        {
            Console.WriteLine("This is a while loop");
            break; // Prevent infinite loop for demonstration purposes
        }

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("This is a for loop: " + i);
        }

        foreach (var item in new[] { 1, 2, 3 })
        {
            Console.WriteLine("This is a foreach loop: " + item);
        }

        switch (5)
        {
            case 1:
                Console.WriteLine("Case 1");
                break;
            case 2:
                Console.WriteLine("Case 2");
                break;
            default:
                Console.WriteLine("Default case");
                break;
        }

        do
        {
            Console.WriteLine("This is a do-while loop");
        } while (false); // Prevent infinite loop for demonstration purposes
    }
}