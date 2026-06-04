"""Solution 1 (pm1): the Citizen talks to a concrete PM that listens and resolves itself."""


class PM:
    def listen(self, problem):
        print("PM: Listening to you.")
        if self._sort_out(problem):
            self._resolve(problem)

    def find_job(self, name):
        print("PM: Don't ask me to find a job for you!")

    def _sort_out(self, problem):
        b = True
        # ...
        return b

    def _resolve(self, problem):
        print("PM: Please resolve this: " + problem)


class Citizen:
    def __init__(self, name, pm):
        self._name = name
        self._pm = pm

    def tell_problem(self):
        self._pm.listen("The problem is ...")

    def ask_for_job(self):
        self._pm.find_job(self._name)


def run():
    pm = PM()
    citizen = Citizen("John", pm)
    citizen.tell_problem()
    citizen.ask_for_job()
