#include <stdio.h>

void sort(int nums,char array[100][20]);
int count=1;

int main()
{
	int n,m;
	char words[100][20];
	while(1)
	{
		scanf("%d",&n);
		for(m=0;m<n;m++)
			scanf("%s",words[m]);
		sort(n,words);
		count++;
	}
	return 0;
}

void sort(int nums,char array[100][20])
{
	char tmp;
	int u,v,w,t;
	int x,y;
	for(u=0;u<nums;u++)//排序 
	{
		for(v=1;v<nums-u;v++)
		{
			for(w=0;w<20;w++)
			{   //当 array[u][w]和 array[u+v][w]同为大写或同为小写时，执行以下语句 
				if(((array[u][w]>=65&&array[u][w]<=90)&&(array[u+v][w]>=65&&array[u+v][w]<=90))||((array[u][w]>=97&&array[u][w]<=122)&&(array[u+v][w]>=97&&array[u+v][w]<=122)))
				{
					if(array[u][w]<array[u+v][w])
						break;
					else if(array[u][w]==array[u+v][w])
					{	//当array[u][w+1]不是字母，array[u+v][w+1]是字母时，执行以下语句 
						if(array[u][w+1]=='\0'&&array[u+v][w+1]!='\0')
							break;
						//当array[u][w+1]是字母，array[u+v][w+1]不是字母时，执行以下语句 
						else if(array[u][w+1]!='\0'&&array[u+v][w+1]=='\0')
						{
							for(t=w;t<20;t++)
							{
								if(array[u][t]=='\0'&&array[u+v][t]=='\0')
									break;
								tmp=array[u][t];
								array[u][t]=array[u+v][t];
								array[u+v][t]=tmp;
							}
							break;
						}
						continue;
					}
					else if(array[u][w]>array[u+v][w])
					{
						for(t=w;t<20;t++)
						{
							if(array[u][t]=='\0'&&array[u+v][t]=='\0')
								break;
							tmp=array[u][t];
							array[u][t]=array[u+v][t];
							array[u+v][t]=tmp;
						}
						break;
					}
				}//当 array[u][w]为大写，array[u+v][w]为小写时，执行以下语句 
				else if((array[u][w]>=65&&array[u][w]<=90)&&(array[u+v][w]>=97&&array[u+v][w]<=122))
				{
					if((array[u][w]+32)<array[u+v][w])
						break;
					else if((array[u][w]+32)==array[u+v][w])
					{	//当array[u][w+1]不是字母，array[u+v][w+1]是字母时，执行以下语句 
						if(array[u][w+1]=='\0'&&array[u+v][w+1]!='\0')
							break;
						//当array[u][w+1]是字母，array[u+v][w+1]不是字母时，执行以下语句 
						else if(array[u][w+1]!='\0'&&array[u+v][w+1]=='\0')
						{
							for(t=w;t<20;t++)
							{
								if(array[u][t]=='\0'&&array[u+v][t]=='\0')
									break;
								tmp=array[u][t];
								array[u][t]=array[u+v][t];
								array[u+v][t]=tmp;
							}
							break;
						}
						continue;
					}
					else if((array[u][w]+32)>array[u+v][w])
					{
						for(t=w;t<20;t++)
						{
							if(array[u][t]=='\0'&&array[u+v][t]=='\0')
								break;
							tmp=array[u][t];
							array[u][t]=array[u+v][t];
							array[u+v][t]=tmp;
						}
						break;
					}
				}//当 array[u][w]为小写，array[u+v][w]为大写时，执行以下语句 
				else if((array[u][w]>=97&&array[u][w]<=122)&&(array[u+v][w]>=65&&array[u+v][w]<=90))
				{
					if(array[u][w]<(array[u+v][w]+32))
						break;
					else if(array[u][w]==(array[u+v][w]+32))
					{	//当array[u][w+1]不是字母，array[u+v][w+1]是字母时，执行以下语句 
						if(array[u][w+1]=='\0'&&array[u+v][w+1]!='\0')
							break;
						//当array[u][w+1]是字母，array[u+v][w+1]不是字母时，执行以下语句 
						else if(array[u][w+1]!='\0'&&array[u+v][w+1]=='\0')
						{
							for(t=w;t<20;t++)
							{
								if(array[u][t]=='\0'&&array[u+v][t]=='\0')
									break;
								tmp=array[u][t];
								array[u][t]=array[u+v][t];
								array[u+v][t]=tmp;
							}
							break;
						}
						continue;
					}
					else if(array[u][w]>(array[u+v][w]+32))
					{
						for(t=w;t<20;t++)
						{
							if(array[u][t]=='\0'&&array[u+v][t]=='\0')
								break;
							tmp=array[u][t];
							array[u][t]=array[u+v][t];
							array[u+v][t]=tmp;
						}
						break;
					}
				}
			}	
		}
	}
	for(x=0;x<nums;x++)//输出 
	{
		for(y=0;y<20;y++)
		{
			if(array[x][y]<65||array[x][y]>122||(array[x][y]>90&&array[x][y]<97))//我躲不过你，我绕过你不就行了 :) 
				break;
			printf("%c",array[x][y]);
		}
		if(x!=nums-1)
			printf("\n");
	}
	printf("\n");
	if(count%3==0)
		printf("\n这鬼程序写了我一整天!\nIt took me a whole day to write this fucking program!\n");
}

