import sys 

def solve():
    try :
        line = sys.stdin.readline()
        if not line :
            return 
        n = int(line.strip())
    except ValueError :
        return  

    file_count = 0
    folder_count = 0
    
    for i in range(n) :
        path = sys.stdin.readline()
        if not path :
            continue
        path = path.strip()
        if "." in path :
            file_count += 1
        else :
            folder_count += 1
    print(f"{file_count} {folder_count}")

if __name__ == "__main__":
    solve()
    
