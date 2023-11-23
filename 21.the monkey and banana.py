class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = "A"
        self.box_position = "A"
        self.bananas_hanging = False

    def move_monkey(self, position):
        self.monkey_position = position

    def move_box(self, position):
        self.box_position = position

    def climb_on_box(self):
        if self.monkey_position == self.box_position and self.box_position == "B":
            self.bananas_hanging = True

    def solve_problem(self):
        print("Initial state:")
        self.display_state()

        print("\nMoving the box to position B...")
        self.move_box("B")
        self.display_state()

        print("\nMoving the monkey to position B...")
        self.move_monkey("B")
        self.display_state()

        print("\nClimbing on the box to reach the bananas...")
        self.climb_on_box()
        self.display_state()

        if self.bananas_hanging:
            print("\nCongratulations! The monkey reached the bananas.")
        else:
            print("\nThe monkey couldn't reach the bananas.")

    def display_state(self):
        print(f"Monkey Position: {self.monkey_position}, Box Position: {self.box_position}, Bananas Hanging: {self.bananas_hanging}")


# Create an instance of the MonkeyBananaProblem
monkey_problem = MonkeyBananaProblem()

# Solve the problem
monkey_problem.solve_problem()
