def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Only run tests if this file is executed directly (not when imported for integration)
# Or create a separate script file for tests
if __name__ == "__main__":
    # Test cases
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(42) == 'L')
    assert(size(38.5)=="M")
    assert(size(38)== 'M')          #38 is not included in S or M. Currently it returns L
    assert(size(15)=="Invalid")     #Smaller values should be invalid. Currently it returns S
    assert(size(60)=="Invalid")     #Larger values should be invalid. Currently it returns L
    assert(size(0)=="Invalid")      #Zero is not a valid size. Currently it returns S
    assert(size(-5)=="Invalid")     #Negative values should be invalid. Currently it returns S
    print("All is well (maybe!)")
