import unittest


def merge_ranges(meetings):

    # Merge meeting ranges
    # input:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    # return:   [(0, 1), (3, 8), (9, 12)]

    # sort by start times
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    merged_intervals = []
    
    start = sorted_meetings[0][0]
    end = sorted_meetings[0][1]
    for i in range(1, len(sorted_meetings)):
      interval = sorted_meetings[i]
      if interval[0] <= end:
        end = max(end, interval[1])
      else:
        merged_intervals.append((start, end))
        start = interval[0]
        end = interval[1]

    merged_intervals.append((start, end))

    return merged_intervals

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
