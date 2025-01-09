# test the Huffman Tree Node generator

from Huffman_Tree import Huffman_Encoding

Huffman_Encoding('test')

def test_encoding():
    assert Huffman_Encoding('test') == """symbols:  dict_keys(['t', 'e', 's'])
probabilities:  dict_values([2, 1, 1])
symbols with codes {'s': '00', 'e': '01', 't': '1'}
Space usage before compression (in bits): 32
Space usage after compression (in bits): 6"""