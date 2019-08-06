import string
import os
import random
num =0;
while num < 50:
    root = "D://test1//"
    test = random.sample('zxvbnmasdfghjklqwretyuiop',13)
    s = ''.join(test);
    if not os.path.exists(root):
        os.mkdir(root);
    with open(root + s + '.txt','w') as f:
        f.write(s);
    num+=1;



