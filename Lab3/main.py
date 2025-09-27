"""need imports"""
import my_function


def demonstrate_my_function():
    """Демонстрирует работу всех фитнес-функций."""

    print("*** ФИТНЕС-ТРЕКЕР: ДЕМОНСТРАЦИЯ ФУНКЦИЙ ***\n")

    # 1. Функция без параметров
    print("Функция без параметров")
    print(f"    {my_function.get_motivation()}\n")

    # 2. Функция с параметрами
    print("Функция с параметрами")
    print(f"    {my_function.calculate_calories_burned('бег', 30)}\n")

    # 3. Функция с несколькими параметрами со значениями по умолчанию
    print("Функция с несколькими параметрами со значениями по умолчанию")
    workout_plan_1 = my_function.create_workout_plan("йога")
    workout_plan_2 = my_function.create_workout_plan("кроссфит", 90, "высокая")
    print(f"    {workout_plan_1}\n")
    print(f"    {workout_plan_2}\n")

    # 4. Функция с несколькими параметрами, у которых задан тип
    print("Функция с несколькими параметрами, у которых задан тип")
    print(f"    ИМТ: {my_function.calculate_bmi(80, 1.75)}\n")

    # 5. Функция с неопределённым количеством параметров (args)
    print("Функция с неопределённым количеством параметров (args)")
    workout_log = my_function.log_workout_exercises("приседания", "отжимания", "планка", "бег")
    for exercise in workout_log:
        print(f"    {exercise}")
    print()

    # 6. Функция с неопределённым количеством параметров (kwargs)
    print("Функция с неопределённым количеством параметров (kwargs)")
    fitness_proile = my_function.create_fitness_profile(
        name="Александр",
        age=21,
        weight=110,
        height=175,
        goal="Похудение",
        activity_level="низкий"
    )
    print(fitness_proile)

    # 7. Функция, вызывающая внутри себя другую функцию
    print("Функция, вызывающая внутри себя другую функцию")
    print(f"    {my_function.get_workout_summary('плавание', 45)}\n")

    # 8. Функция, принимающая функцию как параметр (3 примера)
    print("Функции, принимающие функции как параметр:")

    sample_workouts = [
        {"type": "бег", "duration": 40, "calories": 320},
        {"type": "йога", "duration": 60, "calories": 180},
        {"type": "силовая", "duration": 50, "calories": 280}
    ]

    print("    Пример 1 - анализ длительности:")
    durations = my_function.analyze_workout_data(
        sample_workouts,
        lambda workout: f"{workout['type']}: {workout['duration']} мин"
    )
    for item in durations:
        print(f"        {item}")

    print("    Пример 2 - интенсивные тренировки:")
    intense_workouts = my_function.filter_workouts(
        sample_workouts,
        lambda workout: workout['calories'] > 200
    )
    for workout in intense_workouts:
        print(f"        {workout['type']} - {workout['calories']} ккал")

    print("    Пример 3 - сортировка по калориям:")
    sorted_by_calories = my_function.sort_workouts(
        sample_workouts,
        lambda workout: workout['calories']
    )
    for workout in sorted_by_calories:
        print(f"        {workout['type']} - {workout['calories']} ккал")
    print()

    # 9. Функция с объявленной внутри локальной функцией (2 примера)
    print("Функция с объявленной внутри локальной функцией (2 примера)")

    weekly_workouts = [
        {"type": "бег", "duration": 180, "calories": 1440},
        {"type": "силовая", "duration": 120, "calories": 600},
        {"type": "йога", "duration": 60, "calories": 180}
    ]

    print("    Пример 1 - статистика за неделю:")
    stats = my_function.calculate_workout_statistics(weekly_workouts)
    for key, value in stats.items():
        print(f"        {key}: {value}")

    print("    Пример 2 - анализ интенсивности:")
    workout_analyzer = my_function.create_workout_analyzer()
    analysis_result = workout_analyzer(weekly_workouts)
    for key, value in analysis_result.items():
        print(f"        {key}: {value}")
    print()

    # 10. Лямбда-выражение без параметров
    print("Лямбда-выражение без параметров")
    print(f"    {my_function.get_energy_message()}\n")

    # 11. Лямбда-выражение с параметрами
    print("Лямбда-выражение с параметрами")
    print(f"    Рекомендуемое потребление воды: "
          f"{my_function.calculate_water_intake(70, 2):.1f} л/день\n")

    # 12. Функция, принимающая лямбда-выражение как параметр
    print("Функция, принимающая лямбда-выражение как параметр")
    intensity_calc = lambda level: level * 1.5 + 2
    print(f"    Рекомендация по интенсивности: "
          f"{my_function.recommend_workout_intensity(4, intensity_calc)}\n")

    # 13. Функция с замыканиями (3 примера)
    print("Функция с замыканиями (3 примера)")

    print("    Пример 1 - счетчик калорий:")
    add_calories = my_function.create_calorie_counter()
    print(f"        {add_calories(300)}")
    print(f"        {add_calories(150)}")

    print("    Пример 2 - трекер беговой цели:")
    running_goal = my_function.create_goal_tracker("бег", 50)  # цель 50 км
    print("        Пробежали 15 км")
    progress1 = running_goal(15)  # Пробежали 15 км
    for key, value in progress1.items():
        print(f"            {key}: {value}")
    print("        Пробежали еще 20 км")
    progress2 = running_goal(20)  # Еще 20 км
    for key, value in progress2.items():
        print(f"            {key}: {value}")

    print("    Пример 3 - напоминания о тренировках:")
    remind_workout, get_count = my_function.create_workout_reminder("19:00")
    print(f"        {remind_workout('понедельник')}")
    print(f"        {remind_workout('среду')}")
    print(f"        Всего напоминаний: {get_count()}")


if __name__ == '__main__':
    demonstrate_my_function()
