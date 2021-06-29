def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
    def get_array():
        return []
    
class TestDataUniqueValues(object):
    def get_array():
        return [2,7,4,1,3]
    
    def get_expected_result():
        return  3
    
class TestDataExactlyTwoDifferentMinimums(object):
    def get_array():
        return sorted([3,4,2,6,2])
        
    def get_expected_result():
        return 0
