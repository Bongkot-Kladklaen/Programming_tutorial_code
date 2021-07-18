namespace ArrayQueueTest
{
    public class ArrayQueue
    {
        protected object[] data;
        protected int end, start;
        public ArrayQueue(int capacity){
            data = new object[capacity + 1];
            end = start = 0;
        }
        public bool isEmpty(){
            return end == start;
        }
        public void enqueue(object ob){
            int n = (end + 1) % data.Length;
            if (n != start) 
                data[end=n]=ob;
        }
        public object dequeue(){
            if(isEmpty()){
                return null;
            }
            start = (start + 1) % data.Length;
            object ob = data[start];
            data[start] = null;
            return ob;
        }
    }
}