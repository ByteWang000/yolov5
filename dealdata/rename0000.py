import os
import glob
from PIL import Image

# 该函数可以将文件夹中图像Resize成指定最长边大小图像
# 以指定数字重命名
def resize_and_rename_images():

    input_folder = 'C:/Users/ByteWang/Desktop/FinalResults'  # 输入文件夹路径
    # input_folder = 'E:/yolo负样本'
    output_folder = 'E:/yolo负样本/1'  # 输出文件夹路径
    start_index = 2053  # 设置起始索引值


    # 获取输入文件夹中所有图像文件的路径
    # image_files = glob.glob(os.path.join(input_folder, '*.png'))  # 根据实际图像格式进行修改
    image_files = []
    file_extension = '.png'

    # 递归遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(file_extension):
                image_files.append(os.path.join(root, file))
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历所有图像文件
    for image_file in image_files:
        # 打开图像文件
        with Image.open(image_file) as img:
            # 计算缩放比例
            max_size = max(img.width, img.height)
            scale = 1024 / max_size       #  设置长边最大像素值

            # 计算缩放后的尺寸
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)

            # 进行等比缩放
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 构建新的文件名
            new_filename = '{:04d}.png'.format(start_index)

            # 保存缩放后的图像到输出文件夹
            resized_img.save(os.path.join(output_folder, new_filename), 'PNG')  # 根据实际图像格式进行修改

            # 更新索引值
            start_index += 1

# 生成负样本txt标签文件
def generate_empty_txt_files():
    input_folder = 'E:/yolo负样本/1'  # 替换为实际的输入文件夹路径
    output_folder = 'E:/yolo负样本/label'  # 替换为实际的输出文件夹路径
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # 获取图片文件名（不包含扩展名）
            name = os.path.splitext(filename)[0]

            # 生成对应的空txt文件路径
            txt_path = os.path.join(output_folder, name + '.txt')

            # 创建空txt文件
            open(txt_path, 'w').close()

    print("空txt文件生成完成！")

if __name__ == '__main__':

    Image.MAX_IMAGE_PIXELS = 1000000000  # 设置合适的像素限制值
    # resize_and_rename_images()
    generate_empty_txt_files()