def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)
b=intToBin32(-1)
print(b)
print(((1 << 32) -1))
print((1 << 32) )
print(bin(((1 << 32) -1)))
print(bin((1 << 32) ))
print(bin(-254))