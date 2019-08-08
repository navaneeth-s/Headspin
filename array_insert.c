#include<stdio.h>
int main()
{
	int integers[100],n,v,i;
	printf("Enter the position to insert the element:");
	scanf("%d",&n);
	printf("Enter the value to the %d position",n);
	scanf("%d",&v);
	integers[n]=v;
	printf("Position \t Value \n");
	for(i=0;i<100;i++)
	{
		
		printf("%d \t %d \n",i,integers[i]);
	}
}
