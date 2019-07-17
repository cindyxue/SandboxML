  from collections import Counter
  from modules.cuckooml.cuckooml import Loader
  from modules.cuckooml.cuckooml import ML

  loader = Loader()
  loader.load_binaries("../../sample_data/dict")

  ml = ML()
  ml.load_simple_features(loader.get_simple_features())
  ml.load_labels(loader.get_labels())

  # Remove uncommon labels
  new_labels = ml.labels.copy(True)
  a = Counter(list(ml.labels['label']))
  b = []
  for j in a:
      if a[j] < 10:
          b.append(j)
  new_labels = new_labels.replace(b, "wtr")

  # Pot groups for different learning rates
  for lr in [200, 250, 300, 350, 400, 450, 500, 550, 600]:
      for i in ml.SIMPLE_CATEGORIES:
          ml.visualise_data(data=ml.simple_feature_category(i),
                            labels=new_labels, fig_name=i,
                            learning_rate=lr)

  # Pot groups for different learning rates
  for lr in [200, 250, 300, 350, 400, 450, 500, 550, 600]:
      ml.visualise_data(data=ml.simple_features, labels=new_labels,
                        fig_name="all", learning_rate=lr)