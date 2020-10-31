from copy import copy


class Estate:
    def __init__(self, estate, solution):
        self.estate = estate
        self.solution = solution
        self.node = None
        self.sons = []

    def is_solution(self):
        for j, i in enumerate(self.estate):
            if i != self.solution[j]:
                return False
        return True

    def is_valid(self, _estate):
        estate = Estate(_estate,self.solution)
        estate.node = self
        self.sons.append(estate)

    def find_states(self):
        for i in range(len(self.estate)):
            _estate = copy(self.estate)
            if self.estate[i] == '<':

                if self.estate[i - 1] == '>' and self.estate[i - 2] == '_':
                    _estate[i] = self.estate[i - 2]
                    _estate[i - 2] = self.estate[i]
                    self.is_valid(_estate)

                if self.estate[i - 1] == '_':
                    _estate[i] = self.estate[i - 1]
                    _estate[i - 1] = self.estate[i]
                    self.is_valid(_estate)

            if self.estate[i] == '>':

                if self.estate[i + 1] == '<' and self.estate[i + 2] == '_':
                    _estate[i] = self.estate[i + 2]
                    _estate[i + 2] = self.estate[i]
                    self.is_valid(_estate)

                if self.estate[i + 1] == '_':
                    _estate[i] = self.estate[i + 1]
                    _estate[i + 1] = self.estate[i]
                    self.is_valid(_estate)



    def __str__(self):
        output = ""
        for i in self.estate[1:-1]:
            output += i
        return output


class solution_Arrow:
    def __init__(self):
        self.tree = [Estate([" ", ">", ">", ">", "_", "<", "<", "<", " "],[" ", "<", "<", "<", "_", ">", ">", ">", " "])]
        self.solution = None

    def solve(self):
        for solution in self.tree:
            if solution.is_solution():
                self.solution = [solution]
                while solution.node:
                    self.solution.insert(0, solution.node)
                    solution = solution.node
                break
            solution.find_states()
            self.tree.extend(solution.sons)


def show_states():
    arrow_problem = solution_Arrow ()
    arrow_problem.solve()
    print ("     ESTADO INICIAL ")
    # i = 1
    for i in range(1,len(arrow_problem.solution)):
        print("Estate {number} : {estate}".format(number=i,estate=arrow_problem.solution[i]))
    print("Estate {number} : {estate}".format(number=i, estate=arrow_problem.solution[i]), end=" ")
    
show_states()