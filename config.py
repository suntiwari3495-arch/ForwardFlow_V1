#!/usr/bin/env python3
"""
Configuration file for CNCF Issue Tracker Bot
Contains repository list and default settings.
"""

# Repository list to monitor
REPOSITORIES = [
    "open-telemetry/opentelemetry.io",
    "open-telemetry/opentelemetry-collector-contrib",
    "open-telemetry/opentelemetry-demo",
    "open-telemetry/opentelemetry-specification",
    "open-telemetry/community",
    "meshery/meshery",
    "meshery/meshery.io",
    "layer5io/docs",
    "kubernetes/website",
    "kubernetes/community",
    "kubernetes-sigs/contributor-playground",
    "kubernetes/enhancements",
]

# Default configuration values
DEFAULT_CHECK_INTERVAL = 60  # 1 minute for more real-time feel
DATABASE_PATH = "cncf_issues.db"
LOG_LEVEL = "INFO"
BATCH_SIZE = 3
BATCH_DELAY = 2
NOTIFICATION_DELAY = 1
API_TIMEOUT = 10
CHECK_BUFFER_MINUTES = 2