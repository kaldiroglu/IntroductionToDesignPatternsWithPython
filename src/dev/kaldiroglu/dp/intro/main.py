"""Runs the pm1/pm2/pm3 proxy demos and the db (telescoping-constructor) demo,
mirroring the Java Mains. The complexObject example has no Main in the Java repo,
so (like the original) it is import-only."""

from .problems.db import demo as db_demo
from .proxy.pm import pm1, pm2, pm3


def main():
    print("===== Solution 1 (pm1): Citizen -> PM =====")
    pm1.run()

    print()
    print("===== Solution 2 (pm2): Citizen -> Proxy -> PM =====")
    pm2.run()

    print()
    print("===== Solution 3 (pm3): Citizen -> ProxyPM -> RealPM (served by PMSecretary) =====")
    pm3.run()

    print()
    print("===== Problem: telescoping constructors / post-construction setters (db) =====")
    db_demo.run()


if __name__ == "__main__":
    main()
