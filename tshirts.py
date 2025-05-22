def size(cms):
    if type(cms) != float and type(cms) != int:
        return "Invalid"
    if cms<30 or cms>50:
        return "Invalid" 
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Only run tests if this file is executed directly (not when imported for integration)
if __name__ == "__main__":
    # Test cases
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(42) == 'L')
    assert(size(38.5)=="M")
    assert(size(38)== 'M')
    assert(size(15)=="Invalid")
    assert(size(60)=="Invalid")
    assert(size(0)=="Invalid")
    assert(size(-5)=="Invalid")
    assert(size("abc")=="Invalid")
    print("All is well (maybe!)")
