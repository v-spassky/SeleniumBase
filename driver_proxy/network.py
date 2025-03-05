import logging
import re
import subprocess

logger = logging.getLogger(__name__)


def get_chromedriver_url() -> str:
    try:
        output = subprocess.check_output(["ps", "-aux"]).decode("utf-8")
        match = re.search(r"--port=(\d+)", output)
        if match:
            port = match.group(1)
            return f"http://localhost:{port}"
        else:
            raise RuntimeError("ChromeDriver process not found or port not detected.")
    except Exception as error:
        logger.error(f"Failed to determine ChromeDriver URL: {error}")
        raise
