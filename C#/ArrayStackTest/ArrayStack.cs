using System;
namespace ArrayStackTest
{
    public class ArrayStack
    {
        protected object[] data;
        protected int pointer;
        public ArrayStack(int cpacity){
            data = new object[cpacity];
            pointer = 0;
        }
        public bool isEmpty(){
            return pointer == 0;
        }
        public void push(object ob){
            if (pointer < data.Length)
            {
                data[pointer++] = ob;
            }
        }
        public object pop(){
            if(isEmpty())
                return null;
            object ob = data[--pointer];
            data[pointer] = null;
            return ob;
        }
    }
}