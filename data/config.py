from environs import Env


# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()
current_user_paths = {}
files_in_folders = {}
tasks_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Задачи'
solve_path = r'C:C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Решения'
tests_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Тесты'
documents_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Документы'
organizators_doc_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Документы\Организаторы'
students_doc_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Документы\Ученики'
teachers_doc_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Документы\Учителя'
complaints = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Жалобы\Жалобы.txt'
schedule = r'C:C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Расписание'
feedback = 'www.google.com'
events = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Мероприятия.json'
auditories = ['1', '2', '3']
submit_tasks_data = {}
discipline_rate_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Баллы по предметам'
add_users_path = r'C:\Programming\Фриланс. Заказы\aiogram-bot-template\Файлы\Добавленные пользователи'

ADMINS='319503958'
BOT_TOKEN='1870517443:AAFzS9-xdIfx-uuK6zgzCeRjDN1EFjfzdM8'