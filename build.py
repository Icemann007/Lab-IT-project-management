import subprocess


def build_project():
    print("Початок збірки Django проекту")

    # Створення віртуального середовища
    subprocess.run(["python", "-m", "venv", "venv"])

    # Активація віртуального середовища на Windows
    subprocess.run([r".\venv\Scripts\activate.bat"])

    # Встановлення залежностей Python з requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    subprocess.run(["python", "manage.py", "runserver"])

    print("Збірка завершена")


if __name__ == "__main__":
    build_project()
