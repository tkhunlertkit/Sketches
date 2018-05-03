import math
import operator
from models.model import Model
from models.d_trees.tree import Tree
from lib.utils import Utils

class DTreeModel(Model):

    def __init__(self):
        super(DTreeModel, self).__init__()
        self.model = Tree()
        self.common_output = None
        self.feature_order_num = None
        self.feature_order = None

    def train(self, input_data, feature_names, expected_output, feature_order=None):
        self.generate_feature_dict(input_data, feature_names)
        self.common_output = self.get_common_output(expected_output)
        self.feature_order_num = self.entropy_analysis(input_data, expected_output) if not feature_order else [feature_names.index(i) for i in feature_order]


        gain_sorted_example = []
        self.feature_order = self._sort_feature(feature_names)
        for example in input_data:
            gain_sorted_example.append(self._sort_feature(example))

        self.model = Tree('start', [self.train_feature(gain_sorted_example, self.feature_order, expected_output)])

    def _sort_feature(self, example, order=None):
        if not order:
            order = self.feature_order_num
        return [example[i] for i in order]

    def train_feature(self, input_data, feature_names, expected_output):
        # Case 1: If all the examples have the same expected output,
        # then use that output as prediction
        if len(set(expected_output)) == 1:
            return Tree(self.get_common_output(expected_output))

        # Case 2: If there are no more features left to build the tree,
        # then use the common expected output
        num_features = len(feature_names)
        if not num_features:
            return Tree(self.get_common_output(expected_output))

        # Else pick the feature F with highest information gain and create a node R for it
        #     For each possible value vi of F:
        #       Let examplesi be the subset of examples that have value vi for F
        #       Add an out-going edge E to node R labeled with the value vi.
        #           If examplesi is empty then attach a leaf node to edge E labeled with the category
        #               that is the most common in examples (or the default category).
        #           else call DTree(examplesi , features – {F}) and attach the resulting
        #               tree as the subtree under edge E.
        for feature, feature_id in zip(feature_names, range(num_features)):
            my_node = Tree(feature_names[0])
            for curr_feat in self.feature_dict[feature]:
                curr_feat_tree = Tree(curr_feat)
                trimmed_examples = [example for example in input_data if example[feature_id] == curr_feat]
                trimmed_expected_output = [output for example, output in zip(input_data, expected_output) if example[feature_id] == curr_feat]
                reduced_feature_example, reduced_feature_names = self._reduce_next_feature(trimmed_examples, feature_names)
                curr_feat_tree.add_sub_tree(self.train_feature(reduced_feature_example, reduced_feature_names, trimmed_expected_output))
                my_node.add_sub_tree(curr_feat_tree)
            return my_node

    def _reduce_next_feature(self, examples, features):
        reduced_feature_example = [example[1:] for example in examples]
        reduced_feature_names = features[1:]
        return reduced_feature_example, reduced_feature_names

    def predict(self, feature_values, feature_names):
        feature_order_num = [feature_names.index(feature) for feature in self.feature_order]
        sorted_feature_values = self._sort_feature(feature_values, feature_order_num)

        my_tree = self.model
        for feature_name, feature_val in zip(self.feature_order, sorted_feature_values):
            print(feature_name, feature_val)
            curr_node = my_tree.search_key(feature_name)
            if curr_node.is_leaf_node():
                return curr_node.data
            if curr_node == my_tree:
                print(feature_name, 'not found')
                continue
            next_node = curr_node.search_key(feature_val)
            if next_node == curr_node:
                print(feature_name, 'not found')
                continue
            my_tree = next_node
        if my_tree.is_leaf_node():
            return my_tree.data
        else:
            return self.common_output

    def visualize(self, output_filename, file_format_list):
        self.model.visualize(output_filename, file_format_list)

    @staticmethod
    def example():
        T = Tree('Start')
        t_red = Tree('red', [
            Tree('circle', [Tree('pos')]),
            Tree('square', [Tree('neg')]),
            Tree('triangle', [Tree('pos')])
        ])
        t_green = Tree('green', [Tree('neg')])
        t_blue = Tree('blue', [
            Tree('sml', [Tree('neg')]),
            Tree('med', [Tree('pos')]),
            Tree('big', [Tree('neg')]),
        ])
        T.add_sub_tree(t_red)
        T.add_sub_tree(t_green)
        T.add_sub_tree(t_blue)
        T.visualize('DTreeTest', ['png', 'svg'])
        for node in T:
            print(node.data, node.is_leaf_node())
