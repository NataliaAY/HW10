'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
'''
import pandas as pd
whoAmI
0	human
1	robot
2	robot
3	robot
4	robot
one_hot_data = pd.DataFrame({'robot': [1 if i == 'robot' else 0 for i in lst],
                             'human': [1 if j == 'human' else 0 for j in lst]})
one_hot_data
robot	human
0	0	1
1	1	0
2	1	0
3	1	0
4	1	0
5	0	1
6	0	1
7	0	1
8	1	0
9	0	1
10	0	1
11	1	0
12	0	1
13	0	1
14	0	1
15	0	1
16	1	0
17	1	0
18	1	0
19	1	0
pd.get_dummies(data['whoAmI'])
human	robot
0	1	0
1	0	1
2	0	1
3	0	1
4	0	1
5	1	0
6	1	0
7	1	0
8	0	1
9	1	0
10	1	0
11	0	1
12	1	0
13	1	0
14	1	0
15	1	0
16	0	1
17	0	1
18	0	1
19	0	1
