function add(n1, n2, showResult, resultPhrase) {
    var result = n1 + n2;
    if (showResult) {
        console.log(resultPhrase + result);
    }
    else {
        return result;
    }
}
{
    var number1 = void 0;
    // number1 = '42';
    number1 = 42;
    var number2 = 4.2;
    var printResult = true;
    var resultPhrase = 'Result: ';
    add(number1, number2, printResult, resultPhrase);
}
