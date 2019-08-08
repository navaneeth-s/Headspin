#include<stdio.h>
int main()
{
	int integers[101]={0},n,v,i;
	int 
numbers[100]={30,31,32,33,34,35,36,37,1,2,3,4,5,6,7,38,39,40,41,42,43,44,45,46,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,47,48,49,50,62,63,64,65,66,67,68,69,70,90,51,52,53,54,55,56,57,58,59,60,61,91,92,93,94,95,96,97,98,99,100,71,72,73,74,75,84,85,86,87,88,89,76,77,78,79,80,81,82,83};
// numbers[] is the array containing 100 numbers from 1 to 100, you can replace the array or any of the number to find the missing number in between 1 to 100.
	for(i=0;i<=sizeof(numbers)/sizeof(int);i++)
	{
		if(numbers[i]<=100)
			integers[numbers[i]]=1;
	}
	for(i=1;i<=100;i++)
	{
		if(integers[i]==0)
			printf("Missing number is %d \n",i);
	}
	
}
