from .config import Config

__all__ = ['Config']

## 当其他模块使用from myapp import *进行导入时，
# 依据__all__的设置，只有Config类会被导入，
# 像config.py文件里的其他内容（比如函数、变量）不会被导入。
# 简化使用方式，有了这样的设置，其他模块在使用Config类时，可以采用更简洁的写法