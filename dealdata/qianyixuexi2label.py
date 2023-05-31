import os

'''
更换yolo标签值
例如：标签2改为标签1
'''
def replace_class_in_labels(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            with open(input_path, 'r') as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                elements = line.strip().split()
                if len(elements) > 0:
                    class_id = int(elements[0])
                    if class_id == 2:
                        elements[0] = '1'
                    elif class_id == 3:
                        elements[0] = '2'
                    # elif class_id == 2:
                    #     elements[0] = '8'
                    # elif class_id == 3:
                    #     elements[0] = '9'
                new_line = ' '.join(elements) + '\n'
                new_lines.append(new_line)

            with open(output_path, 'w') as f:
                f.writelines(new_lines)


# 使用示例
input_folder = 'C:/Users/ByteWang/Desktop/123/labelswithout_p/'  # 输入文件夹路径
output_folder = 'C:/Users/ByteWang/Desktop/123/labelswithout_pnew/'  # 输出文件夹路径
replace_class_in_labels(input_folder, output_folder)
