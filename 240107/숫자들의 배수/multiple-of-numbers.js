const input = () => require('fs').readFileSync('/dev/stdin').toString().trim();

N = Number(input())
const result = []
let count = 2;

for (let i = N; count!=0; i+=N){
result.push(i);
if (i%5==0)
    count--;
}
console.log(result.join(' '))