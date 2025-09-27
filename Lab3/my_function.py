"""
Модуль с функциями для работы с библиотекой книг.
Все функции логически связаны с управлением книжной коллекцией.
"""
import typing


# 1. Функция без параметров
def get_motivation():
    """Возвращает мотивационное сообщение."""
    return "Сегодня отличный чтобы похудеть! Ты сможешь!"


# 2. Функция с параметрами
def calculate_calories_burned(exercise: str, duration: int):
    """Рассчитывает сожженные калории для упражнения."""
    calories_rate = 8  # дефолтное значение калорий в минуту
    return f"За {duration} мин {exercise} сожжено {calories_rate * duration} ккал."


# 3. Функция с несколькими параметрами со значениями по умолчанию
def create_workout_plan(workout_type: str, duration: int = 60, intensity: str = "средняя"):
    """Создает план тренировки."""
    return f"План: {workout_type}, {duration} мин, интенсивность: {intensity}"


# 4. Функция с несколькими параметрами, у которых задан тип
def calculate_bmi(weight: float, height: float) -> float:
    """Рассчитывает индекс массы тела."""
    return round(weight / (height ** 2), 2)


# 5. Функция с неопределённым количеством параметров (args)
def log_workout_exercises(*exercises):
    """Логирует выполненные упражнения за тренировку."""
    workout_log = []
    for i, exercise in enumerate(exercises, 1):
        workout_log.append(f"{i} - {exercise}")
    return workout_log


# 6. Функция с неопределённым количеством параметров (kwargs)
def create_fitness_profile(**user_info):
    """Создает фитнес-профиль пользователя."""
    profile = "Фитнес-профиль:\n"
    for key, value in user_info.items():
        profile += f"    {key}: {value}\n"
    return profile


# 7. Функция, вызывающая внутри себя другую функцию
def get_workout_summary(workout_type: str, duration: int):
    """Возвращает сводку по тренировке с расчетом калорий."""
    return f"Тренировка завершена! {calculate_calories_burned(workout_type, duration)}"


# 8. Функция, принимающая функцию как параметр (3 примера)
def analyze_workout_data(workouts: typing.List[typing.Dict],
                         analysis_func: typing.Callable) -> typing.List:
    """Анализирует данные тренировок с помощью переданной функции."""
    return [analysis_func(workout) for workout in workouts]


def filter_workouts(workouts: typing.List[typing.Dict],
                    condition_func: typing.Callable) -> typing.List[typing.Dict]:
    """Фильтрует тренировки по заданному условию."""
    return [workout for workout in workouts if condition_func(workout)]


def sort_workouts(workouts: typing.List[typing.Dict],
                  key_func: typing.Callable) -> typing.List[typing.Dict]:
    """Сортирует тренировки по ключу."""
    return sorted(workouts, key=key_func)


# 9. Функция с объявленной внутри локальной функцией (2 примера)
def calculate_workout_statistics(workouts: typing.List[typing.Dict]):
    """Рассчитывает статистику тренировок."""

    def get_total_duration():
        return sum(workout['duration'] for workout in workouts)

    def get_average_calories():
        return sum(workout['calories'] for workout in workouts) / len(workouts) if workouts else 0

    def get_most_frequent_type():
        types = [workout['type'] for workout in workouts]
        return max(set(types), key=types.count) if types else "нет данных"

    return {
        "total_workouts": len(workouts),
        "total_duration_min": get_total_duration(),
        "avg_calories": round(get_average_calories(), 1),
        "most_popular_type": get_most_frequent_type()
    }


def create_workout_analyzer():
    """Создает анализатор тренировок с локальными функциями."""

    def categorize_workout(workout: typing.Dict) -> str:
        """Категоризирует тренировку по интенсивности."""
        score = round((workout['calories'] / workout['duration']), 2) \
            if workout['duration'] > 0 else 0
        if score >= 8:
            return "Высокая интенсивность"
        if score >= 5:
            return "Средняя интенсивность"
        return "Низкая интенсивность"

    def analyze_weekly_progress(weekly_workouts: typing.List[typing.Dict]) -> typing.Dict:
        """Анализирует прогресс за неделю."""
        categorized = [categorize_workout(workout) for workout in weekly_workouts]

        high_intensity = categorized.count("Высокая интенсивность")
        medium_intensity = categorized.count("Средняя интенсивность")
        low_intensity = categorized.count("Низкая интенсивность")

        total_calories = sum(workout['calories'] for workout in weekly_workouts)
        total_duration = sum(workout['duration'] for workout in weekly_workouts)

        return {
            "high_intensity_workouts": high_intensity,
            "medium_intensity_workouts": medium_intensity,
            "low_intensity_workouts": low_intensity,
            "total_calories_burned": total_calories,
            "total_training_time": total_duration,
        }

    return analyze_weekly_progress


# 10. Лямбда-выражение без параметров
get_energy_message = lambda: "Время зарядиться энергией!"

# 11. Лямбда-выражение с параметрами
calculate_water_intake = lambda weight, activity_level: weight * 0.03 + activity_level * 0.5


# 12. Функция, принимающая лямбда-выражение как параметр
def recommend_workout_intensity(fitness_level: int, calculation_lambda: typing.Callable) -> str:
    """Рекомендует интенсивность тренировки на основе лямбда-функции."""
    intensity_score = calculation_lambda(fitness_level)
    if intensity_score >= 8:
        return "Высокая интенсивность"
    if intensity_score >= 5:
        return "Средняя интенсивность"
    return "Низкая интенсивность"


# 13. Функция с замыканиями (3 примера)
def create_calorie_counter():
    """Создает счетчик калорий с замыканием."""
    total_calories = 0

    def add_calories(calories: int) -> int:
        nonlocal total_calories
        total_calories += calories
        return total_calories

    return add_calories


def create_goal_tracker(goal_type: str, target_value: float):
    """Создает трекер цели с замыканием."""
    current_value = 0.0

    def update_progress(value: float) -> typing.Dict:
        nonlocal current_value
        current_value += value
        progress = (current_value / target_value) * 100
        return {
            'goal_type': goal_type,
            'current': current_value,
            'target': target_value,
            'progress': round(progress, 1)
        }

    return update_progress


def create_workout_reminder(workout_time: str):
    """Создает напоминание о тренировке с замыканием."""
    reminder_count = 0

    def remind(day: str) -> str:
        nonlocal reminder_count
        reminder_count += 1
        return f"Напоминание #{reminder_count}: Тренировка в {workout_time} в {day}"

    def get_reminder_count() -> int:
        return reminder_count

    return remind, get_reminder_count
