import common
import K
import raspisys


class Metadata:
  """Provides metadata such as the current time and stratum."""

  def __init__(self):
    self._log = K.get_logger(K.LOG_NAME_METADATA)

  def get_sample(self):
    return K.META_KEY, {# TODO: Avoid subprocess?
                        K.STRATUM_KEY: raspisys.get_stratum(),
                        K.CLIENT_TIMESTAMP_KEY: common.timestamp()}
