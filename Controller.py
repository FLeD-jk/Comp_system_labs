from Processor import Processor
from Task import Task
from Processors_list import List_of_Processors

import random

class Controller:
    def __init__(self):
        self.number_of_processors = 5
        self.processors = []
        self.min_task_time = 10
        self.max_task_time = 200
        self.number_of_tasks = 10000
        self.Probability_of_task = 70

    def create_processors(self):
        for i in range(self.number_of_processors):
            power_of_processor = int(input(f"Enter power amount for processor with id {i}: "))
            self.processors.append(Processor(i, power_of_processor))

    def generate_tasks(self):
        tasks = []
        min_processor_power = min(processor.get_power() for processor in self.processors)
        min_task_complexity = self.min_task_time * min_processor_power
        max_task_complexity = self.max_task_time * min_processor_power
        list_of_processors = List_of_Processors()
        size_of_list_of_processors = len(list_of_processors.get_list_processors())

        for _ in range(self.number_of_tasks):
            count_of_operations = random.randint(min_task_complexity, max_task_complexity)
            processors = list_of_processors.get_list_processors()[random.randint(0, size_of_list_of_processors - 1)]
            tasks.append(Task(count_of_operations, processors))
        return tasks

    def search_processor_for_task(self, task):
        for i in range(self.number_of_processors):
            if self.processors[i].is_free and i in task.get_processors():
                return i
        return -1

    def is_processor_free(self):
        return all(processor.is_free for processor in self.processors)

    def search_task_for_processor(self, processor, tasks):
        for task in tasks:
            if processor.get_index() in task.get_processors():
                return task
        return None

