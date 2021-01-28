import os
import json

from buildpack import datadog


class TestCaseDatadogUtilFunctions:
    def test_get_service(self):

        tags_cases = [
            (["app:testapp", "service:testservice"], "testservice"),
            (["app:testapp"], "testapp"),
            (["service:testservice"], "testservice"),
            ([], "app"),
        ]

        for (tags, outcome) in tags_cases:
            os.environ["TAGS"] = json.dumps(tags)
            assert datadog.get_service() == outcome
