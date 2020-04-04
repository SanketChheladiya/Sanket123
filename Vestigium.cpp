#include<bits/stdc++.h>
using namespace std;

int main()
{
int y;
cin>>y;
for(int w=0;w<y;w++)
{
int n;
cin>>n;
int a[1000][1000],s=0;

for(int i=1;i<=n;i++)
{
for(int j=1;j<=n;j++)
{
cin>>a[i][j];
if(i==j)
{
s=s+a[i][j];
}
}
}
int r=0,c=0,temp=0;
for(int i=1;i<=n;i++)
{
   for(int j=1;j<n;j++)
   {
       for(int k=j+1;k<=n;k++)
       {
           if(a[i][j]==a[i][k])
           {
               r=r+1;
               temp=1;
               break;
           }
       }
       if(temp==1)
       {
           temp=0;
           break;
       }
   }
}

for(int i=1;i<=n;i++)
{
   for(int j=1;j<n;j++)
   {
       for(int k=j+1;k<=n;k++)
       {
           if(a[j][i]==a[k][i])
           {
               c=c+1;
               temp=1;
               break;
           }
       }
       if(temp==1)
       {
           temp=0;
           break;
       }
   }
}
cout<<"Case "<<"#"<<w+1<<": "<<s<<" "<<r<<" "<<c<<" "<<endl;
}
}
