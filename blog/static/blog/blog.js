for(let i = 0; i < 10; i += 1) {
  console.log("for loop : " + i)
}
i = 0
while(i < 10) {
  console.log("while loop " + i)
  i++
}
const numbers = [1, 2,3 ,4 ,5, 6, 7, 8, 9]

numbers.forEach(x => console.log("For Each: " + x))

const doubled = numbers.map(x => x*2)
console.log(doubled)