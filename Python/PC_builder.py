class Computer:
    def __init__(self):
        self.price = 0

        self.processor = None
        self.change_processor()

        self.generation = None
        self.change_generation()

        self.ram = None
        self.change_ram()

        self.space = None
        self.change_space()

    def change_processor(self):
        self.processor = input(
            "Please enter your choice for processor :\n\t1. i3\n\t2. i5\n\t3. i7\n\t4. i9\n(1/2/3/4) : ")
        try:
            self.processor = int(self.processor)

            if self.processor < 1 or self.processor > 4:
                raise ValueError
        except ValueError:
            while self.processor not in (1, 2, 3, 4):
                try:
                    self.processor = int(input("Invalid!! Please enter (1/2/3/4) : "))
                except:
                    pass
        finally:
            if self.processor == 1:
                self.processor = "i3"
                self.price += 100
            elif self.processor == 2:
                self.processor = "i5"
                self.price += 175
            elif self.processor == 3:
                self.processor = "i7"
                self.price += 250
            elif self.processor == 4:
                self.processor = "i9"
                self.price += 350

    def change_generation(self):
        self.generation = input("Please enter the generation of your processor (6/7/8/9/10/11) : ")
        try:
            self.generation = int(self.generation)

            if self.generation < 6 or self.generation > 11:
                raise ValueError
        except ValueError:
            while self.generation not in (6, 7, 8, 9, 10, 11):
                try:
                    self.generation = int(input("Invalid!! Please enter (6/7/8/9/10/11) : "))
                except:
                    pass
        finally:
            if self.generation == 6:
                self.price += 20
            elif self.generation == 7:
                self.price += 25
            elif self.generation == 8:
                self.price += 30
            elif self.generation == 9:
                self.price += 35
            elif self.generation == 10:
                self.price += 45
            elif self.generation == 11:
                self.price += 55

    def change_ram(self):
        self.ram = input("Enter the amount of RAM in GB : ")
        try:
            self.ram = int(self.ram)

            if self.ram <= 0:
                raise ValueError
        except ValueError:
            while self.ram > 0:
                try:
                    self.ram = int(input("Invalid!! Please enter a value greater than 0 : "))
                except:
                    pass
        finally:
            if self.ram < 3:
                self.price += 20
            elif self.ram < 6:
                self.price += 30
            elif self.ram < 12:
                self.price += 55
            elif self.ram <= 16:
                self.price += 80
            else:
                self.price += self.ram * 6

    def change_space(self):
        self.space = input(
            "Please enter your choice for Disk Space :\n\t1. 128 GB\n\t2. 256 GB\n\t3. 512 GB\n\t4. 1 TB\n(1/2/3/4) : ")
        try:
            self.space = int(self.space)

            if self.space < 1 or self.space > 4:
                raise ValueError
        except ValueError:
            while self.space not in (1, 2, 3, 4):
                try:
                    self.space = int(input("Invalid!! Please enter (1/2/3/4) : "))
                except:
                    pass
        finally:
            if self.space == 1:
                self.space = "128 GB"
                self.price += 30
            elif self.space == 2:
                self.space = "256 GB"
                self.price += 175
            elif self.space == 3:
                self.space = "512 GB"
                self.price += 250
            elif self.space == 4:
                self.space = "1 TB"
                self.price += 350


if __name__ == "__main__":
    print("===== Welcome to your favorite pc shop! =====\n")
    choice = input("Wanna build a pc? (y/n) : ").lower()

    while choice not in ('y', 'n'):
        choice = input("Invalid!! Please enter (y/n) : ").lower()

    if choice == 'y':
        your_pc = Computer()

        print("\nYou have successfully built your pc!")
        print("Your pc configuration is --->")
        print("Processor : Intel core ", your_pc.processor, " ", your_pc.generation, "th Generation", sep = "")
        print("RAM :", your_pc.ram, "GB")
        print("Disk space :", your_pc.space)

        print("Total price ===> $", your_pc.price, sep ="")

        print("\n===== Thanks for buying a pc! =====")
    else:
        print("\n===== Thanks for visiting! =====")
