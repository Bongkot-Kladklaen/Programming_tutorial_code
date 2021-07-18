using System;
namespace ArrayList
{
    public class ArrayList
    {
        protected object[] data;
        protected int start, end, theSize;
        public ArrayList(int capacity){
            data = new object[capacity];
            start = end = theSize = 0;
        }
        public bool isEmpty(){
            return theSize == 0;
        }
        public bool isFull(){
            return theSize >= data.Length;
        }
        public int size(){
            return theSize;
        }
        public void insert(object o){
            if(theSize < data.Length){
                data[start = (start + 1) % data.Length] = o;
                theSize++;
            }
        }
        public void insertEnd(object o){
            if(theSize < data.Length){
                data[end] = 0;
                end = (end+data.Length -1 ) % data.Length;
                theSize++;
            }
        }
        public object remove(){
            if(isEmpty()){
                return null;
            }
            theSize--;
            object o = data[start];
            data[start] = null;
            start=(start+data.Length-1)%data.Length;
            return o;
        }
        public object removeEnd(){
            if(isEmpty()){
                return null;
            }
            theSize--;
            end=(end+1)%data.Length;
            object o = data[end];
            data[end] = null;
            return o;
        }
        public object peek(int offset){
            if (offset >= theSize)
            {
                return null;
            }
            return data[(end + offset + 1) % data.Length];
        }

    }
}