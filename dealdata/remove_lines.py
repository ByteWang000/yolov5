import os

# 不提示输出为空
def remove_lines_with_class(input_folder, output_folder, class_id):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, 'r') as f:
                lines = f.readlines()

            # 过滤掉开头为指定类别的行
            lines = [line for line in lines if line.split(' ')[0] != str(class_id)]

            with open(output_path, 'w') as f:
                f.writelines(lines)

            print(f"Processed: {input_path} -> {output_path}")


# 这是为了移除YOLO标记数据中某一个类别的标签所使用的函数
# 提示空内容
def remove_lines_with_class2(input_folder, output_folder, class_id):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, 'r') as f:
                lines = f.readlines()

            # 过滤掉开头为指定类别的行
            lines = [line for line in lines if line.split(' ')[0] != str(class_id)]

            if len(lines) == 0:
                print(f"Warning: {input_path} has been emptied after removing class {class_id}.")

            with open(output_path, 'w') as f:
                f.writelines(lines)

            print(f"Processed: {input_path} -> {output_path}")


# 设置输入文件夹和输出文件夹路径
input_folder = 'E:\yolo\dealdata\label2'
output_folder = 'E:\yolo\dealdata\label3'

# 设置要删除的类别ID
class_id_to_remove = 3

# 执行函数
remove_lines_with_class2(input_folder, output_folder, class_id_to_remove)
