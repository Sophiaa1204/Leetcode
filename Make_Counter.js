export default function makeCounter(initialValue) {
    let current = initialValue ? initialValue-1 : -1
    return () => {
      current += 1
      return current
    }
  }