CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    log_type TEXT,
    method TEXT,
    endpoint TEXT,
    status INTEGER,
    response_time_ms REAL,
    message TEXT
);

CREATE TABLE IF NOT EXISTS requests (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    log_type TEXT,
    method TEXT,
    endpoint TEXT,
    response_time_ms REAL,
    query TEXT,
    data JSONB,
    message TEXT
);

CREATE TABLE IF NOT EXISTS errors (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    log_type TEXT,
    method TEXT,
    endpoint TEXT,
    error_type TEXT,
    response_time_ms REAL,
    message TEXT
);
