
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
cost_p=6
cost_s=5
cost_c=5

for i in range(0,n):
    count=map(int,raw_input().split())
    
    min_3=min(count)
    group_3 = min_3*((cost_p+cost_s+cost_c)*0.8)
    
    
    
    for i in range(0,len(count)):
        count[i]-=min_3
        
        
    if(max(count)>0):
        if(count[0]==0):
            min_2=min(count[1],count[2])
            group_2=min_2*((cost_s+cost_c)*0.9)
           
        elif count[1]==0:
            min_2=min(count[0],count[2])
            group_2=min_2*((cost_p+cost_c)*0.9)
            
        else:
            min_2=min(count[1],count[0])
            group_2=min_2*((cost_s+cost_p)*0.9)
           
            
        for i in range(0,len(count)):
            count[i]-=min_2
        
        
        if(max(count)>0):
            if(count[0]!=0):
                group_1=count[0]*(cost_p)
                
            elif count[1]!=0:
                group_1=count[1]*(cost_s)
                
            else:
                group_1=count[2]*(cost_c)
               
        else:
            print group_3+group_2
            
        
        print group_3+group_2+group_1
            
        
    else:
        print group_3
