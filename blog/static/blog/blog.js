class Greeter {
  constructor (name) {
    this.name = name
  }
  getGreeting() {
    if(this.name == undefined) {
      return "Hello No Name"
    } else {
      return "Hello " + this.name
    }
  }
  showGreeting(greatingMessage) {
    console.log(greatingMessage)
  }

  greet() {
    this.showGreeting(this.getGreeting())
  }
}
class DelayedGreeter extends Greeter {
  delay = 2000
  constructor(name, delay) {
    super(name)
    if(delay != undefined) {
      this.delay = delay
    }
  }
  greet() {
    setTimeout(() => {this.showGreeting(this.getGreeting())}, this.delay)
  }
}
const g = new Greeter("Lakshay")
g.greet()

const g2 = new DelayedGreeter("Singh", 2000)
g2.greet()

console.log("Delayed")