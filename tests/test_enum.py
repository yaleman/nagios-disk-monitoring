from nagios_disk_monitoring import NagiosResult


def test_str() -> None:
    NagiosResult.OK.__str__() == "OK"
    NagiosResult.OK.value == 0
