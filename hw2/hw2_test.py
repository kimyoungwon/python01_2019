from cse163_utils import assert_equals
# Don't worry about this import syntax, we will talk about it later

import hw2_manual
import hw2_pandas

# This file is left blank for you to fill in with your tests!
DATA1 = 'pokemon_test.csv'
DATA2 = 'pokemon_test_by_yw.csv'
integer_cols = ['id', 'level', 'atk', 'def', 'hp', 'stage']

data1 = hw2_manual.parse(DATA1, integer_cols)
data2 = hw2_pandas.parse(DATA1)
data3 = hw2_manual.parse(DATA2, integer_cols)
data4 = hw2_pandas.parse(DATA2)

def test_species_count():
    """
    Tests the function: species_count
    """
    print('Testing species_count')

    # Cases from the made up "spec" for this problem
    assert_equals(3, hw2_manual.species_count(data1))
    assert_equals(3, hw2_pandas.species_count(data2))
    # Additional two cases
    assert_equals(7, hw2_manual.species_count(data3))
    assert_equals(7, hw2_pandas.species_count(data4))

def test_max_level():
    """
    Tests the function: max_level
    """
    print('Testing max_level')

    # Cases from the made up "spec" for this problem
    assert_equals(('Lapras', 72), hw2_manual.max_level(data1))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(data2))
    # Additional two cases
    assert_equals(('Lapras', 72), hw2_manual.max_level(data3))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(data4))

def test_filter_range():
    """
    Tests the function: filter_range
    """
    print('Testing filter_range')

    # Cases from the made up "spec" for this problem
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'], hw2_manual.filter_range(data1, 30, 70))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'], hw2_pandas.filter_range(data2, 30, 70))
    # Additional two cases
    assert_equals(['Arcanine', 'Arcanine', 'Starmie', 'Persian', 'Magmar', 'Kingler'], hw2_manual.filter_range(data3, 30, 70))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie', 'Persian', 'Magmar', 'Kingler'], hw2_pandas.filter_range(data4, 30, 70))

def test_mean_attack_for_type():
    """
    Tests the function: mean_attack_for_type
    """
    print('Testing mean_attack_for_type')

    # Cases from the made up "spec" for this problem
    assert_equals(47.5, hw2_manual.mean_attack_for_type(data1, 'fire'))
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(data2, 'fire'))
    # Additional two cases
    assert_equals(63.666666666666664, hw2_manual.mean_attack_for_type(data3, 'fire'))
    assert_equals(63.666666666666664, hw2_pandas.mean_attack_for_type(data4, 'fire'))

def test_count_types():
    """
    Tests the function: count_types
    """
    print('Testing count_types')

    # Cases from the made up "spec" for this problem
    assert_equals({'water': 2, 'fire': 2}, hw2_manual.count_types(data1))
    assert_equals({'water': 2, 'fire': 2}, hw2_pandas.count_types(data2))
    # Additional two cases
    assert_equals({'fighting': 1, 'fire': 3, 'normal': 1, 'water': 3}, hw2_manual.count_types(data3))
    assert_equals({'fighting': 1, 'fire': 3, 'normal': 1, 'water': 3}, hw2_pandas.count_types(data4))

def test_highest_stage_per_type():
    """
    Tests the function: highest_stage_per_type
    """
    print('Testing highest_stage_per_type')

    # Cases from the made up "spec" for this problem
    assert_equals({'water': 2, 'fire': 2}, hw2_manual.highest_stage_per_type(data1))
    assert_equals({'water': 2, 'fire': 2}, hw2_pandas.highest_stage_per_type(data2))
    # Additional two cases
    assert_equals({'fighting': 2, 'fire': 2, 'normal': 2, 'water': 2}, hw2_manual.highest_stage_per_type(data3))
    assert_equals({'fighting': 2, 'fire': 2, 'normal': 2, 'water': 2}, hw2_pandas.highest_stage_per_type(data4))

def test_mean_attack_per_type():
    """
    Tests the function: mean_attack_per_type
    """
    print('Testing mean_attack_per_type')

    # Cases from the made up "spec" for this problem
    assert_equals({'water': 140.5, 'fire': 47.5}, hw2_manual.mean_attack_per_type(data1))
    assert_equals({'water': 140.5, 'fire': 47.5}, hw2_pandas.mean_attack_per_type(data2))
    # Additional two cases
    assert_equals({'fighting': 20.0, 'fire': 63.666666666666664, 'normal': 104.0, 'water': 130.33333333333334}, hw2_manual.mean_attack_per_type(data3))
    assert_equals({'fighting': 20.0, 'fire': 63.666666666666664, 'normal': 104.0, 'water': 130.33333333333334}, hw2_pandas.mean_attack_per_type(data4))

def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_highest_stage_per_type()
    test_mean_attack_per_type()

if __name__ == '__main__':
    main()
