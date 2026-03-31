def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []

    for i in range(size):
        
        left = "-".join(alpha[size-1:i:-1])
        
       
        right = "-".join(alpha[i:size])
        
       
        row = left + "-" + right if left else right
        
       
        lines.append(row.center(4*size - 3, "-"))

    
    full_pattern = lines[::-1][:-1] + lines
    print("\n".join(full_pattern))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)