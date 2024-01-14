import os
import shutil
import sys

def copy_files(src, dest):
    """
    Функція для копіювання файлів з src в dest, розсортовуючи за розширеннями.
    """
    try:
        for item in os.listdir(src):
            path = os.path.join(src, item)
            if os.path.isdir(path):
                # Рекурсивний виклик для піддиректорій
                copy_files(path, dest)
            else:
                # Визначення піддиректорії на основі розширення файлу
                ext = os.path.splitext(item)[1][1:]  # Видалення крапки з розширення
                dest_path = os.path.join(dest, ext)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                # Копіювання файлу
                shutil.copy2(path, os.path.join(dest_path, item))
    except Exception as e:
        print(f"Помилка при обробці файлу {path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної директорії.")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files(src_dir, dest_dir)
    print(f"Файли з {src_dir} було успішно скопійовано до {dest_dir}")

if __name__ == "__main__":
    main()
