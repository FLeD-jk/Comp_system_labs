from Processor import Processor
from Task import Task
from Processors_list import List_of_Processors

import random


# noinspection PyStatementEffect
class Controller:
    def __init__(self):
        self.number_of_processors = 5
        self.processors = []
        self.min_task_time = 10
        self.max_task_time = 200
        self.number_of_tasks = 10000
        self.Probability_of_task = 45

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

    @staticmethod
    def search_task_for_processor(processor, tasks):
        for task in tasks:
            if processor.get_index() in task.get_processors():
                return task
        return None

    def result_analyzer(self, run_time, n):
        count_of_operations = 0

        for i in range(n, self.number_of_processors):
                processor = self.processors[i]
                print(f"Processor with ID {i} worked {processor.get_work_time()} and slept {processor.get_sleep_time()}")
                count_time = (10000 * processor.get_work_time()) / run_time
                count_of_operations += int(processor.get_power() * count_time)

        theoretical_operations_value = sum(
            processor.get_power() * 10000 for processor in self.processors[n:])
        print(f"Count of operations in 10 seconds: {count_of_operations}")
        print(f"Theoretical operations value in 10 seconds: {theoretical_operations_value}")
        print(f"Efficiency: {count_of_operations / theoretical_operations_value * 100:.2f} %")



    def FIFO(self):
        tasks = self.generate_tasks()
        run_time = 0
        for processor in self.processors:
            processor.reset_processor()

        task_index = 0
        while True:
            if random.randint(0, 100) < self.Probability_of_task:
                if task_index < len(tasks):
                    task = tasks[task_index]
                    processor_id = self.search_processor_for_task(task)
                    if processor_id > -1:
                        self.processors[processor_id].set_is_free(False)
                        self.processors[processor_id].set_task_work_time(
                            task.get_count_of_operations() // self.processors[processor_id].get_power())
                        task_index += 1

            for processor in self.processors:
                processor.start()

            run_time += 1

            if task_index >= len(tasks) and self.is_processor_free():
                break

        self.result_analyzer(run_time, 0)


    def Weak_processor(self):
        tasks = self.generate_tasks()
        run_time = 0
        for processor in self.processors:
            processor.reset_processor()


        while True:
            for i in range(1, self.number_of_processors):
                processor = self.processors[i]
                if processor.is_free:
                    task = self.search_task_for_processor(processor, tasks)
                    if task is not None:
                        processor.set_is_free(False)
                        processor.set_task_work_time(task.get_count_of_operations() // processor.get_power())
                        tasks.remove(task)

            for processor in self.processors:
                processor.start()

            run_time += 1

            if task_index >= len(tasks) and self.is_processor_free():
                break

        self.result_analyzer(run_time, 1)



    def strong_processor(self, work_time, plan_time):
        tasks = self.generate_tasks()
        time_work_and_sleep = 0
        run_time = 0
        for processor in self.processors:
            processor.reset_processor()


        while True:
            for i in range(0, self.number_of_processors):
                processor = self.processors[i]
                if processor.is_free:
                    task = self.search_task_for_processor(processor, tasks)
                    if task is not None:
                        processor.set_is_free(False)
                        processor.set_task_work_time(task.get_count_of_operations() // processor.get_power())
                        tasks.remove(task)

            for processor in self.processors:
                processor.start()

            run_time += 1

            if time_work_and_sleep <= work_time:
                time_work_and_sleep += 1

            elif time_work_and_sleep <= work_time + plan_time:
                self.processors[4].set_is_free(False)
                time_work_and_sleep += 1

            else:
                self.processors[4].set_is_free(True)
                time_work_and_sleep = 0

            if task_index >= len(tasks) and self.is_processor_free():
                break


        self.result_analyzer(run_time, 0)


'''
    def Weak_processor(self):
        tasks = self.generate_tasks()
        run_time = 0

        for processor in self.processors:
            processor.reset_processor()


        weakest_processor = self.find_weakest_processor()


        while True:
            for processor in self.processors:
                if processor != weakest_processor and processor.is_free:
                    task = self.search_task_for_processor(processor, tasks)
                    if task is not None:
                        processor.set_is_free(False)
                        processor.set_task_work_time(task.get_count_of_operations() // processor.get_power())
                        tasks.remove(task)


            for processor in self.processors:
                if processor != weakest_processor:

            run_time += 1


            if not tasks:
                check_free = self.is_processor_free()
                if check_free:
                    break

        self.result_analyzer(run_time, 0, None)

    def find_weakest_processor(self):
        weakest = self.processors[0]
        for processor in self.processors:
            if processor.get_power() < weakest.get_power():
                weakest = processor
        return weakest

'''
