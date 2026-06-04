"""Mirrors the Java db/Main: builds four connection "profiles" through the default
constructor + attribute assignment. The Java Main produced no output; this prints each
result so the demo is observable."""

from .database_connection import DatabaseConnection


def run():
    # Scenario 1: Basic local development connection
    dev_conn = DatabaseConnection()
    dev_conn.host = "localhost"
    dev_conn.database = "myapp_dev"
    dev_conn.username = "dev_user"
    dev_conn.password = "dev_pass"

    # Scenario 2: Production connection with custom security and timeouts
    prod_conn = DatabaseConnection()
    prod_conn.host = "prod-db-cluster.company.com"
    prod_conn.port = 5432  # PostgreSQL
    prod_conn.database = "myapp_production"
    prod_conn.username = "prod_user"
    prod_conn.password = "complex_secure_password"
    prod_conn.use_ssl = True
    prod_conn.connection_timeout = 10000
    prod_conn.read_timeout = 120000
    prod_conn.connection_pool = "HikariCP"
    prod_conn.enable_logging = True

    # Scenario 3: Testing connection with specific charset and no SSL
    test_conn = DatabaseConnection()
    test_conn.host = "test-server"
    test_conn.database = "test_db"
    test_conn.username = "test_user"
    test_conn.password = "test_pass"
    test_conn.use_ssl = False
    test_conn.charset = "UTF-8"
    test_conn.auto_reconnect = False

    # Scenario 4: Analytics connection with custom timezone and logging
    analytics_conn = DatabaseConnection()
    analytics_conn.host = "analytics-db"
    analytics_conn.database = "warehouse"
    analytics_conn.username = "analytics_user"
    analytics_conn.password = "analytics_pass"
    analytics_conn.timezone = "UTC"
    analytics_conn.enable_logging = True
    analytics_conn.log_level = "DEBUG"
    analytics_conn.read_timeout = 300000  # 5 minutes for long queries

    print("Dev:       " + str(dev_conn))
    print("Prod:      " + str(prod_conn))
    print("Test:      " + str(test_conn))
    print("Analytics: " + str(analytics_conn))
