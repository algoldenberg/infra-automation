import logging

def setup_logging():
    # Configure logging to write to provisioning.log
    # Format: timestamp - level - message
    logging.basicConfig(
        filename='logs/provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

# Global logger instance - import this in other modules
logger = setup_logging()