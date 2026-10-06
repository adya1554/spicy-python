# >>> dictt = {
# ...         "name" : {'first':'kee','second':'adya'},
# ...         "ipl" : {'rcb':'virat','mi':'rohit'}}
# >>> 
# >>> dictt
# {'name': {'first': 'kee', 'second': 'adya'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit'}}
# >>> dictt['first']
# Traceback (most recent call last):
#   File "<python-input-3>", line 1, in <module>
#     dictt['first']
#     ~~~~~^^^^^^^^^
# KeyError: 'first'
# >>> dictt['name']
# {'first': 'kee', 'second': 'adya'}
# >>> dictt['name']['first']
# 'kee'
# >>> dictt['name']['third'] = 'kidu'
# >>> dictt['name']['third']
# 'kidu'
# >>> print(dictt)
# {'name': {'first': 'kee', 'second': 'adya', 'third': 'kidu'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit'}}
# >>> dictt['ipl']['rr'] = 'vaibhav s'
# >>> print(dictt)
# {'name': {'first': 'kee', 'second': 'adya', 'third': 'kidu'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit', 'rr': 'vaibhav s'}}
# >>> 
# >>> 
# >>> dictt_copy = dictt.copy()
# >>> print(dict_copy)
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     print(dict_copy)
#           ^^^^^^^^^
# NameError: name 'dict_copy' is not defined. Did you mean: 'dictt_copy'?
# >>> print(dictt_copy)
# {'name': {'first': 'kee', 'second': 'adya', 'third': 'kidu'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit', 'rr': 'vaibhav s'}}
# >>> dictt.pop('rr')
# Traceback (most recent call last):
#   File "<python-input-16>", line 1, in <module>
#     dictt.pop('rr')
#     ~~~~~~~~~^^^^^^
# KeyError: 'rr'
# >>> dictt.popitem()
# ('ipl', {'rcb': 'virat', 'mi': 'rohit', 'rr': 'vaibhav s'})
# >>> dictt['ipl']['rr'] = 'vaibhav s'
# Traceback (most recent call last):
#   File "<python-input-18>", line 1, in <module>
# >>> data = {
# ...     'name': {
# ...         'first': 'kee',
# ...         'second': 'adya',
# ...         'third': 'kidu'
# ...     },
# ...     'ipl': {
# ...         'rcb': 'virat',
# ...         'mi': 'rohit',
# ...         'rr': 'vaibhav s'
# ...     }
# ... }
# ... 
# ... print(data)
# ... 
# {'name': {'first': 'kee', 'second': 'adya', 'third': 'kidu'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit', 'rr': 'vaibhav s'}}
# >>> 
# >>> del data['name']['third]
#   File "<python-input-28>", line 1
#     del data['name']['third]
#                      ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> del data['name']['third']
# >>> data
# {'name': {'first': 'kee', 'second': 'adya'}, 'ipl': {'rcb': 'virat', 'mi': 'rohit', 'rr': 'vaibhav s'}}
# >>> 
#  *  History restored 

# PS D:\spicy-python> PYTHON
# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
# >>> DIC = {x**3 for x in range(10)}
# >>> dic
# Traceback (most recent call last):
#   File "<python-input-1>", line 1, in <module>
#     dic
# NameError: name 'dic' is not defined. Did you mean: 'dir'?
# >>> dic = {x**3 for x in range(10)}
# >>> dic
# {0, 1, 64, 512, 8, 343, 216, 729, 27, 125}
# >>> dic = {x:x**3 for x in range(10)}
# >>> dic
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
# >>> print(dic)
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
# >>> dict.keys()
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     dict.keys()
#     ~~~~~~~~~^^
# TypeError: unbound method dict.keys() needs an argument
# >>> print(dic.keys())
# dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> print(dic.values())
# dict_values([0, 1, 8, 27, 64, 125, 216, 343, 512, 729])
# >>> print(dic.items())
# dict_items([(0, 0), (1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729)])
# >>> print(dic.items(),end="\n")
# dict_items([(0, 0), (1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729)])
# >>> for i,j in dic.items():
# ...     print(f"{i}:{j}")
# ...     
# 0:0
# 1:1
# 2:8
# 3:27
# 4:64
# 5:125
# 6:216
# 7:343
# 8:512
# 9:729
# >>> dic.pop(0)
# 0
# >>> print(dic)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
# >>> dic.popitem()
# (9, 729)
# >>> print(dic)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
# >>> dic[10] = 1000
# >>> print(dic)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 10: 1000}
# >>> dic['aditya'] = 'x'
# >>> print(dic)
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 10: 1000, 'aditya': 'x'}
# >>> dic.popitem()
# ('aditya', 'x')
# >>> dic.popitem()
# (10, 1000)
# >>> dic.popitem()
# (8, 512)
# >>> dic.popitem()
# (7, 343)
# >>> dic.popitem()
# (6, 216)
# >>> dic.popitem()
# (5, 125)
# >>> dic.popitem()
# (4, 64)
# >>> dic.popitem()
# (3, 27)
# >>> dic.popitem()
# (2, 8)
# >>> dic.popitem()
# (1, 1)
# >>> dic.popitem()
# Traceback (most recent call last):
#   File "<python-input-31>", line 1, in <module>
#     dic.popitem()
#     ~~~~~~~~~~~^^
# KeyError: 'popitem(): dictionary is empty'
# >>> dic
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
# >>> //tuple
#   File "<python-input-38>", line 1
#     //tuple
#     ^^
# SyntaxError: invalid syntax
# >>> #tuple  : one row of record 
# >>> #list   : are mutable                    mutable   we can change  manupulatable 
# >>> #tuple cant change                        
# >>> ipl = ('rcb','mi','rr','dd','kxip','csk')
# >>> ipl
# ('rcb', 'mi', 'rr', 'dd', 'kxip', 'csk')
# >>> ipl[0:]
# ('rcb', 'mi', 'rr', 'dd', 'kxip', 'csk')
# >>> ipl[0:3]
# ('rcb', 'mi', 'rr')
# >>> ipl[:3]
# ('rcb', 'mi', 'rr')
# >>> len(ipl)
# 6
# >>> ipl1 =('lsg','kkr','gt','srh')
# >>> total = ipl+ipl1
# >>> total
# ('rcb', 'mi', 'rr', 'dd', 'kxip', 'csk', 'lsg', 'kkr', 'gt', 'srh')
# >>> if 'rcb' in ipl:
# ...     print("rcb won ipl")
# ... 
# rcb won ipl
# >>> if 'rcb' in total:
# ...     print("rcb won ipl")
# ...     
# rcb won ipl
# >>> ipl.count('rcb')
# 1
# >>> type(ipl)
# <class 'tuple'>