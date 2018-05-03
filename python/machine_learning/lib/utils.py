import os
import math

class Utils(object):

    @staticmethod
    def execute_dot_file(dot_file, formats):
        filename = dot_file[:-4]
        for form in formats:
            format_flag = '-T%s' % form
            execute = 'dot %s %s > %s.%s' % (dot_file, format_flag, filename, form)
            os.system(execute)

    @staticmethod
    def calculate_entropy(feature_list):
        classifier = set(feature_list)
        num_examples = len(feature_list)
        entropy = 0
        for clss in classifier:
            num_clss = len([x for x in feature_list if x == clss])
            prob_clss = num_clss / num_examples
            entropy += -prob_clss * math.log2(prob_clss)

        return entropy