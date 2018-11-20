def duplicateEncoder(string):
    string = string.upper()
    resultado = ""
    for letra in string:
        if string.count(letra) > 1:
            resultado = resultado + ")"
        else:
           resultado = resultado + "("
    return resultado


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert duplicateEncoder("din") == "((("

    # test case 2
    assert duplicateEncoder("recede") == "()()()"

    # test case 3
    assert duplicateEncoder("Success") == ")())())"

    # test case 4
    assert duplicateEncoder("(( @") == "))(("
