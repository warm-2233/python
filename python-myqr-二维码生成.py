import os

# 第三方模块
from MyQR import myqr

p = os.getcwd()

myqr.run(words="",
        version=20,
        level="H",
        picture=p+"/0.jpg",
        colorized=True,
        save_dir=p)
