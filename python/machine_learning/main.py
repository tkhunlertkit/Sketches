from lib.utils import Utils
from models.d_trees.d_tree_model import DTreeModel
from models.d_trees.tree import Tree

if __name__ == '__main__':
    # Data setup
    examples_complete = [
        ['big',   'red',  'circle'   , 1], #1
        ['med',   'red',  'circle'   , 1], #1
        ['small', 'red',  'circle'   , 1], #1
        ['big',   'red',  'square'   , 0], #0
        ['med',   'red',  'square'   , 0], #0
        ['small', 'red',  'square'   , 0], #0
        ['big',   'red',  'triangle' , 1], #1
        ['med',   'red',  'triangle' , 1], #1
        ['small', 'red',  'triangle' , 1], #1
        ['big',   'green', 'circle'  , 0], #0
        ['med',   'green', 'circle'  , 0], #0
        ['small', 'green', 'circle'  , 0], #0
        ['big',   'green', 'square'  , 0], #0
        ['med',   'green', 'square'  , 0], #0
        ['small', 'green', 'square'  , 0], #0
        ['big',   'green', 'triangle', 0], #0
        ['med',   'green', 'triangle', 0], #0
        ['big',   'blue',  'circle'  , 0], #0
        ['big',   'blue',  'square'  , 0], #0
        ['big',   'blue',  'triangle', 0], #0
        ['med',   'blue',  'circle'  , 1], #1
        ['med',   'blue',  'square'  , 1], #1
        ['med',   'blue',  'triangle', 1], #1
        ['small', 'blue',  'circle'  , 0], #0
        ['small', 'blue',  'square'  , 0], #0
        ['small', 'blue',  'triangle', 0], #0
    ]
    examples        = [example[:-1] for example in examples_complete]
    expected_output = [example[-1] for example in examples_complete]
    feature_names = ['size', 'color', 'shape']
    feature_order = ['color', 'shape', 'size']

    # Model Training
    dtm = DTreeModel()
    dtm.train(examples, feature_names, expected_output, feature_order=feature_order)
    dtm.visualize('DTreeTestTrain', ['png'])

    # Model Prediction
    print('%s predicts: %s' % (['green', 'triangle', 'big'], dtm.predict(['green', 'triangle', 'big'], ['color', 'shape', 'size'])))
    print()
    print('%s predicts: %s' % (['big', 'white', 'star'], dtm.predict(['big', 'white', 'star'], ['size', 'color', 'shape'])))
    print()

    feature_names  = ['size', 'color', 'shape']
    feature_values = ['big', 'purple', 'star']
    print('%s predicts: %s' % (feature_values, dtm.predict(feature_values, feature_names)))
    print()

    feature_values = ['small', 'red', 'square']
    print('%s predicts: %s' % (feature_values, dtm.predict(feature_values, feature_names)))
    print()

    feature_values = ['small', 'red', 'triangle']
    print('%s predicts: %s' % (feature_values, dtm.predict(feature_values, feature_names)))
    print()

    feature_names  = ['what', 'color', 'shape']
    feature_values = ['blah', 'red', 'triangle']
    print('%s predicts: %s' % (feature_values, dtm.predict(feature_values, feature_names)))
