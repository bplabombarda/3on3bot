import datetime
import logging

from schedule import Scheduler

logger = logging.getLogger('schedule')


class CustomScheduler(Scheduler):
    """
    An implementation of Scheduler that catches jobs that fail and logs their
    exception as an error.
    Use this to run jobs that may or may not crash as to not affect other jobs
    that are scheduled to run.
    """

    def __init__(self):
        super().__init__()

    def _run_job(self, job):
        try:
            super()._run_job(job)
        except Exception as e:
            logger.exception(e)
            job.last_run = datetime.datetime.now()
            job._schedule_next_run()
