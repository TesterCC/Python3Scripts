import copy

# 创建一个包含列表的对象
original_list = [1, 2, [3, 4]]

# 浅拷贝对象
shallow_copy = copy.copy(original_list)

# 深拷贝对象
deep_copy = copy.deepcopy(original_list)

# 更改浅拷贝对象中的嵌套列表元素
shallow_copy[2][0] = 5

# 输出原始对象、浅拷贝对象和深拷贝对象
print("Original object:", original_list)
print("Shallow copy object:", shallow_copy)
print("Deep copy object:", deep_copy)

# 深拷贝和浅拷贝的区别: 浅拷贝对象和原始对象中的嵌套列表元素都被更改了，而深拷贝对象则保持不变。