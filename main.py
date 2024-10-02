from Controller import Controller





if __name__ == '__main__':
    controller = Controller()
    controller.create_processors()


    controller.FIFO()
    controller.Weak_processor()
    controller.strong_processor(20,4)
    controller.strong_processor(34,67)



