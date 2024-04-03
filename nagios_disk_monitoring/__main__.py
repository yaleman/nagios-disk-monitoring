from pathlib import Path
import shutil
import sys
import click

from nagios_disk_monitoring import NagiosResult


@click.command()
@click.option("--warning", "-w", type=int, default=80, help="Warning threshold")
@click.option("--critical", "-c", type=int, default=95, help="Critical threshold")
@click.option("--debug", "-d", is_flag=True, help="Enable debug mode")
@click.argument("path", type=click.Path())
def cli(path: str, warning: int, critical: int, debug: bool = False) -> None:
    if debug:
        print(f"Warning threshold: {warning}")
        print(f"Critical threshold: {critical}")
        print(f"Path: {path}")

    if not Path(path).exists():
        print(f"UNKNOWN: path={path} does not exist")
        sys.exit(NagiosResult.UNKNOWN)

    if warning > critical:
        print(
            f"UNKNOWN: Critical threshold must be higher than warning threshold {critical=} {warning=}"
        )
        sys.exit(NagiosResult.UNKNOWN)

    usage = shutil.disk_usage(path)
    used_pct = usage.used / usage.total * 100
    if used_pct > critical:
        print(
            f"CRITICAL: path={path} usage={used_pct:.2f}% used={usage.used} total={usage.total}"
        )
        sys.exit(NagiosResult.CRITICAL)
    if used_pct > warning:
        print(
            f"WARN: path={path} usage={used_pct:.2f}% used={usage.used} total={usage.total}"
        )
        sys.exit(NagiosResult.WARNING)
    print(
        f"OK: path={path} usage={used_pct:.2f}% used={usage.used} total={usage.total}"
    )
    sys.exit(NagiosResult.OK)
