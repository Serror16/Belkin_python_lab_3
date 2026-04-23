from src.sources import GeneratorSource, FileTaskSource, ApiTaskSource
from src.receiver import collect_tasks

sources = [
    GeneratorSource(),
    FileTaskSource("tasks.txt"),
    ApiTaskSource(),
]

task_stream = collect_tasks(sources)

print("Начинаю обработку задач:")
for task in task_stream:
    print(f"Выполняю: {task}")
