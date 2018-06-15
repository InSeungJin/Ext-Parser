import struct
import math
import os
from time import sleep
#start tools logo

def ToolMain():
    os.system('cls')
    ToolMain="""

     _____             ______      _   
    |  __ \ /\        |  ____|    | |  
    | |__) /  \ ______| |__  __  _| |_ 
    |  ___/ /\ \______|  __| \ \/ / __|
    | |  / ____ \     | |____ >  <| |_ 
    |_| /_/    \_\    |______/_/\_\\__|
            Parse&Analysis-Ext       
    """
    print(ToolMain)
    sleep(2.5)
    os.system('cls')

ToolMain()

#start of source
n = 0
Period = "."
NSF_lis = []
NSF_dic = {}
dirlist = os.listdir('.')
for i in dirlist:
    if Period in i:
        File = i.split('.')
        Extension = File[1]
        if Extension == 'dd': #you can select other Extension
            n +=1
            #NSF is Number of Select(extension) File
            NSF_lis.append(i)
            
n = 0
for i in NSF_lis:
    n += 1      
    NSF_dic[n] = i
    print("{0}. {1}".format(n, NSF_dic[n])) #print list of your selected Extension file

try:
    Option = input("Select File Number : ") #Option is option what you input
    Option = int(round(float(Option)))
except:
    os.system('cls')
    print("You need to select by number")
else:
    if Option <= n and Option > 0:
        os.system('cls')
        print("you select {}".format(NSF_dic[Option])) #When you select right option, NPF_dic is dic which you select
        sleep(1.5) 
    elif type(Option) != int or float:
        os.system('cls')
    else:
        os.system('cls')
        print("Out of range")

 #up is for option list, down is for ext analysis

f = open(NSF_dic[Option], "rb") 
f.seek(1024) #pass "Group 0 padding" sector
superblock = f.read(1024)
print('\n')

block_size = struct.unpack_from("<I", superblock, 0x18)[0]
#print("Block size = {} bytes\n".format(pow(2,block_size+10))) # +10 is for print in byte

inode_size = struct.unpack_from("<I", superblock, 0x58)[0]
#print("Inode size = {} bytes\n".format(inode_size))

f.seek(1024+136) #For Last mounted path 
LM_path_b = f.read(64) #LM = Last mounted, b = byte type
LM_path = LM_path_b.decode('utf-8')
#print("Last Mounted Path = {}\n".format(LM_path))

gdt_size = struct.unpack_from("<H", superblock, 0xFE)[0]
if gdt_size <= 32:
	gdt_size = 32
#print("GDT size = {} bytes\n".format(gdt_size))
block_size = pow(2, block_size+10)

if block_size >= 4096:
        f.seek(block_size)
else:
        f.seek(2048)

gdt = f.read(gdt_size)

block_bitmap = struct.unpack_from("<H", gdt, 0x0)[0]
block_bitmap = block_size * block_bitmap #block size need to multiply
#print("Block Bitmap address = {}".format(block_bitmap))

inode_bitmap = struct.unpack_from("<H", gdt, 0x4)[0]
inode_bitmap = block_size * inode_bitmap #block size need to multiply
#print("Inode Bitmap address = {}".format(inode_bitmap))

inode_table = struct.unpack_from("<H", gdt, 0x8)[0]
inode_table = block_size * inode_table #block size need to multiply
#print("Inode table address = {}".format(inode_table))

root_start = (inode_table+inode_size)
f.seek(root_start)
root = f.read(inode_size)   #update this position

#print every result of ext
result1 = """
Block Size = {0} bytes          Inode Size = {1} bytes         GDT Size = {2} bytes

Last Mounted Path = {3}

Block Bit map address = {4}    Inode Bitmap address = {5}    Inode Table address = {6}
""".format(block_size, inode_size, gdt_size, LM_path, block_bitmap, inode_bitmap, inode_table)

os.system('cls')
print(result1) #Part 1, part 2 is for inode