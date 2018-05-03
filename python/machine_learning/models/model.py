import operator
from lib.utils import Utils

class Model(object):

    def __init__(self):
        self._feature_dict = {}
        pass

    @property
    def feature_dict(self):
        return self._feature_dict

    def train(self, data_input, expected_output):
        raise NotImplementedError('Implement <train> method')

    def predict(self, data_input):
        raise NotImplementedError('Implement <predict> method')

    def visualize(self, output_filename, file_format_list):
        raise NotImplementedError('Implement <visualize> method')

    def get_common_output(self, expected_output):
        out_clss = set(expected_output)
        highest_count = -1
        common_output = None
        for clss in out_clss:
            curr_count = len([x for x in expected_output if x == clss])
            if  curr_count > highest_count:
                highest_count = curr_count
                common_output = clss

        return common_output

    def generate_feature_dict(self, input_data, feature_names):
        for feature, feature_id in zip(feature_names, range(len(feature_names))):
            self.feature_dict[feature] = []
            for val in set([example[feature_id] for example in input_data]):
                self.feature_dict[feature].append(val)

    def entropy_analysis(self, input_data, expected_output):
        entropy_all = Utils.calculate_entropy(expected_output)

        num_features = 0
        num_examples = len(expected_output)
        for example in input_data:
            num_features = len(example)
            break
        gain = {}
        for i in range(num_features):
            feature_list = [example[i] for example in input_data]
            feature_choices = set(feature_list)
            entropy_features = 0
            for feature in feature_choices:
                expected_out_feature = [expected_output[i] for i, x in enumerate(feature_list) if x == feature]
                entropy_f = Utils.calculate_entropy(expected_out_feature)
                out_proportion = len(expected_out_feature) / num_examples
                entropy_features += out_proportion * entropy_f
            gain[i] = 1 - entropy_features

        return [x[0] for x in reversed(sorted(gain.items(), key=operator.itemgetter(1)))]