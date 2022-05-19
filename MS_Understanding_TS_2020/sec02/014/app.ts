function add(n1: number, n2: number, showResult: boolean, resultPhrase: string) {
  const result = n1 + n2;
  if (showResult) {
    console.log(resultPhrase + result);
  } else {
    return result;
  }
}
  
{
  let number1: number;
  // number1 = '42';
  number1 = 42;
  const number2 = 4.2;
  const printResult = true;
  const resultPhrase = 'Result: ';
  
  add(number1, number2, printResult, resultPhrase);
}