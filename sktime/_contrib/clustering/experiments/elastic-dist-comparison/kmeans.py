import numpy as np
import pandas as pd
import os

from sktime.benchmarking.experiments import run_clustering_experiment
from sktime.clustering.k_means import TimeSeriesKMeans
from sktime._contrib.clustering.experiments.base import BaseExperiment
from sktime._contrib.clustering.experiments.dataset_lists import EQUAL_LENGTH_LOWER

ignore_dataset = []

class KmeansExperiment(BaseExperiment):


    def _run_experiment_for_dataset(self, X_train: pd.DataFrame, y_train: np.ndarray,
                                    X_test: pd.DataFrame, y_test: np.ndarray, dataset_name: str):
        if dataset_name.lower() not in EQUAL_LENGTH_LOWER:
            return

        n_classes = len(set(y_train))

        k_means_clusterer = TimeSeriesKMeans(
            n_init=1,  # Set to 10 as num classes is 10
            n_clusters=n_classes,
            metric='euclidean',
        )

        run_clustering_experiment(
            X_train,
            k_means_clusterer,
            results_path=f'{self.result_path}/{self.experiment_name}',
            trainY=y_train,
            testX=X_test,
            testY=y_test,
            cls_name="kmeans",
            dataset_name=dataset_name,
            resample_id=0,
            overwrite=False,
        )

if __name__ == '__main__':
    kmeans_experiment = KmeansExperiment(
        experiment_name='test_experiment',
        dataset_path=os.path.abspath('C:/Users/chris/Documents/Masters/datasets/Univariate_ts/'),
        result_path=os.path.abspath('C:/Users/chris/Documents/Masters/results/'),
    )
    kmeans_experiment.run_experiment()

