class DatabaseConnection:
    """Faithful port of the Java DatabaseConnection. It deliberately demonstrates the
    "telescoping constructor" problem (plus post-construction setters) that the Builder
    pattern is meant to solve. Python has no constructor overloading, so the defaults live
    in __init__ and callers set attributes afterwards - exactly what the demo does."""

    def __init__(self):
        # Set reasonable defaults
        self.host = None
        self.port = 3306
        self.database = None
        self.username = None
        self.password = None
        self.use_ssl = True
        self.connection_timeout = 30000
        self.read_timeout = 60000
        self.charset = "UTF-8"
        self.auto_reconnect = True
        self.max_retries = 3
        self.connection_pool = None
        self.enable_logging = False
        self.log_level = "INFO"
        self.timezone = None

    def __str__(self):
        return (
            f"DatabaseConnection[host={self.host}, port={self.port}, "
            f"database={self.database}, useSSL={self.use_ssl}, "
            f"connectionTimeout={self.connection_timeout}, readTimeout={self.read_timeout}, "
            f"charset={self.charset}, autoReconnect={self.auto_reconnect}, "
            f"maxRetries={self.max_retries}, connectionPool={self.connection_pool}, "
            f"enableLogging={self.enable_logging}, logLevel={self.log_level}, "
            f"timezone={self.timezone}]"
        )


# Why constructors would be problematic here:
#
# 1. COMBINATORIAL EXPLOSION: With 15 properties, we'd need potentially hundreds of
#    constructor overloads to cover meaningful combinations.
# 2. PARAMETER CONFUSION: A constructor with 8+ parameters becomes error-prone -
#    which timeout is which? Easy to mix up port and timeout values.
# 3. MEANINGLESS COMBINATIONS: Not every combination makes sense.
# 4. MAINTENANCE NIGHTMARE: Adding one new property means many new constructors.
# 5. UNCLEAR INTENT: Post-construction initialization makes it clear which properties
#    are being customized for each use case.
# 6. FLEXIBILITY: Easy to create different "profiles" without predefined constructors.
