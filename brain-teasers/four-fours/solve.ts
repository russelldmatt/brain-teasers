function factorial(n: number): number {
  if (n < 0) throw new Error('Factorial is not defined for negative numbers');
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

type Expressions = Set<string>;
type BucketString = string;

class Bucket {
  value: number;
  numFours: number;

  constructor(value: number, numFours: number) {
    this.value = value;
    this.numFours = numFours;
  }

  toString() {
    return `${this.value}_${this.numFours}`;
  }
}

let allBuckets: Bucket[] = (function () {
  let buckets: Bucket[] = [];
  for (let numFours = 1; numFours <= 4; numFours++) {
    for (let value = 1; value <= 20 * 4 ** (4 - numFours); value++) {
      buckets.push(new Bucket(value, numFours));
    }
  }
  return buckets;
})();

class FourFoursSolver {
  buckets: Map<BucketString, Expressions> = new Map();

  constructor() {
    // Initialize the map with empty buckets
    for (let bucket of allBuckets) {
      this.buckets.set(bucket.toString(), new Set());
    }

    // Seed with initial values
    this.seedBuckets();
  }

  seedBuckets() {
    // We know we can make 4 with one 4
    this.buckets.get(new Bucket(4, 1).toString())?.add('4_1');
  }

  search() {
    let buckets = this.buckets;

    // Combine any two buckets
    for (let bucket1 of allBuckets) {
      let expressions1 = this.buckets.get(bucket1.toString())!;
      if (expressions1.size === 0) continue;

      // factorial
      (function () {
        let newBucket = new Bucket(factorial(bucket1.value), bucket1.numFours);
        buckets.get(newBucket.toString())?.add(`${bucket1}!`);
      })();

      for (let bucket2 of allBuckets) {
        let expressions2 = this.buckets.get(bucket2.toString())!;
        if (expressions2.size === 0) continue;

        this.combine(bucket1, bucket2);
      }
    }
  }

  combine(bucket1: Bucket, bucket2: Bucket) {
    let buckets = this.buckets;
    let { value: value1, numFours: numFours1 } = bucket1;
    let { value: value2, numFours: numFours2 } = bucket2;

    // Addition
    (function () {
      // just pick some ordering to avoid generating a + b AND b + a
      if (value1 > value2 || (value1 == value2 && numFours1 >= numFours2)) {
        let newBucket = new Bucket(value1 + value2, numFours1 + numFours2);
        buckets.get(newBucket.toString())?.add(`${bucket1} + ${bucket2}`);
      }
    })();

    // Multiplication
    (function () {
      // just pick some ordering to avoid generating a + b AND b + a
      if (value1 > value2 || (value1 == value2 && numFours1 >= numFours2)) {
        let newBucket = new Bucket(value1 * value2, numFours1 + numFours2);
        buckets.get(newBucket.toString())?.add(`${bucket1} * ${bucket2}`);
      }
    })();

    // Subtraction
    (function () {
      let newBucket = new Bucket(value1 - value2, numFours1 + numFours2);
      buckets.get(newBucket.toString())?.add(`${bucket1} - ${bucket2}`);
    })();

    // Division
    (function () {
      if (value2 !== 0 && value1 % value2 === 0) {
        let newBucket = new Bucket(value1 / value2, numFours1 + numFours2);
        buckets.get(newBucket.toString())?.add(`${bucket1} / ${bucket2}`);
      }
    })();
  }

  getResults(): Map<string, Expressions> {
    return this.buckets;
  }
}

// Instantiate the solver and get the results
const solver = new FourFoursSolver();

// Take 10 steps
for (let i = 0; i < 10; i++) {
  solver.search();
}

const results = solver.getResults();

function extractNumbers(input: string): number[] {
  const regex = /\d+_\d/g;
  const matches = input.match(regex);

  if (!matches) {
    return [];
  }

  return matches.map((match) => {
    const [numberPart] = match.split('_');
    return parseInt(numberPart, 10);
  });
}

let o = {};

for (let bucket of allBuckets) {
  if (
    bucket.numFours < 4 ||
    (bucket.numFours === 4 && bucket.value > 0 && bucket.value <= 20)
  ) {
    let expressions = results.get(bucket.toString())!;
    if (expressions.size > 0) {
      o[bucket.toString()] = Array.from(expressions);
      //   console.log(`${bucket}:`, Array.from(expressions));
    }
  }
}

console.log(o);
