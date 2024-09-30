class Processor:
    def __init__(self, index, power):
        self.index = index
        self.power = power
        self.is_free = True
        self.task_work_time = 0
        self.work_time = 0
        self.sleep_time = 0

    def get_index(self):
        return self.index

    def get_power(self):
        return self.power

    def set_index(self, index):
        self.index = index

    def set_power(self, power):
        self.power = power

    def is_free(self):
        return self.is_free

    def set_is_free(self, is_free):
        self.is_free = is_free

    def get_task_work_time(self):
        return self.task_work_time

    def set_task_work_time(self, task_work_time):
        self.task_work_time = task_work_time

    def get_work_time(self):
        return self.work_time

    def get_sleep_time(self):
        return self.sleep_time

    def reset_processor(self):
        self.task_work_time = 0
        self.work_time = 0
        self.sleep_time = 0

    def start(self):
        if self.is_free:
            self.sleep_time += 1
        else:
            self.work_time += 1
            self.task_work_time -= 1
            if(self.task_work_time == 0):
                self.is_free = True