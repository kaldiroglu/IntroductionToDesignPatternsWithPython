"""Solution 2 (pm2): a Proxy sorts out and delegates to the PM; the Citizen knows the Proxy."""


class PM:
    def listen(self, problem):
        print("PM: Listening to you.")
        self._resolve(problem)

    def find_job(self, name):
        print("PM: Don't ask me to find a job for you!")

    def _resolve(self, problem):
        print("PM: Please resolve this: " + problem)


class Proxy:
    def __init__(self, pm):
        self._pm = pm

    def listen(self, problem):
        print("Proxy: Listening to you.")
        if self._sort_out(problem):
            self._delegate(problem)

    def find_job(self, name):
        print("Proxy: 'I'll find out what I can do for you!'")

    def _delegate(self, problem):
        self._pm.listen(problem)

    def _sort_out(self, problem):
        b = True
        # ...
        return b


class Citizen:
    def __init__(self, name, proxy):
        self._name = name
        self._proxy = proxy

    def tell_problem(self):
        self._proxy.listen("The problem is ...")

    def ask_for_job(self):
        self._proxy.find_job(self._name)


def run():
    pm = PM()
    proxy = Proxy(pm)
    citizen = Citizen("John", proxy)
    citizen.tell_problem()
    citizen.ask_for_job()
