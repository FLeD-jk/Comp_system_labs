class Task:
    def __init__(self, count_of_operations, processors):
        self.count_of_operations = count_of_operations
        self.processors = processors


    def get_count_of_operations(self):
        return self.count_of_operations

    def get_processors(self):
        return self.processors