"""
PRACTICE Test 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS, SEQUENCES and MUTATION  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nicolas Bohner.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_zero_changer()


def run_test_zero_changer():
    """ Tests the    zero_changer    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   zero_changer   function:')
    print('--------------------------------------------------')

    # Test 1:
    test1 = ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
    expected1 = ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    zero_changer(test1)
    print()
    print('Test 1:')
    print('  Expected:', expected1)
    print('  Actual:  ', test1)

    # ------------------------------------------------------------------
    # Done: 2. Write at least 2 additional tests for the  zero_changer   function.
    #   Try do do some unexpected things like empty lists or an empty tuple.
    # ------------------------------------------------------------------
    test1 = ([0, 0, 0, 0, 0, 0], [2, 2, 2, 2], [1, 0, 1, 0, 1], [1, 2, 3, 5, 9])
    expected1 = ([1, 2, 3, 4, 5, 6], [2, 2, 2, 2], [1, 7, 1, 8, 1], [1, 2, 3, 5, 9])
    zero_changer(test1)
    print()
    print('Test 2:')
    print('  Expected:', expected1)
    print('  Actual:  ', test1)

    test1 = ([1, 1, 1, 1, 1], [0, 1, 1, 1, 1])
    expected1 = ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
    zero_changer(test1)
    print()
    print('Test 3:')
    print('  Expected:', expected1)
    print('  Actual:  ', test1)


def zero_changer(tuple_of_lists):
    """
    What comes in:  A TUPLE of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., none)
    Side effects:  The argument is MUTATED so that:
      -- the 1st 0 in the given tuple of lists is changed to 1.
      -- the 2nd 0 in the given tuple of lists is changed to 2.
      -- the 3rd 0 in the given tuple of lists is changed to 3.
           etc.
    Example:
      If the given tuple of lists is:
          ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
      then AFTER this function is called with that tuple of lists,
      the tuple of lists has been MUTATED to:
          ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    Note that:
      -- If there are no zeros in the given tuple of lists,
           then this function does nothing.
      -- After this function call, the tuple of lists IN THE CALLER
           should contain no zeros.
    Type hints:
      :type tuple_of_lists: tuple of list[int]
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  10 minutes.
    # ------------------------------------------------------------------
    count = 1
    for k in range(len(tuple_of_lists)):
        for j in range(len(tuple_of_lists[k])):
            if tuple_of_lists[k][j] == 0:
                tuple_of_lists[k][j] = count
                count = count+1

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------


main()
