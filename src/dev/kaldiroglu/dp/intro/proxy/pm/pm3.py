"""Solution 3 (pm3): PM is an interface (the Subject). RealPM and ProxyPM implement it;
PMSecretary is a factory that hands the Citizen a ProxyPM typed as PM."""

from abc import ABC, abstractmethod


class PM(ABC):
    @abstractmethod
    def listen(self, problem):
        ...

    @abstractmethod
    def find_job(self, name):
        ...


class RealPM(PM):
    def listen(self, problem):
        print("RealPM: Listening to you.")
        self._resolve(problem)

    def find_job(self, name):
        print("RealPM: Don't ask me to find a job for you!")

    def _resolve(self, problem):
        print("RealPM: Please resolve this: " + problem)


class ProxyPM(PM):
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


class PMSecretary:
    def __init__(self):
        self._pm = ProxyPM(RealPM())

    # Package-private in Java (getMePM); the Citizen, which lives alongside it, calls it.
    def get_me_pm(self):
        return self._pm


class Citizen:
    def __init__(self, name, secretary):
        self._name = name
        self._pm = secretary.get_me_pm()

    def tell_problem(self):
        self._pm.listen("The problem is ...")

    def ask_for_job(self):
        self._pm.find_job(self._name)


def run():
    print("Everything starts with a citizen coming to PM Secretary and asking for PM")
    secretary = PMSecretary()
    citizen = Citizen("John", secretary)
    citizen.tell_problem()
    citizen.ask_for_job()
