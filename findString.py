def count_substring(string, sub_string):
    n=0
    count=0
    while (n+len(sub_string))<=(len(string)+1):
        if string[n:n+len(sub_string)]==sub_string:
            
            count+=1
            
        	
        n+=1
        
            
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
