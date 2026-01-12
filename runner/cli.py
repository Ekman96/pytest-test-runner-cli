import argparse
import os
import subprocess
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Run PyTest suites and generate reports.")
    parser.add_argument(
        "--suite",
        choices=["smoke", "regression", "all"],
        default="all",
        help="Which test suite to run"
    )
    args = parser.parse_args()

    # Create artifacts folder if it doesn't exist
    os.makedirs("artifacts", exist_ok=True)

    # Timestamp for unique report names
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Base pytest command
    cmd = ["pytest"]

    # If user selected a suite, run only those marked tests
    if args.suite != "all":
        cmd += ["-m", args.suite]

    # Add reports (HTML + JUnit XML)
    cmd += [
        f"--html=artifacts/report_{args.suite}_{ts}.html",
        "--self-contained-html",
        f"--junitxml=artifacts/junit_{args.suite}_{ts}.xml",
    ]

    print("Running:", " ".join(cmd))

    # Run pytest as a subprocess so the CLI returns the same exit code (pass/fail)
    result = subprocess.run(cmd)
    raise SystemExit(result.returncode)

if __name__ == "__main__":
    main()
