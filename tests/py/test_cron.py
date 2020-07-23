from liberapay.cron import Weekly
from liberapay.testing import Harness


class TestCronJobs(Harness):

    def test_cron_jobs_with_empty_db(self):
        for period, func, exclusive in self.website.cron.jobs:
            if not isinstance(period, Weekly):
                func()
