import os
import shutil
import time

FILE_EXTENSION = ['jpeg', 'tif', 'ai', 'eps', 'cdr', 'png', 'psd', 'jpg', 'pdf']


def _get_list_folders(path):
    return [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(curr_dir, folder))]


curr_dir = input('Введите адрес папки ИЗ которой нужно вытащить все изображения: ')
target_folder_tmp = input('Введите адрес папки В которую нужно переместить изображения: ')
target_folder = os.path.join(target_folder_tmp, 'all_images')
print('-' * 40)
print(f'Путь куда будут перемещены все изображения {target_folder}')
if not os.path.exists(target_folder):
    os.mkdir(target_folder)
#  размер в мб
target_folder_free_size = round(shutil.disk_usage(target_folder).free / 1024 / 1024, 2)
print('Считаю общий объем всех фотографий ...')

folders = _get_list_folders(curr_dir)
file_size_total = 0
file_size_count = 0
curr_time = time.time()

for folder in folders:
    # пробегаемся по всем папкам
    for file in os.listdir(os.path.join(curr_dir, folder)):
        if os.path.isfile(os.path.join(curr_dir, folder, file)) \
                and os.path.join(curr_dir, folder, file).split('.')[-1].lower() in FILE_EXTENSION:
            # размер в мб
            file_size = round(os.stat(os.path.join(curr_dir, folder, file)).st_size / 1024 / 1024, 4)
            file_size_total += file_size
            file_size_count += 1
            print(os.path.join(curr_dir, folder, file), file_size)  # для удобства вывожу в мб

print('-' * 40)
print(f'Доступный объем свободного места: {round(target_folder_free_size / 1024, 2)} Гб')
print(f'Кол-во всех изображений для перемещения: {file_size_count} шт')
print(f'Общий вес всех изображений для перемещения: {round(file_size_total, 4)} Мб')


# блок скачивания
if file_size_total < target_folder_free_size:
    print('Выполняю скачивание ...')
    for folder in folders:
        # пробегаемся по всем папкам
        for file in os.listdir(os.path.join(curr_dir, folder)):
            file_path = os.path.join(curr_dir, folder, file)
            if os.path.isfile(file_path) \
                    and file_path.split('.')[-1].lower() in FILE_EXTENSION:
                shutil.move(file_path, target_folder)


# #
print('-' * 40)
print('Перемещение завершено')
print(f'Время выполнения: {round((time.time() - curr_time), 2)} секунд')
time.sleep(40)
