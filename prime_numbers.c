#include<stdio.h>
int main()
{
	int s,f,flag,j,i;
	printf("Enter intervals seperated by a space :");
	scanf("%d %d",&s,&f);
	if(s==0)
		s++;
	if(s>f)
	{
		flag=s;
		s=f;
		f=flag;
	}
	for(i=s;i<=f;i++)
	{
		flag=0;
		for(j=2;j<=i/2;j++)
		{
			if(i%j==0)
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			printf("%d\n",i);
	}
}
