"""TODO(FLIC): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds

# TODO(FLIC): BibTeX citation
_CITATION = """
"""

# TODO(FLIC):
_DESCRIPTION = """
"""


class Flic(tfds.core.GeneratorBasedBuilder):
  """TODO(FLIC): Short description of my dataset."""

  # TODO(FLIC): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(FLIC): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        urls=[],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(FLIC): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # TODO(FLIC): Tune the number of shards such that each shard
            # is < 4 GB.
            num_shards=10,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={},
        ),
    ]

  def _generate_examples(self):
    """Yields examples."""
    # TODO(FLIC): Yields examples from the dataset
    yield {}

