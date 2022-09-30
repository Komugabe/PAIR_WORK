multi_table = [['X' if i==j==0 else max(i,j) if i*j == 0 else i*j for i in range(0,13)] for j in range(0,13)]

def test_multi_table_case():
    print()
    assert multi_table[0][0] == 'X'
    assert multi_table[2][0] == 2
    assert multi_table[0][2] == 2
    assert multi_table[6][6] == 36