#include<stdio.h>
#include<stdlib.h>

//define the node structure
typedef struct node{
    int data;
    struct node* link;
}*NODE;

NODE create_node(int data)
{
    NODE temp=(NODE)malloc(sizeof(struct node));
    if(temp !=NULL)
    {
        temp->data=data;
        temp->link=NULL;
    }
    else
    printf("\n\t Unable to create a Node" );
    return temp;
}

void Display(NODE Head)
{
    if(Head==NULL)
    printf("Empty List");
    else{
        printf("\n HEAD->");
        for(NODE temp=Head;temp !=NULL;temp=temp->link)
        printf("%d->",temp->data);
    printf("NULL \n");
    }
}

NODE ins_front(NODE Head,int data)
{
    NODE new_node=create_node(data);
    if(new_node !=NULL)
    {
        new_node->link=Head;
        Head=new_node;
    }
    return new_node;
}

NODE ins_last(NODE Head,int data)
{
    NODE temp,new_node=create_node(data);
    if(new_node !=NULL)
    {
        if(Head==NULL)
      return new_node;
      for(temp=Head;temp->link !=NULL;temp=temp->link);
      temp->link=new_node;
    }
    return Head;
}

NODE Delete_Last(NODE Head)
    {
        if (Head == NULL){
            printf("\n\t\t Empty list");
        return NULL;
        }
         if (Head->link == NULL){
            printf("\n\t Deleted Node %d.Head->data");
            free(Head);
            return NULL;
}
NODE curr = Head;
while (curr->link->link !=NULL)
     curr = curr->link;
    printf("\n\t Deleted Node %d",curr->link->data);
free(curr->link);
curr->link=NULL;
return Head;
}
     NODE insert_position(NODE Head,int data,int pos)
    {
        NODE curr=Head,new_node;
        int i;
        
        new_node = create_node(data);
        if(new_node==NULL)
        return Head;

        if (pos==0 || Head==NULL)
        {
         new_node->link=Head;
        return new_node;
        }
        for(i=0; i<pos-1 && curr !=NULL;i++){
        curr=curr->link;
        }
        
      
        if(curr == NULL)
        {
            printf("out of range.Not inserted");
            free(new_node);
            return Head;
        }
         new_node->link = curr->link;
         curr->link = new_node;

         return Head;
    }

    int main()
    {
        NODE Head=create_node(10);
        Display(Head);

        Head=ins_front(Head,20);
        Display(Head);

        Head=ins_last(Head,50);
        Display(Head);

        Head=Delete_Last(Head);
        Display(Head);

        Head=insert_position(Head,60,2);
        Display(Head);
        
        return 0;

    }