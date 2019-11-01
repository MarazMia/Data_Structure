#include<bits/stdc++.h>
using namespace std;
int size=100,Queue[100],front=-1,rear=-1,value,sz;
void insert()
{
    if(rear>=size-1)
    {
        cout<<"queue overflow\n";
        return;
    }
    else
    {
        if(front==-1)
            front=0;
        cout<<"enter your value : ";
        cin>>value;
        rear++;
        Queue[rear]=value;
        cout<<"value is been added to the queue\n";
        sz++;
    }
}
void Delete()
{
    if(front<0 || front>rear)
    {
        cout<<"queue underflow\n";
        return;
    }
    else
    {
        cout<<"your deleted value is : "<<Queue[front]<<endl;
        front++;
        sz--;
    }
}
void display()
{
    if(front==-1 || sz==0)
    {
        cout<<"no data to be shown\n";
        return;
    }
    else
    {
        cout<<"current data of the queue are"<<endl;
        for(int i=front; i<=rear; i++)
            cout<<Queue[i]<<" ";
        cout<<"with size of "<<sz;
        cout<<endl;
    }
}
int main()
{
    cout<<"1) for insert\n2) for delete\n3) for display the queue\npress any key to exit\n\n\n";
    char ch;
    cout<<"enter your choice\n";
    while(cin>>ch)
    {
        if(ch=='1')
            insert();
        else if(ch=='2')
            Delete();
        else if(ch=='3')
            display();
        else
            break;
        cout<<"enter your choice\n";
    }
}

