import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from autogluon.multimodal import MultiModalPredictor
import uuid
#os.environ['CUDA_LAUNCH_BLOCKING'] = "1"


#np.random.seed(123)

if __name__ == '__main__':
    dataset_path = 'data'

    train_data = pd.read_csv(f'{dataset_path}/train.csv')
    test_data = pd.read_csv(f'{dataset_path}/test.csv')
    label_col = 'label'
    image_col = 'image'
    
    train_data[image_col] = train_data[image_col].apply(lambda ele: ele.split(',')[0])
    test_data[image_col] = test_data[image_col].apply(lambda ele: ele.split(',')[0])

    def path_expander(path, base_folder):
        path_l = path.split(',')
        return ','.join([os.path.abspath(os.path.join(base_folder, path)) for path in path_l])

    train_data[image_col] = train_data[image_col].apply(lambda ele: path_expander(ele, base_folder=dataset_path))
    test_data[image_col] = test_data[image_col].apply(lambda ele: path_expander(ele, base_folder=dataset_path))

    from autogluon.multimodal import MultiModalPredictor
    predictor = MultiModalPredictor(label=label_col, problem_type="regression").fit(
        train_data=train_data,
        time_limit=12000
    )

    predictions = predictor.predict(test_data.drop(columns=label_col))

    # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
    scores = predictor.evaluate(test_data, metrics=["mean_absolute_percentage_error"])

    print(scores)
    scores = predictor.evaluate(test_data, metrics=["accuracy"])

    print('Top-1 test acc: %.3f' % scores["accuracy"])

